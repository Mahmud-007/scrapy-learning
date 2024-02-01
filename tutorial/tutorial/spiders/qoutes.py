import scrapy
from ..items import TutorialItem

class QoutesSpider(scrapy.Spider):
    name = "qoutes"
    page_number = 2
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1"]

    def parse(self, response):
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

        next_page = "https://quotes.toscrape.com/page/"+str(QoutesSpider.page_number) + "/"
        if QoutesSpider.page_number <11:
            QoutesSpider.page_number +=1
            yield response.follow(next_page,callback = self.parse)


