from data_access.database import SessionLocal
from data_access.models import Driver
from rabbit_client import RabbitConsumer
import ast

def update_driver_points_db(driver_id: int, points: int):
    with SessionLocal() as db:
        driver = db.query(Driver).filter(Driver.id == driver_id).first()  
        driver.points += points
        db.commit()

def process_message(ch, method, properties, body):
    res = ast.literal_eval(body.decode())
    update_driver_points_db(res["driver_id"], res["points"])
    ch.basic_ack(delivery_tag=method.delivery_tag) 


def update_driver_points(queue_name, exchange, routing_key):
    consumer = RabbitConsumer(
        queue_name=queue_name,
        exchange=exchange,
        routing_key=routing_key
    )

    consumer.set_callback(process_message)
    pass