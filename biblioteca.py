def triangulo(numero):
    for i in range(numero+1):
        for j in range(i):
            print(i, end= " ")
        print()

def vogais(texto):
    contador = 0
    vogais = "aeiouAEIOU"
    for i in range(len(texto)):
        if  texto[i] in vogais:
            contador +=1
    print(contador)

def estoque(nome_p, qtd_p, valor_p):
    valor_total =  qtd_p * valor_p
    return valor_total

def verificar_num(num):
    resposta = "Z"
    if num > 0:
        resposta = "P"
    elif num < 0:
        resposta = "N"
    return resposta

def soma(*num):
    soma =0
    for i in range(len(num)):
        soma += num[i]
    print(soma)