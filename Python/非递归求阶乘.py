def jc(num):
    sum = 0
    for i in range(1,num):
        num *= i
        sum +=num
    return sum

num = int(input("输入一个整数"))
print("1到%d的阶乘之和是%d" % (num,jc(num)))
