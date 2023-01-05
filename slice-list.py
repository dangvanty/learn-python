my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# in ra danh sách con chứa 5 phần tử đầu tiên
print(my_list[:5])
# in ra danh sách con chứa 5 phần tuer cuối
print(my_list[-5:])
# in ra danh sách con bắt đầu từ phần tử 2 đến phần tử 9 bước nhảy 2
print(my_list[2:9:2]) #[23, 17.6, 12.2, 11.5] 

my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]

print(my_list[:7:2]) #[-1.2, 23, 17.6, 12.2]
print(my_list[:-6:-2])  #[45.6, 20.6, 23.5]
print(my_list[2:9:3]) #[23, 23.5, 11.5]
print(my_list[7:-10:-3]) #[20.6, 17.6, 18.9]
print(my_list[::3]) #[-1.2, 12.4, 12.2, 45.6]
print(my_list[:-10:-2]) #[45.6, 20.6, 23.5, 12.4, 18.9]
print(my_list[::]) #[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2, 20.6, 11.5, 45.6]
print(my_list[:4]) #[-1.2, 18.9, 23, 12.4]
print(my_list[6:]) #[12.2, 20.6, 11.5, 45.6]

# them phan tu bang danh sach con:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
# vi du 2
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']
import test as t
t.n
t.fibonacci(t.n)