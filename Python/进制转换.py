def binary_decimal(binary):
    binary = int(binary,2)
    print('转换为十进制是:',binary)

def binary_hexadecimal(binary):
    binary = hex(int(binary,2))
    print('转换为十六进制是:',binary)

def decimal_binary(decimal):
    decimal = bin(int(decimal))
    print('转换为二进制是:',decimal)

def decimal_hexadecimal(decimal):
    decimal = hex(int(decimal,10))
    print('转换为十进制是:',decimal)

def hexadecimal_binary(hexadecimal):
    hexadecimal = bin(int(hexadecimal,16))
    print('转换为二进制是:',hexadecimal)

def hexadecimal_decimal(hexadecimal):
    hexadecimal = int(hexadecimal,16)
    print('转换为十进制是:',hexadecimal)

def agein():
    print("-------------")
    chose_answer = int(input("输入1重新运行这个程序,  输入0退出:"))
    if chose_answer:
        run()
    else:
        exit()
    

def run():
    chose_input = input("输入A选择输入二进制数据,   输入B选择输入十进制数据,  输入C选择输入十六进制\n")
    if chose_input == 'A' :
        binary = input('输入一个二进制数字:')
        chose_output = input("输入A选择输出十进制数据,  输入B选择输出十六进制数据.\n")
        if chose_output == 'A':
            binary_decimal(binary)
            agein()
        elif chose_output == 'B':
            binary_hexadecimal(binary)
            agein()
    elif chose_input == 'B':
        decimal = input('输入一个十进制数字:')
        chose_output = input("输入A选择输出二进制数据,  输入B选择输出十六进制数据.\n")
        if chose_output == 'A':
            decimal_binary(decimal)
            agein()
        elif chose_output == 'B':
            decimal_hexadecimal(decimal)
            agein()
    elif chose_input == 'C':
        hexadecimal = input('输入一个十六进制数字:')
        chose_output = input("输入A选择输出二进制数据,  输入B选择输出十进制数据.\n")
        if chose_output == 'A':
            hexadecimal_binary(hexadecimal)
            agein()
        elif chose_output == 'B':
            hexadecimal_decimal(hexadecimal)
            agein()   
    else:
        print('输入有误!')
        agein()
        

run()
