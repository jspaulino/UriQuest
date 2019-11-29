# -*- coding: utf-8 -*-

'''
Faça um programa que leia três valores e apresente 
o maior dos três valores lidos seguido da mensagem 
“eh o maior”. Utilize a fórmula:

maiorAB = (a+b+abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois 
primeiros (a e b). Um segundo passo, portanto é necessário 
para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

#recebe e separa os valores
s = input()
a,b,c = s.split(" ")

#converte
a= int(a)
b= int(b)
c= int(c)

#usa a fórmula duas vezes pra decidir qual o maior dos 3 números
maiorAB = (a+b+abs(a-b))/2
maiorAB = (c+maiorAB+abs(c-maiorAB))/2

#converte para inteiro pra pôr na saída(exigido)
maiorAB = int(maiorAB)

print(maiorAB,"eh o maior")