from email.policy import default
from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

    #  - id: PK
    # - name: string
    # - description: string
    # - soft_deleted: Boolean
    # - client: Client
    # - qr: string

class Menu(db.Model):
    __tablename__ = 'menu'
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(50), nullable=True)
    __description = db.Column('description', db.String(50), nullable=True)
    __soft_deleted = db.Column('soft_deleted', db.Boolean, default=False, nullable=True)
    __qr = db.Column('qr', db.String(100), nullable=True)




