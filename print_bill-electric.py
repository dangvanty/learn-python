# a = 100.375
# print('%.3f' %a)
# print('%.4f' %a)
# print('%d' %(-100))
# print('%o' %(20))
# print("--------------------")
# print("{:20}Python".format("Python"))
# print("{:>20}".format("Python"))
# print("{:^20}".format("Python"))

# string = "{:{fill}{align}{width}}"
# print(string.format('python', fill='*', align='^', width=9))
# num = "{:{align}{width}.{precision}f}"
# print(num.format(392.989, align='<', width=8, precision=1))

# S.no          Product                  Unit Price
# 0             orange                   2    150
# 1             grape                    23   130
# Discount:                                   15
# Total:                                      265
name1 = 'orange'
price1 = 150
unit1 = 2

name2 = 'grape'
price2 = 130
unit2 = 23

tprice = price1 + price2
discount=15
fprice=tprice - discount

# cách 1
# print(str("{:44}"+str('Price')).format(
#   str("{:39}"+str('Unit')).format(str("{:14}"+str('Product')).format('S.no'))
# ))
# print(str("{:44}"+str(price1)).format(
#   str("{:39}"+str(unit1)).format(str("{:14}"+str(name1)).format('0'))
# ))
# print(str("{:44}"+str(price2)).format(
#   str("{:39}"+str(unit2)).format(str("{:14}"+str(name2)).format('1'))
# ))
# print(str("{:44}"+str(discount)).format("Discount:"))
# print(str("{:44}"+str(fprice)).format("Total:"))

print('{0:<14}{1:<25}{2:<5}{3:}'.format('S.no','Product','Unit','Price'))
print('{0:<14}{1:<25}{2:<5}{3:}'.format('0',name1,unit1,price1))
print('{0:<14}{1:<25}{2:<5}{3:}'.format('1',name2,unit2,price2))
print('{0:<44}{1:}'.format('Discount:',discount))
print('{0:<44}{1:}'.format('Total:',fprice))
