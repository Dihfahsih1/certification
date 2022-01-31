#decision making
def decision(x):
  if x == True:
    print('It is raining')
  else:
    print('continue playing football')
    
y=input("please enter the value: \n")
decision (y)

#dictionaries
my_dict = {'Namono':33, 'Dihfahsih': 31, 'Dickson': 29, 'Denis':27}
get_keys = my_dict.keys()
print("Names: ", str(get_keys) + "/n")

get_values = my_dict.values()
print("Ages: ", str(get_values) + "/n")


#using while loop
i=1
n=2 
while i <= 10:
  print(n, "*" ,i, "=", i*n)
  i=i+1
  
#for loop

li = ['chair','stool','timber']
l2 = ['yellow','green','red']

for i in li:
  for j in l2:
    print(i, j)


#lambda function
li = [1,2,3,4,5,6,7]
d=list(filter(lambda x:(x%2 !=0), li))
print(d)

from functools import reduce
de = reduce(lambda x,y:y+x, li)
print(de)