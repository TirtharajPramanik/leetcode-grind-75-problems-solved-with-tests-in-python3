def get_result(nums, target):
    for idx, num in enumerate(nums):
        numx = nums.copy()
        numx.pop(idx)
        prob = target - num
        try:
            nxt = numx.index(prob)+1
        except ValueError:
            continue
        return idx, nxt


a = [1, 2, 3]
print(a[~1])
print(a)
