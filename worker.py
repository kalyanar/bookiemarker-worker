import pika
import json
from scraper import Scraper


def publish_result(scraping_result):
    j = json.dumps(scraping_result.__dict__)
    properties = pika.BasicProperties(content_type="application/json")
    channel.basic_publish(exchange='', routing_key='scrapingresult.queue', body=j, properties=properties)

def callback(ch, method, properties, body):
    url = json.loads(body.decode('utf-8'))['url']
    scraper = Scraper()
    result = scraper.scrape(url)
    publish_result(result)

credentials = pika.PlainCredentials("user", "password")
parameters = pika.ConnectionParameters(host='localhost', port=7234, credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

tasks_queue = channel.queue_declare(queue='tasks.queue', durable=True)
scraping_result_queue = channel.queue_declare(queue='scrapingresult.queue', durable=True)

channel.basic_consume(callback, queue='tasks.queue')
channel.start_consuming()

print('[*] Waiting for tasks. To exit press CTRL+C')