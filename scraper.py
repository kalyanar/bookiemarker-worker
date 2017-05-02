from newspaper import Article

class ScrapingResult:
    def __init__(self):
        self.url = None
        self.summary = None
        self.title = None
        self.thumbnail = None


class Scraper:
    def scrape(self, url):
        scraping_result = ScrapingResult()
        scraping_result.url = url
        a = Article(url)
        try:
            print("Parsing %s... " % url)
        except Exception as e:
            scraping_result.summary = "Could not scrape summary. Reason: %s" % e

        print("Done: %s = title: %s | thumb: %s | summary: %s" %
              (url, scraping_result.title, scraping_result.thumbnail,
               scraping_result.summary))

        return scraping_result
