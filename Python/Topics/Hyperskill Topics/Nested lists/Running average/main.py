nums_l = [int(num) for num in input()]
print([((nums_l[i] + nums_l[i + 1]) / 2) for i in range(0, len(nums_l) - 1)])
