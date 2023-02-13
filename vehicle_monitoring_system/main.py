import config
import ast
from data_access import update_driver_points
from rabbit_client import RabbitConsumer, RabbitEnqueuer

def calc_points(speed: float):
    num = int(speed > 60) + int(speed > 80) + int(speed > 100)*3
    return num


enqueuer = RabbitEnqueuer(
    queue_name=config.RMQ_DRIVER_NAME,
    exchange=config.RMQ_DRIVER_EXCHANGE,
    routing_key=config.RMQ_DRIVER_ROUTING_KEY
)

def process_message(ch, method, properties, body):
    res = ast.literal_eval(body.decode())
    points = calc_points(res["speed"])
    update_driver_points(res["driver_id"], points)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
    enqueuer.basic_publish({
        "driver_id": res["driver_id"],
        "points": points
    })

    print(f"""
    driver_id: {res["driver_id"]}
    points: {points}
    speed: {res["speed"]}
    """)



print("Consumer created")

consumer = RabbitConsumer(
    queue_name=config.RMQ_POINTS_NAME,
    exchange=config.RMQ_POINTS_EXCHANGE,
    routing_key=config.RMQ_POINTS_ROUTING_KEY
)

print("Started consuming")

consumer.set_callback(process_message)
    