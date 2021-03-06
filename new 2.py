#abrir o arquivo com as respostas na variável "f"
f = open("Pasta4.csv", "r", encoding = "utf8")
#criar uma variável "data" para receber a leitura dos dados
data = f.read()
#criar uma variável para receber os dados splitados por quebra de linhas
rows = data.split('\n')
#abrir o arquivo com o gabarito na variável "g"
g = open("Pasta3.csv", "r", encoding = "utf8")
#criar uma variável "datas" para receber a leitura dos dados
datas = g.read()
#criar uma lista para receber os dados splitados por vírgula
linhas = datas.split(',')

#criar uma lista para receber os dados splitados por vírgula
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

#cria a variável count para contar quantas linhas existem no arquivo
count = 0
nada = ['']
for row in full_data:
    if row != nada:
        count += 1
        
#cria uma variável para indicar a posição da linha que o script irá rodar
aluno = 0

#cria um loop while enquanto o número de alunos for menor que a quantidade de linhas, irá executar o script
while aluno < count:

    #criar uma variável para receber os dados excluindo a possibilidade de iniciar a linha com aspas duplas
    lista1 = []
    for i in full_data[aluno]:
        lista1.append(i.strip('""'))
        
        
    #cirar uma variável para receber apenas as letras das respostas
    lista2 = []
    for i in lista1:
        if i[:2] == "a)" or i[:2] == "b)" or i[:2] == "c)" or i[:2] == "d)" or i[:2] == "e)" :
            lista2.append(i[:1])

    #criar uma lista para receber os dados do gabarito
    respostas = []
    for i in linhas:
        respostas.append(i)

    lst = 0
    res = 0
    teste = []

    for i in lista2:
        if lista2[lst] == respostas[res]:
            teste.append("certo")
        else:
            teste.append("errado")
        lst += 1
        res += 1

    x = teste.count("certo")

    y = round(x * 0.104,3)

    print("ALUNO: %s \nNOTA: %s" % (lista1[3], y))
    
    aluno += 1
