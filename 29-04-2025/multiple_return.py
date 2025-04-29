def displayName(f_name,l_name):
    if f_name == '' or l_name == '':
        return 'First and last name is manidatory'
    return f'{f_name}.{l_name}'

#print(displayName('Quamarunnisa',''))
#print(displayName('XYZ','abc'))
#print(displayName('',''))
print(displayName('latha',''))
