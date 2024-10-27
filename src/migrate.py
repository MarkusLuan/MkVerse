import app
import app_singleton
from models import *

import sys
import argparse

# db = app_singleton.db
# migrate = app_singleton.migrate

# paser = argparse.ArgumentParser(exit_on_error=False)
# paser.add_argument("--config", default="config.development")

# config_object = paser.parse_known_args()[0]
config_object = sys.argv[1] if len(sys.argv) > 1 else 'config.development'
app = app.create_app(config_object)

with app.app_context():
    app_singleton.db.drop_all()
    app_singleton.db.create_all()