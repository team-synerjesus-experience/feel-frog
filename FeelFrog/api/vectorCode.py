def decodeVect(encoded):
	vector = []
	for x in range(0, 10):
		vector.append(((encoded)>>x)%2)
	vector.append(((encoded)>>10)%8)
	return vector

def encodeVect(vector):
	encoded = 0
	for i in range(0, 10):
		if vector[i]:
			encoded += (vector[i]<<i)
	encoded += (vector[10]<<10)
	return encoded