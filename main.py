import psutil as pu
import pyautogui as bot
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

x, y = bot.size()

x = (x // 2) - 402
y = (y // 2) - 319

x_value = x + 33
y_value = y + 45


def fish_tank():
    global x, y, x_value, y_value
    if bot.locateOnScreen(r'img\tank.png', region=(x, y, x + 112, y + 35)):
        img = bot.screenshot('my_screenshot.png', region=(x_value, y_value, 328, 150))
        answer = pytesseract.image_to_string(img, lang='rus').split('\n')[:4]
        bot.press('space')
        bot.sleep(.1)
        return answer
    else:
        pass


while True:
    if "RF3.exe" in [p.name() for p in pu.process_iter()]:
        print("Процесс запущен...")
        if fish := fish_tank():
            with open('log.txt', 'a', encoding='utf-8') as f:
                print(fish, file=f)

    else:
        bot.alert('Запустите рыбалку')
        break
