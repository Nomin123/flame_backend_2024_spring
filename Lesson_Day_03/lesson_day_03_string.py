fruit='banana'
index=0

while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1
print('FOR loops')
for char in fruit:
    print(char)

word='banana'
index=word.find('a')
print(index)
print(word.find('na'))

data='From stephen.marquard@ucd.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)

camels=42
print(f'{camels}')


