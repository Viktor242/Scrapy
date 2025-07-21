import scrapy

# Паук для парсинга светильников с сайта divan.ru
class DivanSvetSpider(scrapy.Spider):
    name = "divansvetspider"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div.WdR1o')
        for divan in divans:
            yield {
                'Наименование': divan.css('div.lsooF span::text').get(),
                'Цена': divan.css('span[data-testid="price"]::text').get(),
                'Ссылка': divan.css('a::attr(href)').get()
            }
            
