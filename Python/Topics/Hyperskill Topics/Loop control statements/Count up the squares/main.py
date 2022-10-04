nums, s = [int(input())], 0

while sum(nums):
    nums.append(int(input()))
for i in nums:
    s += i ** 2
print(0 if nums[0] == 0 else s)
