string = str(input("Enter the string:--  "))
remove = str(input('Which character you want to remove:--  '))
result=string.find(remove)
# print(result)

if(result>0):
    str1=string.replace(remove,'',5)
else:
    str1="Character/string not found"

print(str1)