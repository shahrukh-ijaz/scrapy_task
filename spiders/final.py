import scrapy


class QuotesSpider(scrapy.Spider):
    name = "sheego"
    start_urls = [
        'https://www.sheego.de/neu/alle-damenmode-neuheiten/',
        'https://www.sheego.de/damenmode/',
        'https://www.sheego.de/damen-waesche/',
        'https://www.sheego.de/bademode/',
        'https://www.sheego.de/damenschuhe/',
        'https://www.sheego.de/damenmode-sale/',

    ]

    def parse(self, response):

        for title in response.xpath("//div[contains(@class,'product__wrapper--bottom')]"):

            name = title.xpath("a/div[contains(@class,'product__title')]/text()").extract_first().strip()
            price = title.xpath("a/div[contains(@class,'product__price')]/span/text()").extract_first().strip()

            link = title.xpath("//div[contains(@class,'product__wrapper')]/div[contains(@class,'js-product__wrapper')]"
                               "/a[contains(@class,'js-product__link')]/img[contains(@class,'cj-product__image')]"
                               "/@src").extract_first().strip()
            yield {
                'name': name,
                'price': price,
                'image_link': link
            }




