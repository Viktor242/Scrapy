from colorama import Fore, Style, init
import re

init(autoreset=True)

html = '<h2>Заголовок</h2><p>Текст</p>'

# Функция для подсветки тегов
def highlight_tags(text):
    return re.sub(r'(<[^>]+>)', Fore.GREEN + r'\1' + Style.RESET_ALL, text)

print(highlight_tags(html)) 