def CountPairs(a, b, n):
	
	# Stores the sum of element at
	# each corresponding index
	C = [0] * n

	# Find the sum of each index
	# of both array
	for i in range(n):
		C[i] = a[i] + b[i]
	
	# Stores frequency of each element
	# present in sumArr
	freqCount = dict() 

	for i in range(n):
		if C[i] in freqCount.keys(): 
			freqCount[C[i]] += 1
		else:
			freqCount[C[i]] = 1

	# Initialize number of pairs
	NoOfPairs = 0

	for x in freqCount:
		y = freqCount[x]

		# Add possible valid pairs
		NoOfPairs = (NoOfPairs + y *
					(y - 1) // 2)
	
	# Return Number of Pairs
	print(NoOfPairs)

# Driver Code

# Given array arr[] and brr[]
arr = [ 2, -2, 5, 3 ]
brr = [ 1, 5, -1, 1 ]

# Size of given array
N = len(arr)

# Function calling
CountPairs(arr, brr, N)
