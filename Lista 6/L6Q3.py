'''
3.Entrar com vários números positivos e imprimir a media dos números digitados. o programa acaba quando se informar que não deseja mais continuar.

OK
'''

numero = 1
cont = 0
soma = 0

while numero > 0:
    numero = int(input("Informe um numero positivo para continuar ou um negativo para parar: "))
    
    if numero <= 0:
        break

    soma = soma + numero
    cont = cont + 1

if cont > 0:
    media = soma / cont
    print(f"A media e: {media}")
else:
    print(f"Não e possível calcular a media, pois nenhum numero positivo foi digitado.")