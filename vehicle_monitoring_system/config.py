import os 
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_HOST = os.environ['POSTGRES_HOST']

RABBIT_EXCHANGE = os.environ["RABBIT_EXCHANGE"]
RABBIT_HOST = os.environ["RABBIT_HOST"]
RABBIT_PORT = os.environ["RABBIT_PORT"]
RABBIT_QUEUE = os.environ["RABBIT_QUEUE"]
RABBIT_ROUTING_KEY = os.environ["RABBIT_ROUTING_KEY"]

ECHO = os.environ['ECHO'] == "True"