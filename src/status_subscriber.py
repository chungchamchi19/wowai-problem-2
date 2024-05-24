import json
from src.configs.connection import create_channel
from src.configs.queue import ExchangeName


channel = create_channel()

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange=ExchangeName.status_exchange,
                   queue=queue_name)


def view_task_callback(ch, method, properties, body):
    task = json.loads(body)
    print(f"\n\nTask {task['id']} is {task['status']}")
    if task['status'] == 'in_progress':
        print(f"Only {task['person']} can edit this task, others can view it")
    else:
        print('This task is open for editing by anyone')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name,
                      on_message_callback=view_task_callback)

print('Waiting for status updates. To exit press CTRL+C')
channel.start_consuming()
