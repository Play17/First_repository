def fab(n):
    if n<1:
        print("输入有误!")

    if n==1 or n==2 :
        return 1
    else:
        return fab(n-1) + fab(n-2)

n = int(input("输入月数:\n"))
print("%d个月后共有%d个小兔崽子诞生" % (n,fab(n)))
      
