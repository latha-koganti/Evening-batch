#write a program to switch values
#stored in variables a &b
a = 10
b = 20
c = 50

print('Before')
print(f'a is {a}')
print(f'b is {b}')
print(f'c is {c}')

a,b,c = c,a,b

#c = a
#a = b
#b = c

print('After')
print(f'a is {a}')
print(f'b is {b}')
print(f'c is {c}')

