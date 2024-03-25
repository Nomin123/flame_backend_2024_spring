
odd_numbers=[1,3,5,7,9]
for index in range(len(odd_numbers)):
    odd_numbers[index]=odd_numbers[index]+1

numbers=[1,4,11,58,10,20]
print(numbers[0])
print(numbers[5])
for index in range(len(odd_numbers)):
    if numbers[index]%2==0:
        print('it is a even number')
    else:
        print('it is a odd number')
    
a=[3,4,5]
b=[7,8,9]
c=b+a
print(c)

c=[1]*4

t=['a','b','c','d','e','f']
print(t)
t[1:3]=['x','y']
print(t)

#element nemeh

t=['a','b','c']
print(t)
t.append('d')
print(t)

#2 listiig нэмэх

t1=['a','b']
t2=['c','d']
t1.extend(t2)
print(t1)

a1=['e','f']
a1.append(['b','c'])
print(a1)

#2D list

matrix=[
    ['x','o','o'],
    ['-','x','-'],
    ['-','-','-']
]
print(matrix)

#устгах
#POP operation хамгийн сүүлийн элэментийг нь устгадаг

data=[1,3,4,5]
print(data)
data.pop()
print(data)

#del operation

del data[0]
print(data)

#remove operation

t=['a','b','c']
print(t)
t.remove('a')
print(t)

#del and slice

t=[1,4,6,7,7]
del t[1:-2]
print(t)

#List and functions

nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(int(sum(nums)/len(nums)))

#String list  functions

s='spam'
t=list(s)
print(t)

s='pining, for the fjords'
delimiter='='
t=s.split(delimiter)
print(t)