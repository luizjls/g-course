
'''
>> 1
qtd = int(input('Quantas vezes este loop deve rodar?'))
soma = 0

for n in range (1, qtd + 1):
    num = input(f'informe o valor {n}/{qtd}: ')
    soma += n

print(f'O valor da soma eh {soma}')

>> 2
nome = "Erik Martins Silva"

for letter in nome:
    print(letter)  # print(letter, end='\n')

>> 3
See link https://apps.timwhitlock.info/emoji/tables/unicode


'''
for x in range(3):
    for x in range(3):
        for n in range(1, 11):
            print('\U0001F61B' * n)

