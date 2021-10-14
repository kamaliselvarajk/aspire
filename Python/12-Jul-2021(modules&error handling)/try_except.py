while True:
    try:
        x = int(input('Enter a number: '))
        print('Thank you for your input')
        break
    except ValueError:
        print('Please enter the numeric value')
print('***********************************************************')
while True:
    try:
        x = int(input('Enter a number: '))
        print('Thank you for your input')
        break
    except(ValueError, TypeError, NameError):
        print('Please enter the valid input')

        
    print('Hi Kamali')
print('***********************************************************')
def fun():
    try:
        return True
    finally:
        return False  
fun()
print('***********************************************************')
while True:
    try:
        x = int(input('Enter a number: '))
        print('Thank you for your input')
        print(y)
        break
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    except NameError:
        print('NameError')
    finally:
        print('Finally part executed')

    print('Hi Kamali')
        
