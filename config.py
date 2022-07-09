import os
from dotenv import load_dotenv

load_dotenv(dotenv_path = ".env")

class Setting:
    TITLE = "Sker"
    VERSION = "0.0.1"
    DESCRIPTION = """
        This is the API for Sker Project
        It is not for production yet
    """
    NAME = "Sker Developers"
    EMAIL = "hanlopb@gmail.com"

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER =os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE","testing")
    POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

setting = Setting()
