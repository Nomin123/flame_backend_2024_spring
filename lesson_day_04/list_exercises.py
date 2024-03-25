#Exercise 01

def sum():
    print(4+5)

sum()

def add(a,b,c):
    return a+b+c

print(add(13,4,6))



def chop(l):
     del l[0]
     del l[-1]
     return None
     


def middle(l):
    t = l[1:-1]
    return t

numbers=[12,4,6,4,7,5]
print(chop(numbers))
numbers=[12,4,6,4,7,5]
print(middle(numbers))

#Exercise 4


new_list = []

while True:
    inp=input('Enter a number:')

    if inp=='done':
        break
    # try хэсгийг бичнэ
    try:    
# inp -ийг int тоо болгож хувирга тэгээд нэг хувьсагчид хадгал
        nums=int(inp)
# new_list дээр энэ тоон хувьсагчаа нэм append ашиглаж болно
        new_list.append(nums)
# except хэсгийг бичнэ


    except:
        print('Error!')


# Шинэ листээсээ хамгийн их болон багыг олж хэвлэ
print(max(new_list))
print(min(new_list))

print(new_list)



