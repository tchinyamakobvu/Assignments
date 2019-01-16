#Reads name.txt

with open('name.txt') as f:
    my_name = f.read()
    greeting = 'Hello my name is ' + my_name + '.'



print(greeting)
#write that to a file
with open('Hello.txt',"w") as g:
	g.write(greeting)