
'''

num = 20

while num < 30:
    print(num)
    num = num + 1

# 2
answer_challenge = 12 * 3 * 5
answer = 0

while answer != answer_challenge:
    answer = int(input("Qual o valor da resposta?"))
    if(answer  != answer_challenge):
        print('Error')
    else:
        print('OK')


# 3

for n in range(1, 20):
    if(n < 18):
        print(n)
    else:
        print('>> quebrou')
        break

print('O Erik saiu do looping')


#4

while True:
    command = input('Digite algodao doce para sair.')
    if command == 'algodao doce':
        break

'''







