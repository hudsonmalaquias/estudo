
full_data = []
lista1 = []
lista2 = []
respostas = []
certo = []

def teste1(jeremias):

    #abrir o arquivo com as respostas na variável "f"
    f = open("Pasta2.csv", "r", encoding = "utf8")
    #criar uma variável "data" para receber a leitura dos dados
    data = f.read()
    #criar uma variável para receber os dados splitados por quebra de linhas
    rows = data.split('\n')

    #criar uma lista para receber os dados splitados por vírgula
    #full_data = []
    for row in rows:
        split_row = row.split(',')
        full_data.append(split_row)

    #criar uma variável para receber os dados excluindo a possibilidade de iniciar a linha com aspas duplas
    #lista1 = []
    for i in full_data[jeremias]:
        lista1.append(i.strip('""'))
        
        
    #cirar uma variável para receber apenas as letras das respostas
    #lista2 = []
    for i in lista1:
        if i[:2] == "a)" or i[:2] == "b)" or i[:2] == "c)" or i[:2] == "d)" or i[:2] == "e)" :
            lista2.append(i[:1])
    print(lista2)

def teste2():
    #abrir o arquivo com o gabarito na variável "g"
    g = open("Pasta3.csv", "r", encoding = "utf8")

    #criar uma variável "datas" para receber a leitura dos dados
    datas = g.read()

    #criar uma lista para receber os dados splitados por vírgula
    linhas = datas.split(',')

    #criar uma lista para receber os dados do gabarito
    #respostas = []
    for i in linhas:
        respostas.append(i[:1])
    print(respostas)

  
teste1(0)
teste2()