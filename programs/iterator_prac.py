# num = iter(range(1_000_000))
# while True:
#     try:
#         print(next(num))
#     except StopIteration:
#         break




# names = ["A", "B", "C"]
# scores = [90, 80, 85]
# for n, s in zip(names, scores):
#     print(n, s)




# class Counter : 
#   def __init__(self, start,end):
#     self.start = start
#     self.end = end
    
#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     if self.start > self.end:
#       raise StopIteration
#     num = self.start
#     self.start = self.start + 1
#     return num
  
# c = Counter(1,10)

# for i in c:
#   print(i)



import itertools
from itertools import islice
# for c in itertools.count(10,2):
#     if c > 20:
#         break
#     else:
#         print(c)
    
    
# for x in itertools.cycle([1, 2, 3]): 
#     print(x)


nums = range(100)
print(list(islice(nums, 5, 10)))