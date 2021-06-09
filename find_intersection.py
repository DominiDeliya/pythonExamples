def FindIntersection(strArr):

  setOne = set(strArr[0].split(", "))
  setTwo = set(strArr[1].split(", "))

  result = sorted(list(setOne.intersection(setTwo)), key=lambda str: int(str))
  return ','.join(result) if len(result) > 0 else False

  # code goes here
  return strArr

# keep this function call here
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))