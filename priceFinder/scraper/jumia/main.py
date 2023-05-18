import os
from jumia.spiders.jumiaslaptops import jumiaLaptopSpyder
from jumia.spiders.jumiasphones import jumiaPhoneSpyder
from jumia.spiders.kongaphones import kongaPhoneSpyder
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging



def scrapy():
    
    settings={
            'BOT_NAME': 'web_page_crawler',
            'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'ROBOTSTXT_OBEY': False,
            'SPLASH_URL': 'http://localhost:8050',
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy_splash.SplashCookiesMiddleware': 723,
                'scrapy_splash.SplashMiddleware': 725,
                'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            },
            'SPIDER_MIDDLEWARES': {
                'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
            },
        "FEEDS" : {
        "./priceFinder/scrapy_data/%(name)s_%(time)s.json": {
        "format": "json",
        }
    },


            'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
            'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage'
        }
 
    process = CrawlerProcess(settings)
    process.crawl(jumiaLaptopSpyder)
    process.crawl(jumiaPhoneSpyder)
    process.start()  # the script will block here until all crawling jobs are finished

scrapy()


""""
    configure_logging(settings)
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(jumiaLaptopSpyder)
        yield runner.crawl(jumiaPhoneSpyder)
        reactor.stop()

    crawl()
    reactor.run() # the script will block here until the last crawl call is finished

"""