from math import sqrt, pow

def lin_dist(x,y):
	return sqrt(sum(map(lambda t: pow(t[0] - t[1],2), zip(x,y))))

def similarity(x,y):
	return 1.0/(1 + lin_dist(x,y))

def predict_emotion(z, t):
	normaliser = 1.0/sum(map(lambda v: similarity(z, v[0:-1]), t))
	total = sum(map(lambda v: similarity(z, v[0:-1])*v[-1], t))
	return normaliser * total
