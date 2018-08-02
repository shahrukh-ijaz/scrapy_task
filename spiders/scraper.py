import scrapy
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst, Join


# class Product(scrapy.item):
#     imageLink = scrapy.Field()
#     sizes = scrapy.Field()
#     price = scrapy.Field()
#     Name = scrapy.Field()
#
# class ProductLoader(ItemLoader):
class QuotesScraper(scrapy.Spider):
    name = "webScrap"
    start_urls = ['https://www.sheego.de/']

    def parse(self, response):
        yield "hi"
        # for e in response.css("div.cj-mainnav__entry a::href").extract():
        #     if len(e.strip()) != 0:
        #         yield e




#
# class QuotesSpider(scrapy.Spider):
#     name = "advanceScrapy"
#     start_urls = [
#         'https://www.sheego.de/',
#     ]
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield    {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }