from sqlalchemy import MetaData, Integer, ForeignKey, Table, Column, String, Float


metadata = MetaData()


menu = Table(
    "menu",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('description', String, nullable=False),
)


submenu = Table(
    "submenu",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('description', String, nullable=False),
    Column('submenu', Integer, ForeignKey("menu.id", ondelete='CASCADE'), unique=True)
)


dish = Table(
    "dish",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('description', String, nullable=False),
    Column('price', Float, nullable=False),
    Column('submenu', Integer, ForeignKey("submenu.id", ondelete='CASCADE'), unique=True)
)