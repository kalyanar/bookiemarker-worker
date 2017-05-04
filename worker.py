import pika
import json
from scraper import Scraper


def publish_result(scraping_result):
    j = json.dumps(scraping_result.__dict__)
    properties = pika.BasicProperties(content_type="application/json")


def callback(ch, method, properties, body):
    url = json.loads(body.decode('utf-8'))['url']
    scraper = Scraper()
    result = scraper.scrape(url)

credentials = pika.PlainCredentials("user", "password")
parameters = pika.ConnectionParameters(host='localhost', port=7234, credentials=credentials)

print('[*] Waiting for tasks. To exit press CTRL+C')