import os
from dotenv import load_dotenv

load_dotenv()

IMANAGE_HOSTNAME = os.getenv("IMANAGE_HOSTNAME")

CLIENT_ID = os.getenv("IMANAGE_CLIENT_ID")
CLIENT_SECRET = os.getenv("IMANAGE_CLIENT_SECRET")

SERVICE_USERNAME = os.getenv("IMANAGE_USERNAME")
SERVICE_PASSWORD = os.getenv("IMANAGE_PASSWORD")

CUSTOMER_ID = os.getenv("IMANAGE_CUSTOMER_ID")
LIBRARY_ID = os.getenv("IMANAGE_LIBRARY_ID")
