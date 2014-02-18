from sklearn import tree
import random

def gen_data(n):
	return [[random.randint(0,1) for r in xrange(10)] + [random.randint(1,5)] for p in xrange(n)]


def train(t):
	input = map(lambda x: map(lambda y: 1 if y == 1 else -1, x[0:-1]), t)
	output = map(lambda x: x[-1], t)
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(input, output)
	return clf

