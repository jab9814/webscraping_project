import scrapy


class ModelSportSpider(scrapy.Spider):
    name = "model_sport"
    allowed_domains = ["x"]
    start_urls = ["https://x"]

    def parse(self, response):
        pass
