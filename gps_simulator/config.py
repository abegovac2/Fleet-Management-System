import os 
from dotenv import load_dotenv

load_dotenv()

RMQ_POINTS_EXCHANGE= os.environ["RMQ_POINTS_EXCHANGE"]
RMQ_POINTS_NAME= os.environ["RMQ_POINTS_NAME"]
RMQ_POINTS_ROUTING_KEY= os.environ["RMQ_POINTS_ROUTING_KEY"]

RMQ_HOST= os.environ["RMQ_HOST"]
RMQ_PORT= os.environ["RMQ_PORT"]

MANAGEMENT_SERVICE = f"http://{os.environ['MANAGEMENT_HOST']}:{os.environ['MANAGEMENT_PORT']}/api/v1"

APP_PORT = int(os.environ['GPS_SIMULATOR_PORT'])