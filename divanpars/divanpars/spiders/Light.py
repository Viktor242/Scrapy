# Код для Selenium с правильными селекторами и сохранением в CSV
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By



# Запуск Chrome
driver = webdriver.Chrome()  # Если chromedriver.exe в PATH или рядом со скриптом

url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(7)  # Увеличьте время ожидания, если интернет медленный

lights = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')
print(f"Найдено товаров: {len(lights)}")

parsed_data = []

for light in lights:
    try:
        # Название светильника
        title_element = light.find_element(By.CSS_SELECTOR, 'div.lsooF span')
        title = title_element.text

        # Ссылка на товар
        try:
            link_element = light.find_element(By.CSS_SELECTOR, 'a')
            link = link_element.get_attribute('href')
        except:
            link = "Нет ссылки"

        # Цена светильника
        try:
            price_element = light.find_element(By.CSS_SELECTOR, 'span[data-testid=\"price\"]')
            price = price_element.text
        except:
            price = "Не указана"

        print(f"Название: {title}, Цена: {price}, Ссылка: {link}")

        parsed_data.append([title, price, link])

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

driver.quit()

with open("Light.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на светильник'])
    writer.writerows(parsed_data)

print("Файл Light.csv успешно создан!")