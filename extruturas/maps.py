
#def five(x): return 5
#print(list(map(five, [1,2,3])))
from operator import add

m = map(lambda x:x**2, [1,2,3,8,9])

m = map(add,[1,2,3,8,9],[1,2,3,8,9])

m = map(lambda x,y:x+y,[1,2,3,8,9],[1,2,3,8,9])

m = map(lambda x,y,z:x+y-z,[1,2,3,8,9],[1,2,3,8,9],[1,2,3,8,9])

print(list(m))