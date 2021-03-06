import psutil as pu
import pyautogui as bot
import pytesseract
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

main = ctypes.windll.user32.FindWindowW("main", None)
ctypes.windll.user32.ShowWindow(main, 4)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

x, y = bot.size()
print(x, y)

x = (x // 2) - 401
y = (y // 2) - 320

x_value = x + 22
y_value = y + 40


def fish_tank():
    global x, y, x_value, y_value
    if bot.locateOnScreen(r'img\tank.png', region=(x, y, x + 111, y + 36)):
        img = bot.screenshot('my_screenshot.png', region=(x_value, y_value, 330, 145))
        bot.sleep(.5)
        answer = pytesseract.image_to_string(img, config='--psm 6', lang='rus').split('\n')[:4]
        bot.sleep(.5)
        bot.press('space')
        # bot.sleep(.5)
        print(answer)
        return answer
    else:
        pass


tmp_fish = ""
err = 0  # value if error else null
while True:

    if "RF3.exe" in [p.name() for p in pu.process_iter()]:
        # print(fish_tank())
        try:
            if ans := fish_tank():
                if str(ans) != tmp_fish:
                    try:
                        fish = ans[0]
                    except:
                        err += 1
                    try:
                        width_f = ans[1].split(':')[1].split()[0].strip().replace(",", '.')
                    except:
                        err += 1
                    try:
                        if "зачетная" in ans[1]:
                            top = "зачетная"
                        else:
                            top = "мелочь"
                    except:
                        err += 1

                    try:
                        bait = ans[2].split(':')[1].strip()
                    except:
                        bait = "error"
                    try:
                        base = ans[3].split(":")[1].split(',')[0].strip()
                    except IndexError:
                        err += 1

                    try:
                        location = ans[3].split(":")[1].split(',')[1].strip()
                    except IndexError:
                        err += 1

                    if err == 0:
                        with open('log.txt', 'a', encoding='utf-8') as f:
                            print(f'{fish}; {width_f}; {top}; {bait}; {base}; {location}', file=f)
                            # print(f'{fish}; {width_f}; {top}; {bait}; {base}; {location}')
                        tmp_fish = str(ans)
                    else:
                        err = 0
        except:
            print('Что-то пошло не так :-(')

    else:
        bot.alert('Запустите рыбалку')
        break
