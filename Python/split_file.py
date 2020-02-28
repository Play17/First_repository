def save_file(boy,girl,count):  #保存文件的函数
    boy_file_name = '小甲鱼_' + str(count) + '.txt'  #给保存小甲鱼对话的文件命名
    girl_file_name = '小客服_' + str(count) + '.txt'  #给保存小客服对话的文件命名

    boy_file = open(boy_file_name,'w')    #以写入的方式打开小甲鱼对话的文件对象，并给个名boy_file的标签
    girl_file = open(girl_file_name,'w')  #以写入的方式打开小客服对话的文件对象，并给个名firl_file的标签

    boy_file.writelines(boy)    #把boy列表的字符串写入文件boy_file中
    girl_file.writelines(girl)  #把girl列表的字符串写入文件girl_file中

    boy_file.close()    #关闭文件boy_file
    girl_file.close()   #关闭文件girl_file

def split_file(file_name):  #分割字符串的函数
    f = open(file_name)  #打开需要分割字符串的文件对象，并给个名f的标签
    boy = []   #存放小甲鱼对话的列表
    girl = []  #存放小客服对话的列表
    count = 1  #count变量用于表示段落1，2，3
    
    for i in f:                               #for循环获取文件的每一句话
        if i[:3] != '===':                    #如果一句话的前三个值不是===的话
            (name,word) = i.split(':',1)      #就以冒号为基础分割两者
            if name == '小甲鱼':               #如果前者是小甲鱼
                boy.append(word)              #就把前者对应的后者的值添加到boy列表
            if name == '小客服':               #如果前者是小客服
                girl.append(word)             #就把前者对应的后者的值添加到girl列表
        else:
            save_file(boy,girl,count)         #调用保存文件的函数
            boy = []                          #把boy列表变为空列表
            girl = []                         #把girl表变为空列表
            count += 1                        #count + 1
    
    #save_file(boy,girl,count)                 #调用保存文件的函数
    f.close()                                 #关闭文件对象f

split_file('E:/小甲鱼与小客服对话/xjy.txt')     #调用split_file函数传入文件参数
