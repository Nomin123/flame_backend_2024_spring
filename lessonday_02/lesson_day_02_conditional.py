#dasgal 1
x=10
y=7
if(x>y):
    print('x is bigger than y')
elif (x<y):
    print("y is bigger than x")
else:
    print("y is equal to x")

try:
    x=int(input('Give me number\n'))
    print(x+5)
except:
    print('Please, Give me number')
                
    