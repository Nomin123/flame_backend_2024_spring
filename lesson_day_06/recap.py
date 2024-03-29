print('recapture')




#line гэдэг үг хэд байгааг ол.
data=open('./data/test.txt')
count_line=0
for line in data:
    if line.find('line')==-1:
        count_line=count_line+1

    else:
        print(line.find('line'))
print(count_line)

#This гэдэг үг хэд баыгааг ол

#third гэдгээс хойшхыг хэвлэ
