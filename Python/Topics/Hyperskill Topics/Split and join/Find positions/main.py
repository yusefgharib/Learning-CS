nums = input().split()
look = input()
found = [str(i) for i in range(len(nums)) if nums[i] == look]
print(' '.join(found) if found else 'not found')
