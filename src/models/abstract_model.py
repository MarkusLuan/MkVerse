from sqlalchemy import BigInteger, Uuid, DateTime, sql

from app_singleton import db

import uuid

class AbstractModel (db.Model):
    __abstract__ = True
    fields = []
    
    id = db.Column(BigInteger, primary_key=True)
    uuid = db.Column(Uuid, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    dt_criacao = db.Column(DateTime, default=sql.func.now(), nullable=False)

    def to_json(self):
        """ Serializer temporário
           * Não encontrei a implementação do Serializer do SQLAlchemy e nem FlaskREST
           * e o do Marshmellow (acho que é assim que se escreve) é horrivel de se fazer.
           * Aí como está acabando o tempo, vou usar desta forma que embora não seja abstrata, é bem prática de se fazer.
        """

        j = {
            "uuid": str(self.uuid),
            "dt_criacao": self.dt_criacao.isoformat()
        }

        j.update({field: self.__getattribute__(field) for field in self.fields})

        return j