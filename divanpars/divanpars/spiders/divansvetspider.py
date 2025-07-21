import scrapy

# Паук для парсинга диванов с сайта divan.ru
class DivanSvetSpider(scrapy.Spider):
    name = "divansvetspider"  # Имя паука для запуска через Scrapy
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Получаем все карточки товаров по актуальному классу
        divans = response.css('div.WdR1o')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('span[data-testid="price"]::text').get(),
                'url': divan.css('a::attr(href)').get()  # Современный способ получения ссылки
            }