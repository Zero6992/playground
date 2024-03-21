def subsets(nums: list[int]) -> list[list[int]]:
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output





