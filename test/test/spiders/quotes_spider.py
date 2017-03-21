import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

import parse
import block_tree
import lxml.html as lhtml

########################CATEGORY ECOMMERCE#####################
# (01) IN USE
class etsySpider(scrapy.Spider):
    name = "etsy"
    def start_requests(self):
        urls = [
            "https://www.etsy.com/developers/documentation",
        ]
        base_url = "https://www.etsy.com/developers/documentation"
        file_name = "etsy"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (02) IN USE
class shopifySpider(scrapy.Spider):
    name = "shopify"
    def start_requests(self):
        urls = [
            "https://help.shopify.com/api/reference",
        ]
        base_url = "https://help.shopify.com/api/reference"
        file_name = "shopify"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (03) IN USE
class ebanxSpider(scrapy.Spider):
    name = "ebanx"
    def start_requests(self):
        urls = [
            "https://www.ebanx.com/business/en/developers/api-reference",
        ]
        base_url = "https://www.ebanx.com/business/en/developers/api-reference"
        file_name = "ebanx"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (04) IN USE
class clearentSpider(scrapy.Spider):
    name = "clearent"
    def start_requests(self):
        urls = [
            "http://developer.clearent.com/docs-and-apis/",
        ]
        base_url = "http://developer.clearent.com/docs-and-apis/"
        file_name = "clearent"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (05) IN USE
class bestBuySpider(scrapy.Spider):
    name = "bestBuy"
    def start_requests(self):
        urls = [
            "https://bestbuyapis.github.io/api-documentation",
        ]
        base_url = "https://bestbuyapis.github.io/api-documentation"
        file_name = "bestBuy"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (06) IN USE, FORBIDDEN FOR FREQUENT REQUEST
class eBayBPMSpider(scrapy.Spider):
    name = "eBayBPM"
    def start_requests(self):
        urls = [
            "http://developer.ebay.com/Devzone/business-policies/Concepts/BusinessPoliciesAPIGuide.html",
        ]
        base_url = "http://developer.ebay.com/Devzone/business-policies"
        file_name = "eBayBPM"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (07) IN USE
class cityGridSpider(scrapy.Spider):
    name = "cityGrid"
    def start_requests(self):
        urls = [
            "http://docs.citygridmedia.com/display/citygridv2/CityGrid+APIs",
        ]
        base_url = "http://docs.citygridmedia.com/display/citygridv2"
        file_name = "cityGrid"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (08) IN USE
class walmartLabsSpider(scrapy.Spider):
    name = "walmartLabs"
    def start_requests(self):
        urls = [
            "https://developer.walmartlabs.com/docs",
        ]
        base_url = "https://developer.walmartlabs.com/docs"
        file_name = "walmartLabs"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (09) IN USE
class bigCommerceSpider(scrapy.Spider):
    name = "bigCommerce"
    def start_requests(self):
        urls = [
            "https://developer.bigcommerce.com/api",
        ]
        base_url = "https://developer.bigcommerce.com/api"
        file_name = "bigCommerce"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (10) IN USE
class dealSurfSpider(scrapy.Spider):
    name = "dealSurf"
    def start_requests(self):
        urls = [
            "http://api.dealsurf.com",
        ]
        base_url = "http://api.dealsurf.com"
        file_name = "dealSurf"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)

########################CATEGORY MOBILE########################
# (01) IN USE
class cleverTapSpider(scrapy.Spider):
    name = "cleverTap"
    def start_requests(self):
        urls = [
            "https://support.clevertap.com/docs/api/getting-started.html",
        ]
        base_url = "https://support.clevertap.com/docs/api"
        file_name = "cleverTap"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (02) IN USE
class batchSpider(scrapy.Spider):
    name = "batch"
    def start_requests(self):
        urls = [
            "https://batch.com/doc/api/prerequisites.html",
        ]
        base_url = "https://batch.com/doc/api"
        file_name = "batch"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (03) IN USE
class oneSignalSpider(scrapy.Spider):
    name = "oneSignal"
    def start_requests(self):
        urls = [
            "https://documentation.onesignal.com/reference",
        ]
        base_url = "https://documentation.onesignal.com/reference"
        file_name = "oneSignal"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (04) IN USE
class linxSpider(scrapy.Spider):
    name = "1Linx"
    def start_requests(self):
        urls = [
            "http://1linx.com/",
        ]
        base_url = "http://1linx.com/"
        file_name = "1Linx"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (05) IN USE
class appSeeSpider(scrapy.Spider):
    name = "appSee"
    def start_requests(self):
        urls = [
            "https://www.appsee.com/docs",
        ]
        base_url = "https://www.appsee.com/docs"
        file_name = "appSee"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (06) IN USE
class deviceAtlasSpider(scrapy.Spider):
    name = "deviceAtlas"
    def start_requests(self):
        urls = [
            "https://deviceatlas.com/resources/rest-api",
        ]
        base_url = "https://deviceatlas.com/resources/rest-api"
        file_name = "deviceAtlas"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (07) IN USE
class prowlAppSpider(scrapy.Spider):
    name = "prowlApp"
    def start_requests(self):
        urls = [
            "https://www.prowlapp.com/api.php",
        ]
        base_url = "https://www.prowlapp.com/api.php"
        file_name = "prowlApp"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)

########################CATEGORY TOOLS#########################
# (01) IN USE
class colourLoversSpider(scrapy.Spider):
    name = "colourLovers"
    def start_requests(self):
        urls = [
            "http://www.colourlovers.com/api",
        ]
        base_url = "http://www.colourlovers.com/api"
        file_name = "colourLovers"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (02) IN USE
class githubSpider(scrapy.Spider):
    name = "github"
    def start_requests(self):
        urls = [
            "https://developer.github.com/v3/",
        ]
        base_url = "https://developer.github.com/v3"
        file_name = "github"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (03) IN USE
class uClassifySpider(scrapy.Spider):
    name = "uClassify"
    def start_requests(self):
        urls = [
            "https://www.uclassify.com/docs/urlrestapi",
            "https://www.uclassify.com/docs/restapi"
        ]
        base_url = "https://www.uclassify.com/docs"
        file_name = "uClassify"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (04) IN USE
class zapierSpider(scrapy.Spider):
    name = "zapier"
    def start_requests(self):
        urls = [
            "https://zapier.com/developer/documentation/v2/",
        ]
        base_url = "https://zapier.com/developer/documentation/v2"
        file_name = "zapier"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (05) IN USE
class semantriaSpider(scrapy.Spider):
    name = "semantria"
    def start_requests(self):
        urls = [
            "https://semantria.readme.io/v4.2.2/docs",
        ]
        base_url = "https://semantria.readme.io/v4.2.2/docs"
        file_name = "semantria"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (06) IN USE
class airBrakeSpider(scrapy.Spider):
    name = "airBrake"
    def start_requests(self):
        urls = [
            "https://airbrake.io/docs/api/",
        ]
        base_url = "https://airbrake.io/docs/api/"
        file_name = "airBrake"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (07) IN USE
class producteevSpider(scrapy.Spider):
    name = "producteev"
    def start_requests(self):
        urls = [
            "https://www.producteev.com/api/doc/",
        ]
        base_url = "https://www.producteev.com/api/doc/"
        file_name = "producteev"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (08) IN USE
class whoisXmlSpider(scrapy.Spider):
    name = "whoisXml"
    def start_requests(self):
        urls = [
            "https://www.whoisxmlapi.com/whois-api-guide.php",
            "https://www.whoisxmlapi.com/domain-availability-api-guide.php",
            "https://www.whoisxmlapi.com/reverse-whois-api-guide.php",
            "https://www.whoisxmlapi.com/brand-alert-api-guide.php",
            "https://www.whoisxmlapi.com/registrant-alert-api-guide.php"
        ]
        base_url = "https://www.whoisxmlapi.com/"
        file_name = "whoisXml"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        # for href in response.css('a::attr(href)').extract():
        #     new_url = response.urljoin(href)
        #     yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (09) IN USE
class slackSpider(scrapy.Spider):
    name = "slack"
    def start_requests(self):
        urls = [
            "https://api.slack.com/",
        ]
        base_url = "https://api.slack.com"
        file_name = "slack"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)
# (10) IN USE
class aylienSpider(scrapy.Spider):
    name = "aylien"
    def start_requests(self):
        urls = [
            "http://docs.aylien.com/docs/",
        ]
        base_url = "http://docs.aylien.com/docs"
        file_name = "aylien"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)

########################CATEGORY MESSAGING#####################
#
class hoiioSpider(scrapy.Spider):
    name = "hoiio"
    def start_requests(self):
        urls = [
            "http://openapi.hoiio.com/docs/",
        ]
        base_url = "http://openapi.hoiio.com/docs"
        file_name = "hoiio"
        visited_urls = []
        for url in urls:
            yield scrapy.Request(url=url, meta={"name": file_name, "v_urls": visited_urls, "b_url": base_url}, callback=self.parse)

    def parse(self, response):
        if response.url in response.meta["v_urls"]:
            return
        response.meta["v_urls"].append(response.url)
        if -1 == str(response.url).find(str(response.meta["b_url"])):
            return
        site = response.css('html').extract_first()
        body = parse.html_parse(site)
        block_tree.construct_and_save_tree(body, response.url, response.meta["name"])
        for href in response.css('a::attr(href)').extract():
            new_url = response.urljoin(href)
            yield scrapy.Request(url=new_url, meta={"name": response.meta["name"], "v_urls": response.meta["v_urls"], "b_url": response.meta["b_url"]}, callback=self.parse)


###############################################################
#################BELLOW ARE DIRECT SPIDERS#####################
###############################################################


#CATEGORY MUSIC
#IN-UNSE
class lastFmSpider(scrapy.Spider):
    name = "lastFM"
    start_urls = [
        'http://www.last.fm/api',
    ]

    def parse(self, response):
        for div in response.css('div.package'):
            for href in div.css('a::attr(href)').extract():
                yield scrapy.Request(response.urljoin(href), callback=self.parse_request)

    def parse_request(self, response):
        article = response.css('article.g9')
        
        name = article.css('h1::text').extract_first()
        description = article.css('div.wsdescription::text').extract_first().replace('\n', ' ').strip()
        
        urls = article.css('p.sampleurl a::attr(href)').extract()
        if [] == urls:  url = "http://ws.audioscrobbler.com/2.0/"
        else:           url = urls[1]
        
        splited_params = article.css('div#wsdescriptor').extract_first().split('<h2>Params</h2>')[1].split('<h2>')[0].split('<span class=\"param\">')
        
        required_params = []
        optional_params = []
        
        for index in range(1, len(splited_params)):
            splited_param = splited_params[index].replace('(unless mbid)]', ')')
            param_name = splited_param.split('</span> (')[0]
            param_flag = splited_param.split('</span> (')[1].split(') : ')[0]
            param_dscp = splited_param.split('</span> (')[1].split(') : ')[1].split('<br>')[0]
            if 1 < len(param_dscp.split("<a")):
                tmp = param_dscp.split("<a")[0] + param_dscp.split("\">")[1].split("</a>")[0] + param_dscp.split("</a>")[1]
                param_dscp = tmp
            param_dscp = param_dscp.replace("/n", "").strip()
            
            param = dict()
            param["ParamName"] = param_name
            param["ParamDescription"] = param_dscp

            if "Required" == param_flag:    required_params.append(param)
            else:                           optional_params.append(param)

        yield {
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url
        }
#IN-USE
class eventfulSpider(scrapy.Spider):
    name = "eventful"
    start_urls = [
        'http://api.eventful.com/docs',
    ]

    def parse(self, response):
        all_api = response.css('div#main').extract_first().split('<h2>All API Methods</h2>')[1].split('<dt><a href=\"')
        for index in range(1, len(all_api)):
            href = all_api[index].split('\"')[0]
            description = all_api[index].split('<dd>')[1].split('</dd>')[0]
            yield scrapy.Request(response.urljoin(href), meta={"description": description}, callback=self.parse_request)

    def parse_request(self, response):
        name = response.css('div#methodmain h1.first::text').extract_first().split("Method ")[1]
        description = response.meta["description"]

        urls = response.css('p.box::text').extract()
        if None == urls:    url = "http://api.eventful.com/rest/"
        else:
            url = ""
            for index in range(0, len(urls)):
                url += urls[index]
            url = url.replace("\n", "").strip()

        splited_params = response.css('dl').extract_first().split("</dd>")

        required_params = []
        optional_params = []

        for index in range(0, len(splited_params)):
            splited_param = splited_params[index].replace("\n", "").replace("\t", "").replace("\r", "").strip()
            if 2 > len(splited_param.split("<dt>")) or 2 > len(splited_param.split("<dd>")):
                continue
            param_name = splited_param.split("<dt>")[1].split("<")[0].replace(" ", "")
            if 1 < len(splited_param.split("<a")):
                a_splited_param = splited_param.split("<a")
                param_dscp = a_splited_param[0].split("<dd>")[1]
                for a_index in range(1, len(a_splited_param)-1):
                    param_dscp += a_splited_param[a_index].split("\">")[1].split("</a>")[0] + a_splited_param[a_index].split("</a>")[1]
                param_dscp += a_splited_param[len(a_splited_param)-1].split("\">")[1].split("</a>")[0] + a_splited_param[len(a_splited_param)-1].split("</a>")[1].split("<")[0]
            else:   param_dscp = splited_param.split("<dd>")[1].split("<")[0]

            param = dict()
            param["ParamName"] = param_name
            param["ParamDescription"] = param_dscp

            if 1 < len(splited_param.split("<strong>")):
                if "optional" in splited_param.split("<strong>")[1]:
                    optional_params.append(param)
                else:
                    required_params.append(param)
            else:
                required_params.append(param)

        yield {
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url
        }
#UNUSED
class soundCloudSpider(scrapy.Spider):
    name = "soundCloud"
    start_urls = [
        "https://developers.soundcloud.com/docs/api/reference",
    ]

    def parse(self, response):
        yield {
            "this": response
        }
        # contents = response.css('section#content').extract_first().split("<h2")
        # for index in range(1, len(contents)):
        #     content = contents[index]
        #     name = content.split(">")[1].split("</h2>")[0]
        #     url = "https://soundcloud.com" + name
        #     descriptions = content.split("</p>")
        #     description = ""
        #     for index in range(0, len(descriptions)):
        #         description += description[index].split("<p>")[1]
        #     yield {
        #         "ServiceName": name,
        #         "ServiceDescription": description,
        #         # "RequiredParams": required_params,
        #         # "OptionalParams": optional_params,
        #         "Url": url
        #     }
#IN-USE
class roviSpider(scrapy.Spider):
    name = "rovi"
    start_urls = [
        "http://prod-doc.rovicorp.com/mashery/index.php/Data/Music-API/V1.1",
        "http://prod-doc.rovicorp.com/mashery/index.php/Data/Name-API/V1.1",
        "http://prod-doc.rovicorp.com/mashery/index.php/Data/Descriptor-API/V1.1"
    ]

    def parse(self, response):
        for tr in response.css('div#mw_contentholder tr'):
            href = tr.css('a::attr(href)').extract_first()
            name = tr.css('a::text').extract_first()
            descriptions = tr.css('td::text').extract()
            description = descriptions[len(descriptions)-1]
            yield scrapy.Request(response.urljoin(href), meta={"name": name, "description": description}, callback=self.parse_request)

    def parse_request(self, response):
        name = response.meta["name"]
        description = response.meta["description"]
        url = "http://api.rovicorp.com/data/v1.1/"
        urls = response.css('div.APIsyntax td').extract()
        if 1 < len(urls):
            url += urls[0].replace(" ", "").split("\">")[1].split("</td>")[0]
            for index in range(1, len(urls)):
                if ( index == len(urls)-1 ) and ( "&" != urls[len(urls)-1][0] ):
                    url += "&amp;"
                url += urls[index].replace(" ", "").replace("</b><br>", "|").replace("<b>", "").split("\">")[1].split("</")[0]
        else:
            url += response.css('p.APIsyntaxHanging').extract_first().replace(" ", "").replace("<b>", "").replace("</b>", "").split("\">")[1].split("</p>")[0]        

        table = response.css('table.sortable').extract_first()
        tmp = table.strip().replace("\n", "")
        if 2 < len(tmp.split("<table>")):
            tmp1 = tmp.split("<table>")[1]
            for index in range(1, len(tmp.split("</table>"))-2):
                tmp1 += tmp.split("</table>")[index].split("<table>")[0]
            tmp1 += tmp.split("</table>")[len(tmp.split("</table"))-2]
            tmp = tmp1
        trs = tmp.split("</tr><tr>")

        required_params = []
        optional_params = []

        for index in range(1, len(trs)-1):
            tds = trs[index].split("</td>")
            if 3 < len(tds):    
                param_name = tds[0].split("<td>")[1]
                param_flag = tds[len(tds)-3].split(">")[1]
                if 1 < len(tds[len(tds)-2].split("<td>")):
                    param_dscp = tds[len(tds)-2].split("<td>")[1].replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").replace("<p>", "").replace("</p>", "")
                else:   param_dscp = ""
                param = dict()
                param["ParamName"] = param_name
                param["ParamDescription"] = param_dscp
                if "Yes" == param_flag: required_params.append(param)
                else:                   optional_params.append(param)

        yield {
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url
        }

#CATEGORY NEWSPAPER
#IN-USE
class redditSpider(scrapy.Spider):
    name = "reddit"
    start_urls = [
        'https://www.reddit.com/dev/api'
    ]

    def parse(self, response):
        all_api = response.css('div.endpoint').extract()
        for api in all_api:
            api = api.replace("\n", "")
            name = api.split("</span>")[1].replace("<em class=\"placeholder\">", "").replace("</em>", "").split("<")[0]
            url = "https://www.reddit.com" + name
            if 1 < len(api.split("md\"><p>")):
                description = api.split("md\"><p>")[1].split("</p>")[0].replace("<em>", "").replace("</em>", "")
            else:
                description = ""
            if 1 < len(api.split("<table class=\"parameters\">")):
                params = api.split("<table class=\"parameters\">")[1].split("</table>")[0]
                if 1 < len(params.split("json-model")) or 1 < len(params.split("</code><br")):
                    params = ""
            else:   params = ""

            required_params = []
            optional_params = []
            all_param = []
            
            if "" != params:
                splited_params = params.split("</td>")
                if 1 < len(splited_params):
                    for index in range(0, len(splited_params)-1):
                        splited_param = splited_params[index]
                        param_name = splited_param.split("<th scope=\"row\">")[1].split("</th>")[0]
                        if 0 < splited_param.find("<p>"):
                            param_dscp = splited_param.split("<p>")[1].split("</p>")[0]
                        else:   param_dscp = ""
                        param = dict()
                        param["ParamName"] = param_name
                        param["ParamDescription"] = param_dscp

                        if param_dscp.find("optional") == -1:
                            required_params.append(param)
                        else:
                            optional_params.append(param)

            yield {
                "ServiceName": name,
                "ServiceDescription": description,
                # "params": all_param,
                "RequiredParams": required_params,
                "OptionalParams": optional_params,
                "Url": url
            }
#UNUSED
class hackerSpider(scrapy.Spider):
    name = "hacker"
    start_urls = [
        "http://hndroidapi.appspot.com/"
    ]

    def parse(self, response):
        main = response.css('div#main').extract_first().replace("\n", "").split("<h2>")
        for index in range(2, len(main)):
            splited_param = main[index]
            name = splited_param.split("</h2>")[0]
            description = splited_param.split("<fieldset>")[1].split("<br />")[0]
            params = splited_param.split("<table>")[1].split("</table>")[0]
            yield {
                "name": name,
                "description": description,
                "params": params
            }
#UNUSED
class yelpSpider(scrapy.Spider):
    name = "yelp"
    start_urls = [
        "https://www.yelp.com/developers/documentation/v3",
    ]

    def parse(self, response):
        for unit in response.css('div.arrange_unit'):
            href = unit.css('a::attr(href)').extract_first()
            name = unit.css('a::text').extract_first()
            description = unit.css('p::text').extract_first()
            # href = unit.split("href=\"")[1].split("\">")[0]
            # name = unit.split("\">")[1].split("</a>")[0]
            # description = unit.split("<p>")[1].split("</p>")[0]
            yield scrapy.Request(response.urljoin(href), meta={"name": name, "description": description}, callback=self.parse_request)

    def parse_request(self, response):
        name = meta["name"]
        description = meta["description"]
        yield {
            "ServiceName": name,
            "ServiceDescription": description,
        }
        # div = response.css('div.column-beta').extract_first().replace("\n", "")
        # detailed_description = div.split("</h1><p>")[1].split("<div")[0]
        # url = div.split("<pre>")[1].split("</pre>")[0]

#UNUSED
class payPalSpider(scrapy.Spider):
    name = "paypal"
    start_urls = [
        "https://developer.paypal.com/docs/api/",
    ]

    def parse(self, response):
        for dax in response.css('div.dax-api'):
            href = dax.css('h2 a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(href), callback=self.parse_request)

    # def parse_request(self, response):

#TODO 
class rezgoSpider(scrapy.Spider):
    name = "rezgo"
    start_urls = [
        'https://www.rezgo.com/api-documentation/'
    ]

    def parse(self, response):
        divs = response.css('div.pado-section-enter')
        div = divs[2]
        name = div.css('h2.pado-section-heading::text').extract_first()
        contents = div.css('article.document')
        description = contents[0].css('div.document-content p::text').extract_first()
        params = contents[1].css('div.document-content table tbody')
        required_params = []
        optional_params = []
        for tr in params.css('tr'):
            param = dict()
            tds = tr.css('td::text')
            param["ParamName"] = tds[0]
            param["ParamDescription"] = tds[1]
            if tds[1].find("Required") > 0:
                required_params.append(param)
            else:
                optional_params.append(param)
          

#CATEGORY EDUCATION
#IN-USE
class greatSchoolsSpider(scrapy.Spider):
    name = "greatSchools"
    start_urls = [
        'http://www.greatschools.org/api/docs/main.page'
    ]

    def parse(self, response):
        for request in response.css('div.call div.mainRequest'):
            href = request.css('a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(href), callback=self.parse_request)

    def parse_request(self, response):
        name = response.css('div.content div.callfirst h2::text').extract_first()
        description = response.css('div.content div.callfirst').extract_first().replace("\n", "").split("</h2>")[1].split("<div")[0]
        url = response.css('div.content div.callfirst div.sample_url::text').extract_first()
        required_params = []
        optional_params = []
        
        params = response.css('div.content div.call tbody tr')
        for tr in params:
            param = dict()
            param["paramName"] = tr.css('td::text').extract()[0]
            param["paramDescription"] = tr.css('td::text').extract()[1].strip()
            if param["paramName"].find("*") > 0:
                tmp = param["paramName"][:-1]
                param["paramName"] = tmp
                required_params.append(param)
            else:
                optional_params.append(param)
        sample = response.css('div.content div.call textarea.sampleTextArea::text').extract_first()
        yield{
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url,
            "SampleResponse": sample
        }
#TODO
class altmetricSpider(scrapy.Spider):
    name = "altmetric"
    start_urls= [
        'http://api.altmetric.com/docs/call_citations.html'
    ]

    def parse(self, response):
        base_url = "http://api.altmetric.com"
        for href in response.css('header#mainheader nav#mainnav div.inner ul li.active ul.subnav li a::attr(href)').extract():
            url = base_url + href
            yield scrapy.Request(url, callback=self.parse_request)

    def parse_request(self, response):
        name = response.css('div.page-header h1::text').extract_first()
        urls = response.css('div.container div.content section.no_border b').extract_first()
        url = urls.split("<b>")[1].split("</b>")[0].replace("<i>", "").replace("</i>", "")
        description = response.css('div.container div.content section.no_border p::text').extract_first()

        yield {
            "ServiceName": name,
            "Url": url
        }
#IN-USE
class wiziqSpider(scrapy.Spider):
    name = "wiziq"
    start_urls = [
        'http://developer.wiziq.com/documentation'
    ]

    def parse(self, response):
        for href in response.css('div.dv100.martop10 span.left_method a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_request)

    def parse_request(self, response):
        name = ' '.join(response.css('h1 strong::text').extract_first().replace("\n", "").replace("\r", "").split())
        description = ' '.join(response.css('p.martop10::text').extract()[2].replace("\n", "").replace("\r", "").split())
        url = ''.join(response.css('p[style*=color]::text').extract_first().split())
        required_params = []
        optional_params = []
        trs = response.css('tr')
        for index in range(2, len(trs)):
            tr = trs[index].css('td').extract()
            param = dict()
            param["ParamName"] = ' '.join(tr[0].split(">")[2].split("<")[0].split())
            param["ParamDescription"] = ' '.join(tr[2].split(">")[1].split("<")[0].split())
            param_flag = tr[1]
            if param_flag.find("Optional") > 0:
                optional_params.append(param)
            else:
                required_params.append(param)
        sample = response.css('pre::text').extract_first()

        yield {
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url,
            "SampleResponse": sample
        }
#UNUSED
class edxSpider(scrapy.Spider):
    name = "edx"
    start_urls = [
        'http://edx-platform-api.readthedocs.io/en/latest/courses/overview.html',
        'http://edx-platform-api.readthedocs.io/en/latest/enrollment/overview.html',
        'http://edx-platform-api.readthedocs.io/en/latest/user/overview.html'
    ]
#IN-USE
class skyPrepSpider(scrapy.Spider):
    name = "skyprep"
    start_urls = [
        'https://skyprep.com/api'
    ]

    def parse(self, response):
        for method in response.css('div.method-section'):
            name = method.css('div.method-description h3::text').extract_first()
            if None == name:
                continue
            if "Introduction" == name:
                continue
            if "Authentication" == name:
                continue
            description = ' '.join(method.css('div.method-description p::text').extract()).replace("\n","")
            url = method.css('div.method-description code::text').extract_first()
            required_params = []
            optional_params = []

            if not method.css('div.method-description div.info').extract() is None:
                info = method.css('div.method-description div.info')
                for field in info.css('div.field'):
                    param = dict()
                    param["ParamName"] = field.css('div.key::text').extract_first()
                    param["ParamDescription"] = ' '.join(field.css('div.desc::text').extract()).replace("\n", "")
                    param_flag = field.css('div.desc strong::text').extract_first()
                    if param_flag.find("optional") > 0:
                        optional_params.append(param)
                    else:
                        required_params.append(param)
            sample = ' '.join(method.css('div.method-example pre code::text').extract())

            yield {
                "ServiceName": name,
                "ServiceDescription": description,
                "RequiredParams": required_params,
                "OptionalParams": optional_params,
                "Url": url,
                "SampleResponse": sample
            }

#CATEGORY VOICE
#IN-USE
class twilioSpider(scrapy.Spider):
    name = "twilio"
    start_urls = [
        'https://www.twilio.com/docs/api/rest'
    ]

    def parse(self, response):
        for li in response.css('div.primary-column div.docs-prose div.block-markdown div ul li'):
            name = li.css('a::text').extract_first()
            if name.find("Make a Call") < 0:
                href = li.css('a::attr(href)').extract_first()
                yield scrapy.Request(response.urljoin(href), meta={"name": name}, callback=self.parse_request)

    def parse_request(self, response):
        name = response.meta["name"]
        description = response.css('div.block-markdown p::text').extract_first()
        url = "https://www.twilio.com" + response.css('div.block-markdown div pre.notranslate.http-request::text').extract_first().replace("\n", "")
        required_params = []
        optional_params = []
        required_table = response.css('div.block-markdown div table')[0]
        for tr in required_table.css('tbody tr'):
            param = dict()
            param["ParamName"] = tr.css('td::text').extract()[0]
            param["ParamDescription"] = tr.css('td::text').extract()[1]
            required_params.append(param)
        if len(response.css('div.block-markdown div table')) > 1:
            optional_table = response.css('div.block-markdown div table')[1]
            for tr in optional_table.css('tbody tr'):
                param = dict()
                param["ParamName"] = tr.css('td::text').extract()[0]
                param["ParamDescription"] = tr.css('td::text').extract()[1]
                optional_params.append(param)
        sample = ""
        yield {
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url,
            "SampleResponse": sample
        }
#IN-USE
class planetTeamSpeakSpider(scrapy.Spider):
    name = "planet"
    start_urls = [
        'https://www.planetteamspeak.com/rest-api/'
    ]

    def parse(self, response):
        parts = response.css('article.uk-article').extract_first().split("<h2>")
        for index in range(1, len(parts)):
            part = parts[index].replace("\n", "")
            name = part.split("\">")[1].split("<")[0]
            description = part.split("</h2><p>")[1].split("</p")[0]
            url = part.split("de1\">")[1].split("</pre")[0].split(" ")[1]
            codes = part.split("de1\">")[2].split("</pre")[0].split("</span>")
            sample = ' '
            for index in range(0, len(codes)-1):
                sample = sample + codes[index].split("\">")[1]
            required_params = []
            optional_params = []
            if part.find("uk-description-list-line") > 0:
                tables = part.split("uk-description-list-line\">")[1].split("</dl>")[0].split("</dd>")
                for index in range(0, len(tables)-1):
                    table = tables[index]
                    param = dict()
                    param["ParamName"] = table.split("<dt>")[1].split("</dt>")[0]
                    param["ParamDescription"] = table.split("<dd>")[1]
                    if param["ParamDescription"].find("optional") > 0:
                        optional_params.append(param)
                    else:
                        required_params.append(param)
            yield {
                "ServiceName": name,
                "ServiceDescription": description,
                "RequiredParams": required_params,
                "OptionalParams": optional_params,
                "Url": url,
                "SampleResponse": sample
            }

#CATEGORY TRANSPORTATION
#IN-USE
class transicastSpider(scrapy.Spider):
    name = "transicast"
    start_urls = [
        'http://www.transicast.com/documentation.html'
    ]

    def parse(self, response):
        for href in response.css('div#content div.section.first p.lead a::attr(href)').extract():
            if href.find("#json") < 0:
                yield scrapy.Request(response.urljoin(href), callback=self.parse_request)

    def parse_request(self, response):
        name = response.css('div#content div.section.first h2::text').extract_first()
        description = ' '.join(response.css('div#content div.section.first p.lead::text').extract()).replace("\n","").replace("\r", "")
        url = response.css('pre a::text').extract_first()
        samples = response.css('pre').extract()[1]
        sample = samples.split("<pre>")[1].split("</pre>")[0].replace("\n", "")
        required_params = []
        optional_params = []
        tables = response.css('div#content div.section table').extract_first().split("</tr>")
        for index in range(1, len(tables)-1):
            table =tables[index].replace("\n","")
            param = dict()
            param_name = ''
            param_names = table.split("</td>")[0].split(">")
            for p_index in range(0, len(param_names)):
                param_name += param_names[p_index].split("<")[0]
            param["ParamName"] = param_name
            param_dscp = ''
            param_dscps = table.split("</td>")[1].split(">")
            for p_index in range(0, len(param_dscps)):
                param_dscp += param_dscps[p_index].split("<")[0]
            param["ParamDescription"] = param_dscp
            param_flag = table.split("</td>")[2]
            if param_flag.find("center") > 0:
                required_params.append(param)
            else:
                optional_params.append(param)
        yield {
            "ServiceName": name,
            "ServiceDescription": description,
            "RequiredParams": required_params,
            "OptionalParams": optional_params,
            "Url": url,
            "SampleResponse": sample
        }
#UNUSED
class lyftSpider(scrapy.Spider):
    name = "lyft"
    start_urls = [
        'https://developer.lyft.com/docs'
    ]

    def parse(self, response):
        for reference in response.css('div#hub-reference div.hub-reference'):
            name = reference.css('div.hub-reference-section.hub-reference-top div.hub-reference-left h2::text').extract_first()
            descriptions = reference.css('div.hub-reference-section.hub-reference-top div.hub-reference-left div p').extract()
            description = ' '.join(descriptions).replace("<p>", "").replace("</p>", "").replace("<code>", "").replace("</code>","").replace("\n","")
            yield {
                "ServiceName": name,
                "ServiceDescription": description,
                # "RequiredParams": required_params,
                # "OptionalParams": optional_params,
                # "Url": url,
                # "SampleResponse": sample
            }
#UNUSED
class autoScoutSpider(scrapy.Spider):
    name = "autoScout"
    start_urls = [
        'https://autoscout24.github.io/api/'
    ]

    # def parse(self, response):

#CATEGORY DATA
class organicitySpider(scrapy.Spider):
    name = "organicity"
    start_urls = [
        'http://organicityeu.github.io/api/'
    ]

    def parse(self, response):
        for href in response.css('div.container div.api div.row div.apiBlock h2 a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_request)

    def parse_request(self, response):
        for panel in response.css('div.container div.swagger--panel-operation-get.panel'):
            name = panel.css('h3.panel-title strong::text').extract_first()
            url = 'http://discovery.organicity.eu/v0' + name
            description = panel.css('div.panel-body section.sw-operation-description p::text').extract_first()
            params = panel.css('div.panel-body section.sw-request-params table')
            required_params = []
            optional_params = []
            # print len(params)
            if len(params) > 0:
                # print params.extract()
                for tr in params.css('tbody tr'):
                    tds = tr.css('td').extract()
                    param = dict()
                    param["ParamName"] = ' '.join(tds[0].split("<td>")[1].split("</td>")[0].split()).replace("\n", "")
                    param["ParamDescription"] = ' '.join(tds[1].split("<td>")[1].split("</td>")[0].split()).replace("\n", "").replace("<p>", "").replace("</p>", "")                   
                    param_flag = tds[4].split("<td>")[1].split("</td>")[0]
                    if param_flag.find("require") > 0:
                        required_params.append(param)
                    else:
                        optional_params.append(param)
            samples = panel.css('div.panel-body section.sw-responses a.json-schema-ref::attr(href)')
            if len(samples) > 0:
                sample_id = 'http://organicityeu.github.io/api/AssetDiscovery.html' + samples.extract_first()




            yield {
                "ServiceName": name,
                "ServiceDescription": description,
                "RequiredParams": required_params,
                "OptionalParams": optional_params,
                "Url": url,
                "SampleResponse": sample_id
            }
