'''
grade_erik = {'math':100, 'english':85, 'portuguese':95}
grade_erik['phisical'] = 98
grade_class = {'science': 70}
grade_erik.update(grade_class)
grade_erik.update({'math3':98})
grade_erik.pop('science')

print(grade_erik)
# print(type(grade_erik))


car = [{'nome':'PS5', 'quantidade':1, 'preco':3500}]
car2 = ({'nome':'PS5', 'quantidade':1, 'preco':3500}, {'nome':'cortina', 'quantidade':2, 'preco':100})

p1 = {'nome':'PS5', 'quantidade':1, 'preco':3500}
p2 = {'nome':'cortina', 'quantidade':2, 'preco':100, 'peso':165}
p3 = {'nome':'repelente', 'quantidade':10, 'preco':5}
p4 = {'nome':'arma com silenciador', 'quantidade':1, 'preco':7000}

car.append(p1)
car.append(p2)
car.append(p3)
car.append(p4)

# car = [p1, p2, p3, p4]

print(car[1].get('quantidade'))

# print(type(car))


students = {}
students = {'name':'Victor', 'altura':170, 'peso':52}
students = dict(name='Victor', altura=170, peso=50 )
students = {}.fromkeys(['name', 'altura', 'peso'], 'desconhecido')

print(students)
print(type(students))

#students = {}.fromkeys(<<ITERAVEL>>, <<VALOR>>)
students = {}.fromkeys(['name', 'altura', 'peso'], 'desconhecido')


print(students)
print(type(students))

value = 2.3
value = ['2', '.', '3']

print(value)
print(type(value))


# students = {}.fromkeys(<<ITERAVEL>>, <<VALOR>>)
# students = {}.fromkeys(['name', 'altura', 'peso'], 'desconhecido')
# students = {}.fromkeys('name', 'desconhecido')
# students = {}.fromkeys(range(4,7), [1,2,3])
students = {}.fromkeys([1,2,3], range(4,7))

print(students)
print(type(students))


allowance = {'jan': 35, 'fev': 40, 'mar': 58}



for key in allowance:
    print(f'0 {key} eu ganhei {allowance[key]}')

'''

list = []
tuple = ()
dict = {}
set = ({1, 2, 2, 6, 9, 4, 4, 5, 2})

print(set)
print(type(set))



