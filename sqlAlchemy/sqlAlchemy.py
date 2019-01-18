from sqlalchemy import Column,String,create_engine
from sqlAlchemy.orm import sessionmaker
from sqlAlchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key = Ture)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/test')
DBSession = sessionmaker(bind = engine)
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()