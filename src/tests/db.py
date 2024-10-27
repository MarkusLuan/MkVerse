from models import User
import app_singleton

import datetime

def devera_criar_usuario():
    user = User(
        dt_nascimento=datetime.date(1997, 2, 19),
        nick="markus_luan",
        nome="Markus Luan",
        email="markus@mkgcriacoes.com.br",
        bio="testando",
        senha="1234",
    )

    app_singleton.db.session.add(user)
    app_singleton.db.session.commit()