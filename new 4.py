import os
arq1 = open("arquivo1.txt", "w", encoding = "utf8")
arq1.write("Python é uma linguagem poderosa!")
arq1.close()
arq1 = open("arquivo1.txt", "r", encoding = "utf8")
print(arq1.read())
print(arq1.tell())
print(arq1.seek(0,0))
print(arq1.read(10))
arq2 = open("arquivo1.txt", "w", encoding = "utf8")
arq2.write("Testando gravação de arquivos em Python ")
arq2.close()
arq2 = open("arquivo1.txt", "r", encoding='utf8')
print(arq2.read())
arq3 = open("arquivo1.txt", "a", encoding = "utf8")
arq3.write(" Acrescentando conteúdo")
arq3.close()
arq3 = open("arquivo1.txt", "r", encoding = "utf8")
print(arq3.read())

'''
arq4 = input("nome: ")
arq4 = arq4 + ".txt"
print(arq4)
arq5 = open("%s" % arq4, "a", encoding = "utf8")
texto = input("texto: ")
arq5.write(" %s" % texto)
arq5.close()
arq5 = open("%s" % arq4, "r", encoding = "utf8")
print(arq5.read())
print("\n")
print("Texto inserido!")
'''


f = open("Pasta1.csv", "r")
data = f.read()
print(data)
rows = data.split('\n')
full_data = []
print(rows)
print("\n")


for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
#print(full_data)

count = 0
nada = ['']
print(full_data[0])
for row in full_data[1:]:
    if row != nada:
        print(", ".join(row))
        #print(row)
        count += 1

print("%i linhas" % count)

data2 = full_data[0]
print("%i colunas" % len(data2))


