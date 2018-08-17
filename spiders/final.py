# import scrapy
# import json
# from scrapy.utils.response import open_in_browser
#
# final_url = ''
# variantid = ''
# result = 0
# to_string = ''
# json = ''
#
## class sheegoItem(scrapy.Item):
#     spiderName = scrapy.Field()
#     category = scrapy.Field()
#     url = scrapy.Field()
#     retailer = scrapy.Field()
#     image_url = scrapy.Field()
#
#
# class SheegoSpider(scrapy.Spider):
#     name = "SheegoSpider"
#     start_urls = [
#         # 'https://www.sheego.de/neu/alle-damenmode-neuheiten/',
#         #'https://www.sheego.de/damenmode/',
#         # 'https://www.sheego.de/damen-waesche/',
#         #'https://www.sheego.de/bademode/',
#          'https://www.sheego.de/damenschuhe/',
#         # 'https://www.sheego.de/damenmode-sale/',
#     ]
#
#     def parse(self, response):
#         for href in response.xpath("//a[contains(@class,'js-product__link')]/@href"):
#             yield response.follow(href, self.go_to_item_page)
#
#         next_page = response.xpath('//span[contains(@class,"paging__btn--next")]/a/@href').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             # print("\n\n Time to move next page :: " + next_page + "\n\n")
#             yield scrapy.Request(next_page, callback=self.parse)
#
#     def go_to_item_page(self, response):  # here response will return the page of each item
#         item = sheegoItem()
#         item['url'] = response.url
#         item['spiderName'] = "SheegoSpider"
#         cateogry_list = list()
#
#         print("RESPONSE ::", response.url)
#
#         for x in response.xpath("//section[contains(@class,'c-breadcrumb')]/span[contains(@class,'breadcrumb__item')]"):
#                print("DAta :: ", x.xpath("a[contains(@class,'text-link')]/span[@itemprop]"))
#                # print("DATA :: ", x.xpath("strong/text()").extract())
#                # print("DATA :: ", x.xpath("a/span/text()").extract())
#
#         # /a[contains(@class,'text-link')]/span/text()
#
#         #print(cateogry_list)
#         # image_urls = list()
#         # for image_url in response.xpath("//a[@id='magic']/@href"):
#         #     image_urls.append(image_url.extract().strip())
#         # # category scraper
#         # category = response.xpath("//span[contains(@class,'p-details__name')]/text()").extract_first().strip()
#         # categories = list()
#         # categories.append(category)
#         # list_of_color = list()
#         # for script in response.xpath("//section[contains(@class,'p-details__variants')]/section"
#         #                              "/section[contains(@class,' color')]"
#         #                              "/div[contains(@class,'cj-slider')]/div[contains(@class, 'cj-slider__frame')]"
#         #                              "/div[contains(@class, 'cj-slider__slides')]"
#         #                              "/script[contains(@class,'js-ads-script')][1]/text()"):
#         #     data = script.extract()
#         #     data = data.split("=")[1]
#         #     data = data.split(";")[0]
#         #     data = data.replace("[", '')
#         #     data = data.replace("]", '')
#         #     for index in data.split(","):
#         #         index = index.replace("'","")
#         #         index = index.replace(" ","")
#         #         list_of_color.append(index)
#         #
#         #     # print("List :: ", list_of_color)
#         #     link = response.url.split("?")[0] + "?color="
#         #     urls = list()
#         #     # print("These are the links of the products :: \n")
#         #     for index in list_of_color:
#         #         temp = link + index
#         #         i = 0
#         #         # print(temp)
#         #         urls.append(temp)# Is it possible to send list
#             # yield response.follow(urls, self.extract_item_details)
#
#     def extract_item_details(self, response):
#         print("Hello from the extract item details function!!\n")
#         color_data = response.xpath("//section[contains(@class,'p-details__variants')]/section/p[last()]/text()").extract()
#         color_name = ''
#         # for index in color_data:
#         #     index = index.replace("\n", "")
#         #     index = index.replace(" ", "")
#         #     if index != '':
#         #         color_name = index
#         # print(color_name)
#         price = response.xpath("//section[contains(@class,'p-details__price')]/span[contains(@class,'l-subline-2')]/text()")
#         sizes = list()
#        # for size in response.xpath("//div[contains(@class,'c-sizespots')]/div[contains(@class,'sizespots__item')]/text()").extract():
#        # response.xpath("//section[contains(@class,'size')]/select[contains(@class,'js-sh-dropdown')]/option[@disabled]/text()").extract() for all sizes which are not available
#         for size in response.xpath("//div[contains(@class,'c-sizespots')]/div[contains(@class,'sizespots__item')]/text()").extract():
#             size = size.replace("\n", '')
#             size = size.replace(" ", '')
#             sizes.append(size)
#         print(sizes)
#
