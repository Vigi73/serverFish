import psutil as pu
import pyautogui as bot
import pytesseract
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

main = ctypes.windll.user32.FindWindowW("main", None)
ctypes.windll.user32.ShowWindow(main, 6)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

x, y = bot.size()

x = (x // 2) - 402
y = (y // 2) - 319

x_value = x + 32
y_value = y + 44


def fish_tank():
    global x, y, x_value, y_value
    if bot.locateOnScreen(r'img\tank.png', region=(x, y, x + 112, y + 35)):
        img = bot.screenshot('my_screenshot.png', region=(x_value, y_value, 329, 151))
        answer = pytesseract.image_to_string(img, lang='rus').split('\n')[:4]
        bot.sleep(.2)
        bot.press('space')
        bot.sleep(.2)
        return answer
    else:
        pass


tmp_fish = ""

while True:
    if "RF3.exe" in [p.name() for p in pu.process_iter()]:

        if ans := fish_tank():
            if str(ans) != tmp_fish:
                try:
                    fish = ans[0]
                except:
                    fish = "error"
                try:
                    width_f = ans[1].split(':')[1].split()[0].strip().replace(",", '.')
                except:
                    width_f = "error"
                try:
                    if "зачетная" in ans[1]:
                        top = "зачетная"
                    else:
                        top = "мелочь"
                except:
                    top = "error"

                try:
                    bait = ans[2].split(':')[1].strip()
                except:
                    bait = "error"
                try:
                    base = ans[3].split(":")[1].split(',')[0].strip()
                except IndexError:
                    base = ""

                try:
                    location = ans[3].split(":")[1].split(',')[1].strip()
                except IndexError:
                    location = ""

                with open('log.txt', 'a', encoding='utf-8') as f:
                    print(f'{fish}; {width_f}; {top}; {bait}; {base}; {location}', file=f)
                    # print(f'{fish}; {width_f}; {top}; {bait}; {base}; {location}')
                tmp_fish = str(ans)

    else:
        bot.alert('Запустите рыбалку')
        break
