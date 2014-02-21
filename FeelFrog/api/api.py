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

@app.route('/v0/get/prediction/for/<start>/to/<end>', methods = ['POST'])
def query_prediction(start, end):
	if not request.json or not 'user' in request.json:
		abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	if start_date is None or end_date is None:
		abort(400)

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
	app.logger.debug(feature_unencoded)

	features = [1 if any(map(lambda x: x == i, feature_unencoded)) else 0 for i in xrange(10)]

	cursor = db.execute("select vector from moodEntry_activityvector")
	vecs = cursor.fetchall()
	packed_vecs = map(lambda x: x[0], vecs)
	decoded = map(decodeVect, packed_vecs)

	try:
		clf = train(decoded)
	except ValueError:
		response = {
			'msg' : 'Insufficient Data',
			'code': 101
		}

		return jsonify( { 'error' : response } ), 418

	response = {
		'value': clf.predict(features)[0] # get predicting vector
	}
	return jsonify( { 'prediction': response } ), 201

@app.route('/v0/get/activites/between/<start>/and/<end>', methods = ['POST'])
def get_activities(start, end):
	if not request.json or not 'user' in request.json: # complete 
	   	abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	if start_date is None or end_date is None:
		abort(400)

	db = get_db()

	vector_cur = db.execute("""SELECT 
									moodEntry_activity.no
									moodEntry_activityattime.timestart
									moodEntry_activityattime.timestop
									moodEntry_activityattime.description
								FROM 
									moodEntry_activityattime 
									INNER JOIN moodEntry_activity
									ON moodEntry_activityattime.activity_id = moodEntry_activity.id
								WHERE 
									(moodEntry_activityattime.timeStart BETWEEN datetime(?) AND datetime(?)) OR
									(moodEntry_activityattime.timeStop BETWEEN datetime(?) AND datetime(?))""", 
							[start_date.isoformat(' '), end_date.isoformat(' '), start_date.isoformat(' '), end_date.isoformat(' ')])
	

<<<<<<< HEAD
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
=======
	response = {
		'1hour' : intervals_one,
		'4hour' : intervals_four,
		'6hour' : intervals_six,
		'12hour': intervals_twelve,
		'24hour': intervals_days
	}
	return jsonify( { 'intervals' : response } ), 201
>>>>>>> e8d28583f19b8502de753a2de8b04ea6fb96d493

@app.route('/v0/add/activity', methods = ['POST'])
def add_activity():
	if not request.json or not 'user' in request.json or not 'name' in request.json or not 'category' in request.json or not 'start' in request.json or not 'end' in request.json:
	   	abort(400)

	# compose db request (output success_state)

	response = {
		'success' : success_state
	}
	return jsonify(response), 201 # change 201 depending on success_state

@app.route('/v0/add/mood', methods = ['POST'])
def add_mood():
	if not request.json or not 'user' in request.json or not 'mood' in request.json or not 'time' in request.json:
	   	abort(400)

	# compose db request (output success_state)

		# get most recent mood time 
		# store mood
		# get all numbers of activites between mood times
		# create/encode vector
		# store vector

	response = {
		'success' : success_state
	}
	return jsonify(response), 201 # change 201 depending on success_state

# Uses format string %Y%m%d%H%M
def date_parse(input):
		try:
			return datetime.strptime(input, "%Y%m%d%H%M")
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