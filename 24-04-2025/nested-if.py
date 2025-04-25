age = 50
has_license = False

if age>=18:
#   50>18 - True
    if has_license:
        # False
        print('You can drive')
    else:
        print('You are eligible to drive , but need license')
else:
    print('You are not eligible')
    
