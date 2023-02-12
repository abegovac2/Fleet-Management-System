import os 
from dotenv import load_dotenv

load_dotenv()

RABBIT_EXCHANGE = os.environ["RABBIT_EXCHANGE"]
RABBIT_HOST = os.environ["RABBIT_HOST"]
RABBIT_PORT = os.environ["RABBIT_PORT"]
RABBIT_QUEUE = os.environ["RABBIT_QUEUE"]
RABBIT_ROUTING_KEY = os.environ["RABBIT_ROUTING_KEY"]

MANAGEMENT_SERVICE = f"http://{os.environ['MANAGEMENT_HOST']}:{os.environ['MANAGEMENT_PORT']}/api/v1"

APP_PORT = int(os.environ['GPS_SIMULATOR_PORT'])