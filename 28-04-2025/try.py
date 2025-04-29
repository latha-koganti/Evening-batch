try:
    n = int(input('Enter number : '))
except Exception as e:
    print(f'Error: {e}')
else:
    print(n)
finally:
    #no matter what happens this will execute
    print('Bye')
