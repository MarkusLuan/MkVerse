import app
import app_singleton
import models

import argparse

db = app_singleton.db
migrate = app_singleton.migrate

paser = argparse.ArgumentParser(exit_on_error=False)
paser.add_argument("--config", default="config.development")

config_object = paser.parse_known_args()[0]
app = app.create_app("config.development")