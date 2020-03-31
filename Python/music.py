import time
import pygame
import os

filePath="D:\PG1"
list = os.listdir(filePath)
print('\n')
print('可播放音乐有:')
for i in list:
    print(i)

chose = input('\n'+'输入1表示播放第一首歌，以此类推:')

def play(music,file):
    pygame.mixer.init()
    track=pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    print('播放'+file+'中')

if chose == '1':
    music1 = str(filePath)+"\\"+str(list[0])
    file = list[0]
    play(music1,file)
    input()
elif chose == '2':
    music2 = str(filePath)+"\\"+str(list[1])
    file = list[1]
    play(music2,file)
    input()
elif chose == '3':
    music3 = str(filePath)+"\\"+str(list[2])
    file = list[2]
    play(music3,file)
    input()
elif chose == '4':
    music4 = str(filePath)+"\\"+str(list[3])
    file = list[3]
    play(music4,file)
    input()
elif chose == '5':
    music5 = str(filePath)+"\\"+str(list[4])
    file = list[4]
    play(music5,file)
    input()
elif chose == '6':
    music6 = str(filePath)+"\\"+str(list[5])
    file = list[5]
    play(music6,file)
    input()
elif chose == '7':
    music7 = str(filePath)+"\\"+str(list[6])
    file = list[6]
    play(music7,file)
    input()
