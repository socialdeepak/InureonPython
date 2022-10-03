""" from re import L


print("Hello")
l = [1,2,3,4,"deepak","asdf"]
for i in l:
    if(type(i)== str):  
        print(type(i))
        charl =[]
        for j in i:
            charl.append(j);
        print(charl)

for i,j in enumerate(l):
    print(i,j)
for i in l:
    if(type(i)== int):  
        print(i**2)
 """
# city = input()
# length = len(city)
# res = 1
# print(city[::-1])
# if(city == city[::-1]):
#     print(city ,"is palendom")
# else:
#     print(city ,"is not palendom")

""" for i,j in enumerate(city):eye
    if( j== city[length -1]):
        length = length -1
    else:
        res = 0
        break
  

print(res)
 """

# country = {"India":"IN",
#             "China":"CH",
#             "Canada":"CA",
#             "United States":"US"}

# print(country)
# filter = []
# for item in country:
#     print(len(item))
#     if(len(item) < 6):
#         filter.append(item)

# print(filter)

dict_1 = {
    'KEY1':{'a':14, 'b':12,'c':10},
    'KEY2':{'a':141, 'b':121,'c':101},
    }

print(dict_1)
biggest = 0
for i in dict_1:
    biggest = 0
    for j in dict_1[i]:
        if  dict_1[i][j] >= int(biggest):
            biggest = dict_1[i][j]
    print(biggest)


for i in dict_1.values():
    lst =[]
    for j in i.values():
        lst.append(j)
    print(max(lst))
