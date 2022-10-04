nums = list(iter(input, '.'))
m = float(nums[0])
for i in nums:
    if float(i) < m:
        m = float(i)
print(m)
