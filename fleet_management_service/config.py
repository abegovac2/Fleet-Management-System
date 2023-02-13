import os 
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_HOST = os.environ['POSTGRES_HOST']

RMQ_DRIVER_EXCHANGE= os.environ["RMQ_DRIVER_EXCHANGE"]
RMQ_DRIVER_NAME= os.environ["RMQ_DRIVER_NAME"]
RMQ_DRIVER_ROUTING_KEY= os.environ["RMQ_DRIVER_ROUTING_KEY"]

RMQ_HOST= os.environ["RMQ_HOST"]
RMQ_PORT= os.environ["RMQ_PORT"]

ECHO = os.environ['ECHO'] == "True"

APP_PORT = int(os.environ['MANAGEMENT_PORT'])