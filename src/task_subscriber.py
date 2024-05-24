import json
from src.configs.connection import create_channel
from src.configs.queue import QueueName


channel = create_channel()


def new_task_callback(ch, method, properties, body):
    task = json.loads(body)
    print(f"New task: {task['id']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=QueueName.task_queue,
                      on_message_callback=new_task_callback)

print('Waiting for new tasks. To exit press CTRL+C')

channel.start_consuming()
