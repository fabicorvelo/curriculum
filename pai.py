

print('Digite o primeiro número:')
x = input()

print('Digite o segundo número: ')
y = input()

resultado = int(x) + int(y) 
print(resultado)

print('O resultado da soma de ' + x + '+' + y + ' é igual a ' + str(resultado))

if resultado > 10:
    print("O resultado da soma é maior que 10")
else:
    print("O resultado da soma é menor que 10")

    