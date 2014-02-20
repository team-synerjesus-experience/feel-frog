from flask import Flask
from correlations import correlation, train
import datetime
app = Flask(__name__)

@app.route('/v0/get/correlation', methods = ['POST'])
def query_correlation():
	if not request.json or not 'user' in request.json:
		abort(400)

	# query database for vectors

	response = {
		'values': [correlation(i, t) for i in xrange(10)]
	}
	return jsonify( { 'correlations': response } ), 201

@app.route('/v0/get/prediction/for/<start>/to/<end>', methods = ['POST'])
def query_prediction():
	if not request.json or
	   not 'user' in request.json:
		abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	# how do we get the vector we're trying to predict

	# query database for vectors

	clf = train(vectors) # make vectors exist

	response = {
		'value': clf.predict(features) # get predicting vector
	}
	return jsonify( { 'prediction': response } ), 201

@app.route('/v0/get/activites/between/<start>/and/<end>', method = ['POST'])
def get_activities(start, end):
	if not request.json or
	   not 'user' in request.json: # complete 
	   	abort(400)

	start_date = date_parse(start)
	end_date = date_parse(end)

	if start_date is None or end_date is None:
		abort(400)

	# get intervals out

	response = {
		'1hour' : intervals_one,
		'4hour' : intervals_four,
		'6hour' : intervals_six,
		'12hour': intervals_twelve,
		'24hour': intervals_days
	}
	return jsonify( { 'intervals' : response } ), 201

@app.route('/v0/add/activity', method = ['POST'])
def add_activity():
	if not request.json or
	   not 'user' in request.json or
	   not 'name' in request.json or
	   not 'category' in request.json or
	   not 'start' in request.json or
	   not 'end' in request.json:
	   	abort(400)

	# compose db request (output success_state)

	response = {
		'success' : success_state
	}
	return jsonify(response), 201 # change 201 depending on success_state

@app.route('/v0/add/mood', method = ['POST'])
def add_mood():
	if not request.json or
	   not 'user' in request.json or
	   not 'mood' in request.json or
	   not 'time' in request.json:
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

