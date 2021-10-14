print('Example for positional only argument')
def fun(a,b,c):
    print(a,b,c)
fun(200,300,100)
print('****************************************************')
print('Example for keyword only argument')
def fun(a,b,c):
    print(a,b,c)
fun(a=200,c=300,b=100)
print('****************************************************')
def fun(a,b,/,c):
    print(a,b,c)
fun(200,100,c=300)
print('****************************************************')
def fun(a,b,/,c):
    print(a,b,c)
fun(200,100,400)
print('****************************************************')
def fun(a,b,/,c,*,d):
    print(a,b,c,d)
fun(200,100,400,d=300)
print('****************************************************')
def fun(a,b,/,c,*,d):
    print(a,b,c,d)
fun(200,100,c=300,d=400)
print('****************************************************')
