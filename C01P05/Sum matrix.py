def sum_matrix(m):
	result = 0 
	for row in m:
		for x in row:
			result += x
	return result			




tests = [
    (
    	[
    		[1, 2, 3],
    		[4, 5, 6],
    		[7, 8, 9]
    	],	
    	45
    ),
    (
    	[
    	[0, 0, 0], 
    	[0, 0, 0], 
    	[0, 0, 0]
    	],
    	0
    ),
    (
    	[
    		[1, 2],
  			[3, 4],
  			[5, 6],
  			[7, 8],
  			[9, 10]
  		],
  		55
  	)
]

for m, expected in tests:
    result = sum_matrix(m)
    # print(f"'{expected}', '{result}'")
    # print(expected, result)
    print(result == expected)