from flask import Flask, request, g, abort, jsonify
import sqlite3
from correlations import correlation, train
from datetime import datetime
import os
from math import isnan
from vectorCode import decodeVect, encodeVect
from numpy import std

app = Flask(__name__)

@app.route('/v0/get/correlation', methods = ['POST'])
def query_correlation():
	if not request.json or not 'user' in request.json:
		abort(400)

	db = get_db()
	cursor = db.execute("select vector from moodEntry_activityvector")
	vecs = cursor.fetchall()
	packed_vecs = map(lambda x: x[0], vecs)
	decoded = map(decodeVect, packed_vecs)
	correls = [correlation(x, decoded) for x in xrange(10)]
	mood_dev = std(map(lambda x: x[10], decoded))

	json_data = map(lambda x: { 
			'status': 'success' if not isnan(x) else 'failure',
			'msg'   : '' if not isnan(x) else 'Mood Unchanging' if mood_dev == 0 else 'Event Always Occurs',
			'code'  : 0 if not isnan(x) else 102 if mood_dev == 0 else 103,
			'value' : x}, correls)

	return jsonify( { 'correlations': json_data } ), 201

def get_vector(start, end):
	db = get_db()

	vector_cur = db.execute("""SELECT 
									moodEntry_activity.no
								FROM 
									moodEntry_activityattime 
									INNER JOIN moodEntry_activity
									ON moodEntry_activityattime.activity_id = moodEntry_activity.id
								WHERE 
									(moodEntry_activityattime.timeStart BETWEEN datetime(?) AND datetime(?)) OR
									(moodEntry_activityattime.timeStop BETWEEN datetime(?) AND datetime(?))""",
							[start_date.isoformat(' '), end_date.isoformat(' '), start_date.isoformat(' '), end_date.isoformat(' ')])


	feature_unencoded = map(lambda x: x[0], vector_cur.fetchall())

	return[1 if any(map(lambda x: x == i, feature_unencoded)) else 0 for i in xrange(10)]

@app.route('/v0/get/predictions', methods = ['POST'])
def query_predictions_batch():
	if not request.json or not 'user' in request.json or not 'intervals' in request.json:
		abort(400)

	intervals = [(date_parse(pair['start']), date_parse(pair['end'])) for pair in request.json['intervals']]

	# would like to batch the DB queries but not sure how atm, and not enough time
	feature_vecs = map(lambda x: get_vector(x[0], x[1]), intervals)

	# shouldn't be None in any of these pairs but is probably worth checking; add this in

	cursor = db.execute("select vector from moodEntry_activityvector")
	vecs = cursor.fetchall()
	packed_vecs = map(lambda x: x[0], vecs)
	decoded = map(decodeVect, packed_vecs)

	try:
		clf = train(decoded)
	except ValueError:
		response = {
			'msg'    : 'Insufficient Data',
			'code'   : 101,
			'status' : 'failure'
		}

		return jsonify( response ), 418

	response = {
			'predictions' : map(lambda x: {
								'msg'    : '',
								'status' : 'success',
								'code'   : 0,
								'value'  : clf.predict(get_vector(x[0], x[1]))[0] # get predicting vector
							}, feature_vecs)
	}


@app.route('/v0/get/prediction/for/<start>/to/<end>', methods = ['POST'])
def query_prediction(start, end):
	if not request.json or not 'user' in request.json:
		abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	if start_date is None or end_date is None:
		abort(400)

	db = get_db()


	cursor = db.execute("select vector from moodEntry_activityvector")
	vecs = cursor.fetchall()
	packed_vecs = map(lambda x: x[0], vecs)
	decoded = map(decodeVect, packed_vecs)

	try:
		clf = train(decoded)
	except ValueError:
		response = {
			'msg'    : 'Insufficient Data',
			'code'   : 101,
			'status' : 'failure'
		}

		return jsonify( response ), 418

	response = {
		'msg'    : '',
		'status' : 'success',
		'code'   : 0,
		'value'  : clf.predict(get_vector(start_date, end_date))[0] # get predicting vector
	}
	return jsonify( response ), 201

@app.route('/v0/get/activities/between/<start>/and/<end>', methods = ['POST'])
def get_activities(start, end):
	if not request.json or not 'user' in request.json: # complete 
	   	abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	if start_date is None or end_date is None:
		response = {
			'status' : 'failure',
			'code'   : 105,
			'msg'    : 'Incorrect Date Format'
		}

		return jsonify(response), 418

	db = get_db()

	activities = db.execute("""SELECT 
									moodEntry_activity.no,
									moodEntry_activityattime.timeStart,
									moodEntry_activityattime.timeStop,
									moodEntry_activityattime.description
								FROM 
									moodEntry_activityattime 
									INNER JOIN moodEntry_activity
									ON moodEntry_activityattime.activity_id = moodEntry_activity.id
								WHERE 
									(moodEntry_activityattime.timeStart BETWEEN datetime(?) AND datetime(?)) OR
									(moodEntry_activityattime.timeStop BETWEEN datetime(?) AND datetime(?))""", 
							[start_date.isoformat(' '), end_date.isoformat(' '), start_date.isoformat(' '), end_date.isoformat(' ')])
	

	# this needs finished, get the activities into interval form

	# response = {
	# 	'1hour' : intervals_one,
	# 	'4hour' : intervals_four,
	# 	'6hour' : intervals_six,
	# 	'12hour': intervals_twelve,
	# 	'24hour': intervals_days
	# }
	# return jsonify( { 'intervals' : response } ), 201
	return jsonify(activities)

@app.route('/v0/add/activity/from/<start>/to/<end>', methods = ['POST'])
def add_activity(start, end):
	if not request.json or not 'user' in request.json or not 'category' in request.json:
	   	abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	if start_date is None or end_date is None:
		response = {
			'status' : 'failure',
			'code'   : 105,
			'msg'    : 'Incorrect Date Format'
		}

		return jsonify(response), 418

	no = request.json['category']

	desc = request.json['desc'] if 'desc' in request.json else ''

	if len(desc) >= 200:
		response = {
			'status' : 'failure',
			'code'   : 104,
			'msg'    : 'Description Too Long'
		}

		return jsonify( response ), 418

	db = get_db()

	activity_id = db.execute('select id from moodEntry_activity where no = ?', [no]).fetchone()

	# should check for existence; we assume it does at the moment

	app.logger.debug(activity_id[0])

	db.execute("""insert into moodEntry_activityattime 
		(user_id, activity_id, timeStart, timeStop, description) 
		values (2, ?, datetime(?), datetime(?), ?)""", 
		[activity_id[0], start_date.isoformat(' '), end_date.isoformat(' '), desc])
	
	db.commit()

	response = {
		'status' : 'success',
		'code'   : 0,
		'msg'    : ''
	}
	return jsonify(response), 201 # change 201 depending on success_state

@app.route('/v0/add/mood/at/<time>', methods = ['POST'])
def add_mood(time):
	if not request.json or not 'user' in request.json or not 'mood' in request.json:
	   	abort(400)

	time_date = date_parse_ws(time)

	if time_date is None:
		response = {
			'status' : 'failure',
			'code'   : 105,
			'msg'    : 'Incorrect Date Format'
		}

		return jsonify(response), 418
	# compose db request (output success_state)

	db = get_db()

	most_recent_mood = db.execute("select MAX(time) AS max_time from moodEntry_moodattime").fetchone()

	app.logger.debug(most_recent_mood[0])

	mrm_time = date_parse_db(most_recent_mood[0]) # we can assume this isn't None since it's not null in the db

	if mrm_time >= time_date:
		response = {
			'status' : 'failure',
			'code'   : 106,
			'msg'    : 'Invalid Time (Attempting to time-travel)'
		}

		return jsonify(response), 418

	db.execute("insert into moodEntry_moodattime (mood, time, user_id) values (?, datetime(?), 2)", [request.json['mood'], time_date.isoformat(' ')])
	db.commit()

	activities = db.execute("""SELECT 
								moodEntry_activity.no
							FROM 
								moodEntry_activityattime 
								INNER JOIN moodEntry_activity
								ON moodEntry_activityattime.activity_id = moodEntry_activity.id
							WHERE 
								(moodEntry_activityattime.timeStart BETWEEN datetime(?) AND datetime(?)) OR
								(moodEntry_activityattime.timeStop BETWEEN datetime(?) AND datetime(?))""",
						[mrm_time.isoformat(' '), time_date.isoformat(' '), mrm_time.isoformat(' '), time_date.isoformat(' ')])

	# get all numbers of activites between mood times
	feature_unencoded = map(lambda x: x[0], activities.fetchall())
	app.logger.debug(feature_unencoded)

	# create/encode vector
	features = [1 if any(map(lambda x: x == i, feature_unencoded)) else 0 for i in xrange(10)]
	features.append(request.json['mood'])
	encoded = encodeVect(features)

	# store vector
	db.execute("insert into moodEntry_activityvector (vector, user_id) values (?, 2)", [encoded])

	db.commit()

	response = {
		'status' : 'success',
		'code'   : 0,
		'msg'    : ''
	}
	return jsonify(response), 201 # change 201 depending on success_state

# Uses format string %Y%m%d%H%M
def date_parse(input):
		try:
			return datetime.strptime(input, "%Y%m%d%H%M")
		except ValueError:
			return None

def date_parse_ws(input):
		try:
			return datetime.strptime(input, "%Y%m%d%H%M%S")
		except ValueError:
			return None

def date_parse_db(input):
		try:
			return datetime.strptime(input, "%Y-%m-%d %H:%M:%S")
		except ValueError:
			return None

def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

if __name__ == '__main__':	
	app.config.update(dict(
    	DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    	DEBUG=True,
    	SECRET_KEY='development key',
    	USERNAME='admin',
    	PASSWORD='default'
	))

	app.run()