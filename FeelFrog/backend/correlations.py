from sklearn import tree
import random
from math import floor
from scipy import stats

def gen_data(n):
	return [[random.randint(0,1) for r in xrange(10)] + [random.randint(1,5)] for p in xrange(n)]


def foldr(f, z, l):
	for i in xrange(len(l)):
		z = f(l.pop(), z)

	return z



def gen_data_biased(n):
	event_moods = [random.randint(1,4) for r in xrange(10)]
	event_biases = [random.random() for r in xrange(10)]
	event_bias_total = sum(event_biases)

	scenarios = [[(random.randint(0,1),r) for r in xrange(10)] for p in xrange(n)]

	#for each scenario [(x1, i1), ...]:
	# - if x1 == 1, event_biases[i1] * event_moods[i1]
	# - else 0
	# sum these (a fold; the proper kind, not reduce)

	def weighted(l, r):
		xi, ii = l
		s, w = r
		if xi == 1:
			return ((event_biases[ii] * event_moods[ii]) + s, event_biases[ii] + w)
		else:
			return r

	return [map(lambda x: x[0], s) + [1 + foldr(lambda x,y: x/y, 1,[x for x in foldr(weighted, (0,1), s)])] for s in scenarios]


def train(t):
	input = map(lambda x: map(lambda y: 1 if y == 1 else -1, x[0:-1]), t)
	output = map(lambda x: x[-1], t)
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(input, output)
	return clf

def predicted_mood(i, model):
	# if you liked python, you probably won't after what i've done to it
	seqs = [[x1, x2, x3, x4, x5, x6, x7, x8, x9] for x1 in xrange(2) 
	                                             for x2 in xrange(2)
	                                             for x3 in xrange(2)
	                                             for x4 in xrange(2)
	                                             for x5 in xrange(2)
	                                             for x6 in xrange(2)
	                                             for x7 in xrange(2)
	                                             for x8 in xrange(2)
	                                             for x9 in xrange(2)]

	map(lambda x: x.insert(i, 1), seqs)

	# uses square of the number of activities in each interval as weight
	# this is perhaps not optimal at the moment but we need better test data
	# to show this. it might be okay as a weighting method however, 
	# since it gives more priority to cases where the activity is the only one
	# which happened, and less to ones where the activity would have less influence.
	# A more advanced model could take into account the order in which the activities
	# occurred (since people tend to psychologically rate their mood according
	# to what happened most recently), or perhaps a probablistic model based on
	# past data with smoothing (similar to basic expectation) to better account
	# for a person's behaviour patterns?
	normaliser = sum(map(lambda x: 1.0/pow(x.count(1),2), seqs))
	numerator = sum(map(lambda x: (1.0/pow(x.count(1),2)) * model.predict(x), seqs))

	return numerator / normaliser

def moodEquals(n):
	return lambda x: x[10] == n

def happened(n):
	return lambda x: x[n] == 1

# Correlation between variable n and mood value
# assumes 9 >= n >= 0
def correlation(n,t):
	event = map(lambda x: x[n], t)
	moods = map(lambda x: x[10], t)

	c, p = stats.pearsonr(event, moods)

	return c

