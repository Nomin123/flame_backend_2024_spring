print('recapture')
#Lists
a=[1,2,3,4,5]

print(a)

index=0
while True:
    if index<len(a):
        print(a[index])
    else:
        break
    index=index+1

# for loop
for element in a:
    print(element)
    
# while loop another way
    index=0
while index<len(a):
    print(a[index])
    index=index+1

a[2]=10

print(a)
 
#calculateLength  гэдэг list_г паратетрээр нь авдаг функц

b=[1,3,4,5,6,7]
c=[4,5,6]
e=['hi','hey','hallo','hello']

def calculateLength(l):
    return len(l)
print(calculateLength(b))
print(calculateLength(c))
print(calculateLength(e))

