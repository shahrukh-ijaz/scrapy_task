from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'sheego', '-o', 'sheegoitems.json'])
# execute(['scrapy', 'crawl', 'quotes'])
# execute(['scrapy', 'shell', 'https://www.sheego.de/'])
