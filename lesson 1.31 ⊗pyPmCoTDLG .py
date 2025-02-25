# С помощью включения сделайте следующий список:

# [
# 	[1, 2, 3, 4, 5],
# 	[1, 2, 3, 4, 5],
# 	[1, 2, 3, 4, 5],
# ]

lst = [[j for j in range(1, 6)] for i in range(0, 3)]
print(lst) # [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# 2.С помощью включения сделайте следующий список:

[
	[
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3],
	],
	[
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3],
	],
	[
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3],
	],
]

lst = [[[j for j in range(1, 4)] for i in range(0, 3)] for x in range(0, 3)]
print(lst) # [[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]