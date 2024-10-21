import scrapy
from hw2_scrapy.items import Hw2ScrapyItem
from bs4 import BeautifulSoup

class MlbSpiderSpider(scrapy.Spider):
    name = "mlb_spider"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["https://www.mlb.com/stats/"]
    page_number = 1

    def parse(self, response):
        # Check if the current page is valid before processing
        if not self.is_valid_page(response):
            print(f"Page {self.page_number} is not valid.")
            return
    
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("tbody", class_="notranslate")
        rows = table.find_all("tr")

        for row in rows:
            item = Hw2ScrapyItem()
            item["PLAYER"] = row.find("th").text
            item["TEAM"] = row.find("td", attrs={"data-col": '1'}).text
            item["G"] = row.find("td", attrs={"data-col": '2'}).text
            item["AB"] = row.find("td", attrs={"data-col": '3'}).text
            item["R"] = row.find("td", attrs={"data-col": '4'}).text
            item["H"] = row.find("td", attrs={"data-col": '5'}).text
            item["HR"] = row.find("td", attrs={"data-col": '8'}).text
            item["RBI"] = row.find("td", attrs={"data-col": '9'}).text
            item["BB"] = row.find("td", attrs={"data-col": '10'}).text
            item["SO"] = row.find("td", attrs={"data-col": '11'}).text
            item["SB"] = row.find("td", attrs={"data-col": '12'}).text
            item["AVG"] = row.find("td", attrs={"data-col": '14'}).text
            item["OBP"] = row.find("td", attrs={"data-col": '15'}).text
            item["SLG"] = row.find("td", attrs={"data-col": '16'}).text
            yield item

        self.page_number = self.page_number + 1
        next_page = self.start_urls[0] + "?page=" + str(self.page_number)
        yield response.follow(next_page, callback=self.parse)
            
        pass

    def is_valid_page(self, response):
        # Check if the table with player stats exists
        table = response.xpath('//tbody[@class="notranslate"]')
        
        ### Not working as expected ###
        # If the table is not found, the page is not valid
        #if not table:
            #print(f"Table not found on page {self.page_number}.")
            #return False

        # Check if there are any rows in the table (in case it's an empty table)
        rows = table.xpath('.//tr')
        if not rows:
            print(f"No rows found on page {self.page_number}.")
            return False

        return True

