from playwright.async_api import async_playwright
import scrapy
from scrapy_playwright.page import PageMethod
import time
from scrapy import Item, Field



class Scraping(scrapy.Spider):

    name = 'Work_Domains'

    def start_requests(self):
        yield scrapy.Request('https://v-tylu.work/?transaction_type=offering-with-online-payment',
                             meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_methods=[
                                     # This where we can implement scrolling if we want
                                     PageMethod(
                                         'wait_for_selector', 'div.wrapper')
                                 ]
                             )
                             )

    async def parse(self, response):
        scrapped_info = {
                      'profession': response.xpath("//a[@class='item__title']//text()").extract(),
                      'tag': response.xpath("//div[@class='item__tags']//text()").extract(),
                      'location': response.xpath("//div[@class='item__location']//text()").extract(),
                      'description': response.xpath("//div[@class='item__desc']//text()").extract(),
                      'date': response.xpath("//div[@class='item__create-date']//text()").extract()
                }
        yield scrapped_info
