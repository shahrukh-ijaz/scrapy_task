from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'sheego', '-o', 'test.json'])
# execute(['scrapy', 'crawl', 'quotes'])
# execute(['scrapy', 'shell', 'https://www.sheego.de/'])
