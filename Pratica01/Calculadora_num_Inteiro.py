# 5- Calculadora de Número Inteiro
# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
# Entrada: O arquivo de entrada contém 4 valores inteiros. 
# Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

# Digite o valor de A, B,C e D e converte para inteiro
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))


# Calcula a diferença entre o produto de A*B e o produto de C*D
DIFERENCA = (A*B - C*D)

# Exibe o resultado com a palavra "DIFERENCA" em letras maiúsculas, conforme exigido
print("DIFERENCA = {}".format(DIFERENCA))