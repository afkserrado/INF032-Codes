'''
4.Entrar com vários números e informar quantos números entre 100 e 200 foram digitados. quando o valor 0 for digitado o programa deve encerrar.

OK
'''

numero = 1
cont = 0

while numero != 0:
    numero = int(input("Informe um numero (ou 0 para encerrar): "))
    
    if 100 <= numero <= 200:
        cont += 1

print(f"Foram digitados {cont} numeros entre 100 e 200.")