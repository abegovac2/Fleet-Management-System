import pika
import config
import ast
from data_access import update_driver_points

result = {}

class RabbitConsumer:

    def __init__(self, queue_name, exchange, routing_key='', exchange_type='direct') -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = config.RABBIT_HOST, 
        port = config.RABBIT_PORT))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)
        self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        self.channel.basic_qos(prefetch_count=1)
        self.is_consuming = False

    
    def set_callback(self, callback_foo):
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=callback_foo,
            )
        if not self.is_consuming: 
            self.channel.start_consuming()
            self.is_consuming = True

def calc_points(speed: float):
    num = int(speed > 60) + int(speed > 80) + int(speed > 100)*3
    return num


def process_message(ch, method, properties, body):
    res = ast.literal_eval(body.decode())
    points = calc_points(res["speed"])
    update_driver_points(res["driver_id"], points)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"""
    driver_id: {res["driver_id"]}
    points: {points}
    speed: {res["speed"]}
    """)



print("Consumer created")

consumer = RabbitConsumer(
    queue_name=config.RABBIT_QUEUE,
    exchange=config.RABBIT_QUEUE,
    routing_key=config.RABBIT_ROUTING_KEY
)

print("Started consuming")

consumer.set_callback(process_message)
    