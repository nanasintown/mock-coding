def maximumEvenSplit(finalSum: int) -> list[int]:
  # get even numbers
  res = []
  evennum = []
  total = 0
  curr = 2
  if finalSum % 2:
    return res
  for i in range(2, finalSum + 1):
    if i % 2 == 0:
      evennum.append(i)
  while total < finalSum:
    total += curr
    res.append(curr)
    curr += 2
  
  if total == finalSum:
    return res
  else:
    res.pop(res.index(total - finalSum))

  return res

result = maximumEvenSplit(28)
print(result)


        