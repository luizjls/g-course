'''
dic = {'idade': 16}
print(dic)
print(dic.get('idade'))
print(dic.get('name'))

print(dic['idade'])
print(dic['name'])

from collections import defaultdict

defdic = defaultdict(lambda : 8)
defdic['name'] = 'Victor'
defdic['idade'] = '14'

print(defdic)
print(defdic['note'])
print(defdic)



'''
from typing import OrderedDict
dict = OrderedDict({'b': 11,'a': 9,'e': 1,'d': 7,'c': 5,})

#print(dict.get('11'))


print(dir(()))



