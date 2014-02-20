def decodeVect(encoded):
	vector = []
	for x in range(0, 9):
		vector.append(((self.encoded)>>x)%2)
	vector.append(((self.encoded)>>10)%8)
	return vector

def encodeVect(vector)