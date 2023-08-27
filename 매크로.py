import pyautogui
import keyboard
import random
from PIL import ImageGrab
import numpy as np
import time as ttt

def m(a, b, x, y):
    pyautogui.moveTo(dayx, dayy, duration=0.4)
    pyautogui.click(dayx, dayy)
    pyautogui.moveTo(a, b)
    pyautogui.click(a, b)
    pyautogui.moveTo(timex,timey, duration=0.3)
    pyautogui.click(timex, timey)
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    

def main():
    print("시간 | 좌석선택완료 버튼 좌표 가져오기\n 마우스 가져다 대고 순서대로 a, b 를 누르면 됨\n")

    while True:
        if keyboard.read_key() == "a":
            xxx, yyy = pyautogui.position()
            break;

    while True:
        if keyboard.read_key() == "b":
            selx, sely = pyautogui.position()
            break;

    print(selx, sely, xxx, yyy)

    print("좌석 캡쳐 영역 잡기 (왼쪽 상단, 오른쪽 하단)\n 마우스 가져다 대고 a, b 순서대로 누르면 됨\n")
    while True:
        if keyboard.read_key() == "a":
            left_top = pyautogui.position()
            break;

    while True:
        if keyboard.read_key() == "b":
            right_bottom = pyautogui.position()
            break;

    print(left_top, right_bottom)

    print("종료는 ctrl + alt + delete 로 빠져나가셈...ㅎㅎ")
    index = 0
    iter_num = 0
    flag = True

    # 좌석 색.
    
    color = []
    
    print( "좌표 색상 저장 , a 저장, c 종료 ")
    while True:
        screen = ImageGrab.grab()
        if keyboard.read_key() == "a":
            x, y = pyautogui.position()
            rgb = screen.getpixel((x, y))
            color.append(rgb)
            print(rgb, "저장 완료")
        if keyboard.read_key() == "c":
            break;

    #좌측상단의 x, 우측하단의 y값을 저장해둔다
    left_top_x = left_top[0]
    right_bottom_y = right_bottom[1]

    #캡쳐 범위의 폭과 높이를 구한다
    capture_width = right_bottom[0]-left_top[0]
    capture_height = right_bottom[1]-left_top[1]

    #좌측상단의 x, 우측하단의 y값을 저장해둔다
    left_top_x = left_top[0]
    right_bottom_y = right_bottom[1]

    #캡쳐 범위의 폭과 높이를 구한다
    capture_width = right_bottom[0]-left_top[0]
    capture_height = right_bottom[1]-left_top[1]



    colorlen = len(color)
    for i in color:
        print(i)
    dif = 10
    
    while flag:
        pyautogui.click(xxx,yyy)

        index = index + 1
        iter_num += 1

        img = ImageGrab.grab()
        for i in range(left_top[0], right_bottom[0], 2):
            if flag == True:
                for j in range(left_top[1], right_bottom[1], 2):
                    rgb = img.getpixel((i,j))
                    if flag == True:
                        for ss in range(colorlen): 
                            if(abs(rgb[0] - color[ss][0]) <= dif and abs(rgb[1] - color[ss][1]) <= dif and abs(rgb[2] - color[ss][2]) <= dif):
                                pyautogui.moveTo(i,j)
                                pyautogui.click(i+1,j+1)
                                pyautogui.moveTo(i,j)
                                pyautogui.click(i-20,j+1)
                                pyautogui.moveTo(selx,sely)
                                pyautogui.click(selx,sely)
                                flag = False
                                break

        ttt.sleep(1)

if __name__ == "__main__":
    main()