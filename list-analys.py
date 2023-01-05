# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort()
# print('Sorted list:', vowels)
# vowels.sort(reverse=True)
# print('Sorted list (in Descending):', vowels)
# đảo ngược danh sách: a = [1,2,3,4]
#cách 1: 
#a[::-1]
# cách 2: 
# a.reverse()
my_list=[8.5,5.6,6.7,7.8,8.4,4.9,9.0,0.5,-1.2,-8.9]
a=float(input())
b=float(input())
min_value = min(my_list)
max_value = max(my_list)
if (min_value>=a and max_value<=b) or (min_value>=b and max_value<=a) :
  print('All elements in list belong to ['+str(a)+','+str(b)+']')
elif min_value>a and min_value>b or max_value<b and max_value <a:
  print('All elements in list do not belong to ['+str(a)+','+str(b)+']')
else:
  c=0
  if (a<my_list[0] and my_list[0]>b) or (b>my_list[0] and my_list[0]<a):
    c+=1
  if (a<my_list[1] and my_list[1]>b) or (b>my_list[1] and my_list[1]<a):
    c+=1
  if (a<my_list[2] and my_list[2]>b) or (b>my_list[2] and my_list[2]<a):
    c+=1
  if (a<my_list[3] and my_list[3]>b) or (b>my_list[3] and my_list[3]<a):
    c+=1
  if (a<my_list[4] and my_list[4]>b) or (b>my_list[4] and my_list[4]<a):
    c+=1
  if (a<my_list[5] and my_list[5]>b) or (b>my_list[5] and my_list[5]<a):
    c+=1
  if (a<my_list[6] and my_list[6]>b) or (b>my_list[6] and my_list[6]<a):
    c+=1
  if (a<my_list[7] and my_list[7]>b) or (b>my_list[7] and my_list[7]<a):
    c+=1
  if (a<my_list[8] and my_list[8]>b) or (b>my_list[8] and my_list[8]<a):
    c+=1
  if (a<my_list[9] and my_list[9]>b) or (b>my_list[9] and my_list[9]<a):
    c+=1
  if c ==10:
    print('All elements in list do not belong to ['+str(a)+','+str(b)+']')
  else:
    print('Some elements in list belong to ['+str(a)+','+str(b)+']')

my_list=[8.5,5.6,6.7,7.8,8.4,4.9,9.0,0.5,-1.2,-8.9]
a=float(input())
b=float(input())
min_value = min(my_list)
max_value = max(my_list)
if (min_value>=a and max_value<=b) or (min_value>=b and max_value<=a) :
  print(f'All elements in list belong to [{a},{b}]')
elif min_value>a and min_value>b or max_value<b and max_value <a:
  print(f'All elements in list do not belong to [{a},{b}]')
else:
  c=0
  if (a<my_list[0] and my_list[0]>b) or (b>my_list[0] and my_list[0]<a):
    c+=1
  if (a<my_list[1] and my_list[1]>b) or (b>my_list[1] and my_list[1]<a):
    c+=1
  if (a<my_list[2] and my_list[2]>b) or (b>my_list[2] and my_list[2]<a):
    c+=1
  if (a<my_list[3] and my_list[3]>b) or (b>my_list[3] and my_list[3]<a):
    c+=1
  if (a<my_list[4] and my_list[4]>b) or (b>my_list[4] and my_list[4]<a):
    c+=1
  if (a<my_list[5] and my_list[5]>b) or (b>my_list[5] and my_list[5]<a):
    c+=1
  if (a<my_list[6] and my_list[6]>b) or (b>my_list[6] and my_list[6]<a):
    c+=1
  if (a<my_list[7] and my_list[7]>b) or (b>my_list[7] and my_list[7]<a):
    c+=1
  if (a<my_list[8] and my_list[8]>b) or (b>my_list[8] and my_list[8]<a):
    c+=1
  if (a<my_list[9] and my_list[9]>b) or (b>my_list[9] and my_list[9]<a):
    c+=1
  if c ==10:
    print(f'All elements in list do not belong to [{a},{b}]')
  else:
    print(f'Some elements in list belong to ['+str(a)+','+str(b)+']')
   

 