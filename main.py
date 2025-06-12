from core.client import app
from core.loader import load_modules
import logging_config

load_modules()
app.run()
