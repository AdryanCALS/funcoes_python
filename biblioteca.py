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
    print(f"O valor total de {nome_p} no estoque é: {valor_total}")