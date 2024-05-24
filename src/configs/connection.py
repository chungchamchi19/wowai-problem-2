import pika
from src.configs.queue import ExchangeName, QueueName

def create_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QueueName.task_queue, durable=True)
    channel.exchange_declare(exchange=ExchangeName.status_exchange, exchange_type='fanout')
    return channel
