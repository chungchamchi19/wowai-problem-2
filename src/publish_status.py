import json
import pika
import sys
from src.configs.connection import create_channel
from src.configs.queue import ExchangeName

channel = create_channel()


def assign_task(status):
    channel.basic_publish(
        exchange=ExchangeName.status_exchange,
        routing_key='',
        body=json.dumps(status),
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent,
        )
    )
    print(f"Task {task_id} assigned to {person} with status {status}")
    channel.close()


task_id = sys.argv[1]
person = sys.argv[2]
status = sys.argv[3]

assert status in ['new', 'in_progress', 'completed'], 'Invalid status'

task = {
    'id': task_id,
    'person': person,
    'status': status
}

assign_task(task)

