var = 7
print(var)
var

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
#print(mylist[0]) # prints 1
#print(mylist[1]) # prints 2
#print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
    
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# captar o segundo campo da lista names para a variável second_name
second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("A lista de nomes é: " + ", ".join(names))
print("Exemplo2: %s" % names)
print("O segundo nome na lista NAMES é: %s" % second_name)

for x in names:
    print(x)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

#print(", ".join(repr(e) for e in x_list))
for x in x_list:
    print(x)
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))


# testing code
if x_list.count(x) < 10 and y_list.count(y) < 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
    
data = ("John", "Doe", 53.44)
format_string = "Hello"
format_string2 = "Hello %s %s. Your current balance is $%s."
print(format_string + " %s" % data[0] + " %s" % data[1] + ". Your current balance is $%s." % data[2])
print(format_string2 % data)

# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
    
print("acabou aqui")
    
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
    
    
def my_function():
    print("Hello From My Function!")
    
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b
    
my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)
print(x)


# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
    
def teste():
    print("teste")

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
teste()