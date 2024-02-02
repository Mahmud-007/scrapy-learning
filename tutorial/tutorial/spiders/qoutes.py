import scrapy
from scrapy.http import FormRequest
from ..items import TutorialItem

class QoutesSpider(scrapy.Spider):
    name = "qoutes"
    page_number = 2
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        token = response.css("form input::attr(value)").extract()
        print("csrf",token)
        return FormRequest.from_response(response, formdata={
            "csrf_token": token,
            "username": "attreya01@gmail.com",
            "password": "dsadsdsa"
        }, callback = self.start_scraping)
    
    def start_scraping(self,response):
        items = TutorialItem()
        all_div_quotes = response.css("div.quote")
        
        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tags = quote.css(".tag::text").extract()
            items["title"] = title
            items["author"] = author
            items["tags"] = tags
            yield items