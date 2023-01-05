# num = int(input("Number of rows: "))

# for i in range(num): # lặp qua từng hàng
#   for j in range(num - i): #
#     print(end = " ")
#   for j in range(i+1):
#     print("*", end=" ")
#   print()
# print('* '*(num+1))

# for i in range(num,0,-1): # lặp qua từng hàng
#   for j in range(num - i+1,0,-1): #
#     print(end = " ")
#   for j in range(i):
#     print("*", end=" ")
#   print()

# game treo cổ: 
# print("Start the game...")
# word = "secret"
# guesses = ''
# turns = 10
# while turns > 0:        
#   failed = 0            
#   for char in word:     
#     if char in guesses:   
#       print(char)
#     else:
#       print("_")
#       failed += 1   
#   if failed == 0:       
#     print("You won")
#     break             
#   guess = input("Guess a character: ")
#   guesses += guess                   
#   if guess not in word: 
#     turns -= 1
#     print("Wrong guess!")
#     print("You have", + turns, "more guesses")
#     if turns == 0:          
#         print("You Lose")

# rowLen = int(input())
# colLen = int(input())

# matran = [0]*rowLen
# for i in range(rowLen):
#   matran[i]=[0]*colLen
# print (matran)

# size = int(input())
# i=size
# while i>0:
#   j=i
#   k=size - i
#   while k >0:
#     print(end=' ')
#     k-=1
#   while j >0:
#     print('*',end=' ')
#     j-=1
#   print()
#   i-=1
# m = 0
# while m<size:
#   j=0
#   k = 1
#   while k <size-m:
#     print(end=' ')
#     k+=1
#   while j <m+1:
#     print('*',end=' ')
#     j+=1
#   print()
#   m+=1


# for i in range(num): # lặp qua từng hàng
#   for j in range(num - i): #
#     print(end = " ")
#   for j in range(i+1):
#     print("*", end=" ")
#   print()

# arr = []
# while True:
#   a = int(input())
#   if a <0:
#     break
#   elif a%2==0:
#     arr.append(a)
  
# print(arr)

# def test(c,a=2):
#   'dfdf'
#   b = a+c
#   print(b)

# test(1)
# print(test.__doc__)
# a = ["A", 3, "A"]
# try:
#     # Replace first occurrence of A with B
#     a[a.index("A")] = "B"
# except ValueError:
#     pass
# print(a)
# new_item = 'whatever'
# hand = ["A", 3, "A"]
# hand = [new_item if x == 'A' else x for x in hand]

# x=[1.2,2.3,3.4,4.5,5.6,6.7,7.8,8.9]
# y=[9.8,8.7,7.6,8.5,5.4,4.3,3.2,2.1]
# def manhattan (x,y):
#   sum = 0
#   for i in range(len(x)):
#     sum += abs(x[i]-y[i])
#   return sum
  
# print (manhattan(x,y))

# def verify_email (email):
#   email_reverse = email[::-1]
#   if ord(email[0])>122 or ord(email[0])<65 or 91<=ord(email[0])<=96:
#     return False
#   elif email[-1]=='.':
#     return False
#   elif email_reverse.index('.')> email_reverse.index('@'):
#     return False
#   else:
#     dem_a =0
#     dem_dot = 0 
#     for i in range(len(email)):
#       if email[i] == '.' and email[i-1] =='@' or email[i] == '@' and email[i-1] =='.' or email[i] == '.' and email[i-1] =='.':
#         return False
#       if email[i] =='@':
#         dem_a+=1
#       elif email[i] == '.':
#         dem_dot+=1
#     if dem_a == 1 and dem_dot >0:
#       return True
#   return False

# email=input()
# if verify_email(email)==True:
#     print('Valid')
# else:
#     print('Invalid')

# def sqrt (num):
#   if num ==0:
#     return True
#   for i in range(1,num+1):
#     if num/i == i:
#       return True
#   return False

# def square_number (n):
#   arr = []
#   for i in range(n+1):
#     if sqrt(i) == True:
#       arr.append(i)
#   return arr
  
# num = int(input())
# print(square_number(num))
# def vi_du():
#     a = 100

#     def vi_du2():
#         global a
#         a=1
    
#     print("Giá trị của biến a là:", a)
#     vi_du2()
#     print("Giá trị của biến a sau khi gọi hàm được lồng bên trong là:", a)

# vi_du()
# print("Giá trị của biến a bên ngoài hàm là:",a)

#Define funtion with multiple default argument
# Define function
# Define function
# def printf(*args,sep=' ',end=""):
#     str=sep.join(args)
#     print(str+end)
#     return len(args)

# #Call function
# one_word = printf("learn")
# print(one_word)

# many_words = printf("learn", "python", "with", "tek4.vn")
# print(many_words)

# words_with_sep= printf("learn", "python", "with", "tek4.vn",sep='_')
# print(words_with_sep)

# words_with_end= printf("learn", "python", "with", "tek4.vn",sep='_',end='.')
# print(words_with_end)

# def fibonacci(n):
#   f0=1
#   f1=1
  
#   for i in range(2,n+1):
#     f=f0+f1
#     f0=f1
#     f1=f
#   return f

# n= int(input())
# golden_rate= fibonacci(n+1)/fibonacci(n)

# print(f'Golden rate= {golden_rate}')

# def power(a, b):
#   c=1
#   if b==0:
#     return 1
#   while b>=1:
#     c*=a
#     b-=1
#   return c

# a=float(input())
# n=int(input())
# print(f'{a} to the power of {n} is {power(a,n)}')

# def power(a, b):
#   if b ==0:
#     return 1
#   if a ==0:
#     return 0
#   return a*power(a,b-1)

# a=float(input())
# n=int(input())
# print(f'{a} to the power of {n} is {power(a,n)}')

# my_list = [2, 6, 5, 7, 9, 12, 4, 15]
# # new_list = list(filter(lambda x: x %2==0 , my_list))
# new_list = [i*3 for i in my_list]
# print(new_list)

# age=[18,21,11,2,-2,190,34,17,25,38,26,-21,200,-28,28,19]
# result = filter(lambda age: 15<=age<=130,age)
# result_list = list(result)
# print(result_list)

# a ='đặng văne tỵ'
# b=a[3:6]
# print(b)
# tuple1 = ((5, 15, 25), [10, 20, 30], [20, 10, 30], (5, 15, 25),(15, 5, 25),[16, 24, 33])
# print(tuple1[2][1])
# print(sum(list(map(lambda tum: tum[1] ,tuple1))))

# my_tuple=input()
# mt_to_list = my_tuple.split()
# my_tuple = tuple(mt_to_list)
# print(my_tuple)

# if my_tuple.count("30") == 1: 
#   first_indx = my_tuple.index("30")
#   print(f'FOUND only one time at index: {first_indx}')
# elif my_tuple.count("30")>1:
#   first_indx = my_tuple.index("30")
#   reverse_arr = mt_to_list[::-1].index("30")
#   last_indx= len(mt_to_list) - reverse_arr-1
#   print(f'FOUND {my_tuple.count("30")} times')
#   print(f'The first occurrence is at index: {first_indx}')
#   print(f'And the last occurrence is at index: {last_indx}')
# else:
#   print('NOT FOUND')


# Tìm tuple với tất cả các phần tử chia hết cho K
# test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
# K = int(input())

# test2 = list(map(lambda item: list(item),test_list))
# arr_output= []
# for i in range(len(test2)):
#   arr = list(filter(lambda item: item %K ==0,test2[i]))
#   if arr == test2[i]:
#     arr_output.append(arr)

# test_list = list(map(lambda item: tuple(item),arr_output))
# print(test_list)

  