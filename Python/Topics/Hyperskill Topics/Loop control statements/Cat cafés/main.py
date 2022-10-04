cats = list(iter(input, 'MEOW'))
nums, names, m, idx = [], [], 0, 0

for i in range(len(cats)):
    for j in range(0, len(cats[i])):
        if cats[i][j] == " ":
            nums.append(int(cats[i][j + 1:]))
            names.append(cats[i][:j])
            
for x in range(len(nums)):
    if nums[x] > m:
        m = nums[x]
        idx = x
        
print(names[idx])
