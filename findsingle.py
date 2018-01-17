def findsg(data):
	length = len(data)
	num = 0
	for i in range(length):
		num ^= data[i]
	return num

def main():
	data = [1,1,2,2,3,3,4]
	print(findsg(data))

if __name__ == '__main__':
	main()