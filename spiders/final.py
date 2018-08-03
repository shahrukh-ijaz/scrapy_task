import scrapy
import re
from scrapy.utils.response import open_in_browser



class SheegoSpider(scrapy.Spider):
    name = "sheego"
    start_urls = [
        # 'https://www.sheego.de/neu/alle-damenmode-neuheiten/',
        #'https://www.sheego.de/damenmode/',
        # 'https://www.sheego.de/damen-waesche/',
        # 'https://www.sheego.de/bademode/',
        'https://www.sheego.de/damenschuhe/',
        # 'https://www.sheego.de/damenmode-sale/',

    ]

    def parse(self, response):
        # print("hi hello ")
        for href in response.xpath("//a[contains(@class,'js-product__link')]/@href"):
            yield response.follow(href, self.go_to_item_page)

        next_page = response.xpath('//span[contains(@class,"paging__btn--next")]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # print("\n\n Time to move next page :: " + next_page + "\n\n")
            yield scrapy.Request(next_page, callback=self.parse)

    def go_to_item_page(self, response):  # here response will return the page of each item
        # open_in_browser(response)
        #  print("item page url ::  " + response.url)
        # image url scraper
        image_urls = list()
        for image_url in response.xpath("//a[@id='magic']/@href"):
            image_urls.append(image_url.extract().strip())
        # category scraper
        category = response.xpath("//span[contains(@class,'p-details__name')]/text()").extract_first().strip()
        categories = list()
        categories.append(category)

        for script in response.xpath("//script[contains(@class,'js-ads-script')]/text()"):
            temp = script.extract()

            for main_product_url in temp.split(";"):
                if "window.product.articleVariant.data.ads.anid" in main_product_url:
                    variantid = main_product_url[main_product_url.index("'") + 1:-1]
                    # print("product id :: " + variantid)
                    target_url = response.url.split("?")[0]
                    to_string = ''.join(map(str, target_url))
                    #print(" Link before become targer_url  :: " + to_string)
                    # global final_url
                    final_url = to_string + "?variantid=" + variantid
                    print("Link After become targer_url  :: " + final_url)
                if "window.product.articleVariant.data.ads.aColorIds" in main_product_url:
                    print("hi hello")
                    colors = main_product_url[main_product_url.index("=") + 1:-1] # list of colors available
                    #print(colors)
                    product_opton=list();
                    for index in colors.split(","):
                        # print(index[index.index("'")+1:-1])
                        print(final_url)


