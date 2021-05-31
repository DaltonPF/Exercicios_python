m1_linhas = int(input("Quantas linha na primeira matriz: "))

m1_colunas = int(input("quantas colunas na primeira matriz: "))

m1 = []

for m1_linha in range(m1_linhas):
    m1.append([])
    for m1_coluna in range(m1_colunas):
        num = int(input(f"digite um numero para a linha {m1_linha+1} e a coluna {m1_coluna+1} da primeira matriz: "))
        m1[m1_linha].append(num)


m2_linhas = int(input("Quantas linha na segunda matriz: "))

m2_colunas = int(input("quantas colunas na segunda matriz: "))

m2 = []

for m2_linha in range(m2_linhas):
    m2.append([])
    for m2_coluna in range(m2_colunas):
        num = int(input(f"digite um numero para a linha {m2_linha+1} e a coluna {m2_coluna+1} da segunda matriz: "))
        m2[m2_linha].append(num)


print(m1)

print(m2)

x = 0

if m1_linhas == m2_linhas and m1_colunas == m2_colunas:
    soma =[]
    for linha_soma in range(m1_linhas):
        soma.append([])
        for coluna_soma in range(m2_colunas):
            soma[linha_soma].append(m1[linha_soma][coluna_soma] + m2[linha_soma][coluna_soma])
            
    print(f"A soma das matrizes se resulta na matriz : {soma}")
else:
    print("Não é possivel realizar a soma entre essas matrizes")

