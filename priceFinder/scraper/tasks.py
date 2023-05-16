




from scraper.jumia.jumia.spiders.jumiaslaptops import jumiaLaptopSpyder
from scraper.jumia.jumia.spiders.jumiasphones import jumiaPhoneSpyder
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from celery import shared_task



@shared_task
def scrape():
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
        "s3://scrapy-outputfiles/scrapy/%(name)s_%(time)s.json": {
        "format": "json",
        }
    },

    "AWS_ACCESS_KEY_ID" :'AKIAZPO36HGBPFNCGKZE',
    "AWS_SECRET_ACCESS_KEY": '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',
            'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
            'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage'
        }
    configure_logging(settings)
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(jumiaLaptopSpyder)    
        yield runner.crawl(jumiaPhoneSpyder)
        
    crawl()
    reactor.run() # the script will block here until the last crawl call is finished
       
if __name__ == '__main__':
    scrape()
    reactor.stop()





