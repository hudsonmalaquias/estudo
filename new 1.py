
#criação de uma classe
class carro:
    nome = ""
    tipo = ""
    cor = ""
    valor = ""
    
    #criação de uma função para captar os campos da classe 
    def descricao(self):
        desc_str = "%s é um tipo de %s, de cor %s e custa $%.2f dólares." % (self.nome, self.tipo, self.cor, self.valor)
        return desc_str

#inserção de informações nos campos das classes
carro1 = carro()
carro1.nome = "Ferrari"
carro1.tipo = "conversível"
carro1.cor = "vermelho"
carro1.valor = 60000.00

#imprimir a função com a descrição
print(carro1.descricao())

#criação de uma lista de dados
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)

# prints out 1,2,3
for x in mylist:
    print(x)

#criação de uma lista com campos determinados
names = ["John", "Eric", "Jessica"]

# captar o segundo campo da lista names para a variável second_name
second_name = names[1]

#imprime a lista de nomes utilizando o .join(names) 
print("A lista de nomes é: " + ", ".join(names))
#imprime a lista de nomes utilizando o %s names (sendo a captura dos dados da lista para uma string) 
print("Lista de nomes: %s" % names)
#imprime o segundo nome da lista pela captura da variável second_name
print("O segundo nome na lista NAMES é: %s" % second_name)

#criação de um dicionário, parecida com arrays 
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#outra forma para a criação de um dicionário
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#interação com os dicionários
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("O número de telefone do %s é %d" % (name, number))

#remoção de itens de um dicionário
del phonebook["John"]
print(phonebook)

#outra forma para excluir itens de um dicionário
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

#adicionando um ítem no dicionário
phonebook["Jake"] = 938273443
del phonebook["Jill"]

#interação com dicionário usando IF
if "Jake" in phonebook:  
    print("Jake está listado na lista de telefone.")
    
if "Jill" not in phonebook:      
    print("Jill não está listado na lista de telefone.")  

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

listadomercado = ["ovos", "farinha", "leite", "maças"]

print(listadomercado)

if "carne" not in listadomercado:
    listadomercado.append("carne")
    
if "carne" not in listadomercado:
    listadomercado.append("carne")
    
print(listadomercado)

#comando para captar entradas pelo usuário "str(input("Qual seu nome? \n"))"
a = "Hudson de Souza Rocha Malaquias"
print(a)
c = a.count(" ")
b = len(a) - c

print("O nome acima contém %s letras" % b)

if (b > 25):
    print("nome grande")
else:
    print("nome pequeno")

bota = []
celsius = [39.2, 36.5, 37.3, 37.8]
def chute():
    for i in celsius: 
        bota.append((i * 9/5) + 32)
chute()
print(bota)

bota2 = map(lambda x: (float(x) * 9/5) + 32, celsius)
print(list(bota2))

e = 'as'

if not e.isdigit():
    print("bleu")


numeros = 0
lista1 = []
while numeros <= 3:
    j = numeros + 1
    i = input("Insira o %iº número: " % j)
    lista1.append(i)
    numeros += 1

numeros = len(lista1)

notas = float(0)
for i in lista1:
    j = float(i)
    notas = float(notas + j)
nota_final = float(notas)
media = round(nota_final/numeros, 2)

print("A média é: %s" % media)

i = input("Quantos metros? ")
metros = float(i)
centimetros = 100
resultado = metros * centimetros
print("%s centímetros" % resultado)

i = input("Raio do círculo: ")
raio = float(i)
raio_q = raio * raio
resultado = round(3.1415926535898 * raio_q,3)
print("A área do círculo é de %s metros" % resultado)

i = input("Lado do quadrado: ")
lado = float(i)
resultado = lado * lado
dobro = resultado * 2
print("A área do quadrado é de %s metros e o dobro da área é %s metros" % (resultado,dobro))

s = input("Quanto recebe por hora: ")
salario = float(s)
h = input("Número de horas trabalhadas no mês: ")
horas = float(h)
resultado = salario * horas
print("Seu salário é de R$%s reais." % resultado) 

