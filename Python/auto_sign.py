import pyautogui as pg
import time

"""
使用前请先看以下概述,再根据你的情况小小修改代码即可运行。

这个简单的自动签到是靠python的pyautogui库(你需要先下载这个库)实现的
主要是靠以下几个方法:
pyautogui.position()        确定鼠标当前位置，返回x,y坐标的元组

pyautogui.moveTo(x,y[,duration = t])
    将鼠标移动到屏幕指定位置
    duration参数是鼠标移动所需要的秒数，如果不写这个参数，鼠标指针会瞬间到达给定位置
    
pyautogui.click()    默认在当前光标位置，使用鼠标左键点击

pyautogui.press()    根据传入的键字符串，向计算机发送虚拟的按键然后释放

pyautogui.write()    根据传入的字符串模拟键盘输入
"""

pg.press('win')
pg.write('google')
pg.press('enter')
pg.press('enter')
#此处位置是你的浏览器输入网址的输入框的位置
pg.moveTo(487,65,duration=1)    
pg.click()
pg.write('https://fishc.com.cn/plugin.php?id=k_misign:sign')  #此处的网址是你鱼c论坛的签到页面
pg.press('enter')
pg.moveTo(220,531,duration=1)   #此处位置是你的签到页面的签到按钮的位置
pg.click()


