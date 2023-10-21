
def differenceOfSum(nums: list[int]) -> int:
  digit = 0
  sums = sum(nums)
  for i in nums:
    if i < 10:
      digit += i
    else:
      digit += sum([int(j) for j in str(i)])
  
  return abs(digit - sums)


print(differenceOfSum([1,2,3,4]))