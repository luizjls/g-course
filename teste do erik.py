'''
list1 = []
list2 = list(range(5,20))
list3 = ['P','e','r','s','o','n','a','l','D','a','d']
list4 = list('Personal Dad')
list7 = ['99','55','48', '31', '95', '4', '70', '47', '59', '37']
list5 = ['99','55','48','23','43','54','91','16']
list6 = list5

list5.pop(7)
list6.pop(6)
list5.pop(4)

print(list5)
print(list6)

curse = "LearningXWithXPersonalXDad"
print(curse)
curse = curse.split('')
print(curse)


curse = ["O", "Erik", "acerta", "todas", "as", "formigas."]
abc = ' - '.join(curse)
print(abc)


list1 = ['P','e','r','s','o','n','a','l','D','a','d']
list2 = list('Personal Dad')

list3 = ['99','55','48', '31', '95', '4', '70', '47', '59', '37']
list3 = [99,55,48,31,95,4,70,47,59,37]

soma = '0'
for element in list3:
    print(element)
    soma = soma + element

print(soma)


car = []
product = ''

while product != 'exit':
    print("Enter with another product or write 'exit' ")
    product = input()
    if product != 'exit':
        car.append(product)

for product in car:
    print(product)


#            0      1       2        3        4
colors = ['blue', 'red', 'pink', 'purple', 'green']

#print(colors[-4])
#print(list(enumerate(colors)))

for a, b in enumerate(colors):
    #print('The indice is: ' + str(a) + ' and color is: ' + str(b))
    print(type(a))
    print(type(b))
    print(f'The indice is: {a}  and color is: {b}')


    listA = ['a']
listA.append('123')

count = 0
while count < 10:
   listA.append(count)
   count = count + 2

print(listA)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 83, 84, 84, 93]
print(numbers.index(84, 10, 11))

'''

# list (start:end:step)
# list (start:end)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[:4:-1])
