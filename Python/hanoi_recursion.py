def hanoi(n):
    if n == 1:
        return 1
    else :
        return 2*hanoi(n-1)+1

n = int(input('请输入汉诺塔层数\n'))
print("共需要移动%d次" % (hanoi(n)))
