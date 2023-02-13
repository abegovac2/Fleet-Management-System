import config
import pika

class RabbitConsumer:
    def __init__(self, queue_name, exchange, routing_key='', exchange_type='direct') -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host = config.RMQ_HOST, 
                port = config.RMQ_PORT
            )
        )

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


class RabbitEnqueuer:
    def __init__(self, queue_name, exchange, routing_key='', exchange_type='direct') -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host = config.RMQ_HOST, 
                port = config.RMQ_PORT
            )
        )

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)
        self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key

    
    def __del__(self):
        self.connection.close()
    
    
    def basic_publish(self, body):
        print("body", body)
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=str(body)
        )