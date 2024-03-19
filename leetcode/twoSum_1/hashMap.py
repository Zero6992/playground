def twoSum(self, nums, target):
  map = {}
  for index, value in enumerate(nums):
    remaining = target - value
    if remaining in map:
      return [map[remaining], index]
    map[value] = index