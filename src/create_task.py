import json
import pika
import sys
from src.configs.connection import create_channel
from src.configs.queue import QueueName

channel = create_channel()


def create_task(task):
    channel.basic_publish(
        exchange='',
        routing_key=QueueName.task_queue,
        body=json.dumps(task),
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent,
        )
    )
    print(f"Task {task_name} created")
    channel.close()


task_name = sys.argv[1]

task = {
    'id': task_name,
    'type': 'edit_picture',
    'file': 'path/to/file.jpg',
    'status': 'new'
}

create_task(task)
