#multiple parameters
def greetwithNC(name,city):
    print(f'Hello {name}')
    print(f'How is the weather in {city}')

#positional parameters
#greetwithNC('quma','Hyderabad')

#greetwithNC('Hyderabad','latha')
#keyword parameters
#greetwithNC(city='Hyderabad',name='latha')

n = input('Enter name: ')
c = input('Enter your City: ')
#greetwithNC(c,n)
greetwithNC(city=c,name=n)
