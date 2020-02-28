def jc(num):
    if num==1:
        return 1;
    else :
         n = num * jc(num-1)
         return n

num = int(input("输入一个整数\n"))

print("%d的阶乘是%d" % (num,jc(num)))
