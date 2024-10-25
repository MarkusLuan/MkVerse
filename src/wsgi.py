import os
import sys

PROJECT_DIR = "/app"

sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)

from app import app as application
