import peewee
from datetime import datetime

db = peewee.SqliteDatabase('database.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Client(BaseModel):
    addrClient = peewee.TextField(unique=True)
    

class IO(BaseModel):
    fromClient = peewee.ForeignKeyField(Client, backref='io')
    messageReciver = peewee.TextField(default=None)
    messageSender = peewee.TextField(default=None)
    timeReciver = peewee.DateTimeField(default=None)
    timeSender = peewee.DateTimeField(default=None)

class Connections(BaseModel):
    fromClient = peewee.ForeignKeyField(Client, backref='connections')
    timeConnection = peewee.DateTimeField(default=datetime.now())
    timeDisconnection = peewee.DateTimeField(default=datetime.now())
    

try:
    db.create_tables([
        IO,
        Client,
        Connections
    ])
    print("[DATABASE]:\t[OK] ao criar tabela")
except:
    print("[DATABASE]:\t[ERRO] ao criar tabela")

### TEST
try:
    cliente_cliente = Client.create(
        addrClient = "1523sfsasdafssd435"
    )
except:
    cliente_cliente = Client.select().where(Client.addrClient == "1523sfsasdafssd435")

Connections.create(
    fromClient = cliente_cliente   
)
