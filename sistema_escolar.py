# -*- coding: utf-8 -*-
"""Avaliação TCT do Hall CapacitaTI da Globalhitss.


#Escreva um código em Python para criar o Sistema Escolar:

## 1. Criar uma função para exibir um cabeçalho padrão. Que deverá ser apresentado em todo o momento da execução do código.

## 2. Solicitar a inserção dos seguintes dados: 5 nomes de alunos e 3 notas para cada aluno, armazenando em variáveis compostas. Utilizar estrutura de repetição.

## 3. Tendo a média para aprovação no valor de 7,0 pontos e sabendo que entre 5,0 pontos e menor que 7,0 pontos os alunos irão para a prova final e abaixo de 5,0 pontos serão reprovados, exibir a mensagem informando os nomes dos alunos com suas respectivas médias e resultados (aprovado, reprovado ou prova final). O cálculo da média e o resultado final deverão ser feito por funções.
"""

#Função para exibir cabeçalho padrão
def exibirCabecalho():
  if os.name == 'nt':
    os.system('cls') #para limpar tela em Windows
  else:
    os.system('clear') #para limpar tela em Linux
  print("")
  print("=" * 70)
  print("=" * 21, "Sistema de notas de alunos".upper(), "=" * 21)
  print("=" * 70)
  print("")

#Função para solicitar nome de cada aluno e suas respectivas 3 notas
def solicitarNomeNota():
  for i in range(5):
    exibirCabecalho()
    lista.append(input(f"Informe o nome do {i+1}º aluno(a): "))
    for j in range(3):
      lista.append(float(input(f"Informe a {j+1}ª nota de {lista[i*5]}: ")))
    calcularMedia()

#Função para calcular média das 3 notas (usado o tamanho da lista para
# auxiliar na procura da posição das 3 últimas notas mencionadas do
# respectivo aluno) e criando uma última posição para armazenar a média.
def calcularMedia():
  lista.append( (float(lista[len(lista)-3]) + float(lista[len(lista)-2]) + float(lista[len(lista)-1])) / 3 )
  return lista[len(lista)-1]

#Função para definir a situação de cada aluno com base na média
def definirSituacao(media):
  if media >= 7:
    return "APROVADO"
  elif media >= 5:
    return "PROVA FINAL"
  else:
    return "REPROVADO"

#Função para exibir o resultado final de cada aluno
def exibirResultado():
  exibirCabecalho()
  for i in range(0, 24, 5):
    print(f"Aluno(a) {lista[i]}, média {lista[i+4]}, {definirSituacao(lista[i+4])}.")
  print("")


import os

#Criando uma lista para armazenar o nome, as três notas e a média, respectivamente, de cada aluno.
lista = []

solicitarNomeNota()
exibirResultado()
