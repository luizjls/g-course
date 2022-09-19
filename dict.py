'''
grade_erik = {'math':100, 'english':85, 'portuguese':95}
grade_erik['phisical'] = 98
grade_class = {'science': 70}
grade_erik.update(grade_class)
grade_erik.update({'math3':98})
grade_erik.pop('science')

print(grade_erik)
# print(type(grade_erik))

'''

car = []

p1 = {'nome':'PS5', 'quantidade':1, 'preco':3500}
p2 = {'nome':'cortina', 'quantidade':2, 'preco':100}
p3 = {'nome':'repelente', 'quantidade':10, 'preco':5}
p4 = {'nome':'arma com silenciador', 'quantidade':1, 'preco':7000}

car.append(p1)
car.append(p2)
car.append(p3)
car.append(p4)

# car = [p1, p2, p3, p4]

print(car[1].get('quantidade'))

# print(type(car))


