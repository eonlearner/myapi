from sqlalchemy.schema import Column
from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.types import String, Integer, Text
from schemas import Union, List
from database import Base
from sqlalchemy.orm import relationship


class Cards(Base):
    __tablename__ = "Cards"
    c_id = Column(Integer, primary_key=True, index=True)
    c_name = Column(String(20), unique=True)
    c_invest = Column(Integer)
    c_desc = Column(Text())
    selected = Column(Boolean, default=False)
    
class Products(Base):
    __tablename__ = "Products"
    p_id = Column(Integer, primary_key=True, index=True)
    p_name = Column(String(20), unique=True)
    p_invest = Column(Integer)
    p_desc = Column(Text())
    selected = Column(Boolean, default=False)


class Flags(Base):
    __tablename__ = "Flags"
    f_id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String(20), unique=True)
    f_invest = Column(Integer)
    f_desc = Column(Text())
    selected = Column(Boolean, default=False)

class CustServit(Base):
    __tablename__ = "CustServit"
    ci_id = Column(Integer, primary_key=True, index=True)
    it_low = Column(Boolean, default=False)
    serv_low = Column(Boolean, default=False)
    it_med = Column(Boolean, default=False)
    serv_med = Column(Boolean, default=False)
    it_high = Column(Boolean, default=False)
    serv_high = Column(Boolean, default=False)
    it_invest = Column(Integer)
    serv_invest = Column(Integer)

class ProductLaunch(Base):
    __tablename__ = "ProductLaunch"
    __table_args__= {
        'mysql_engine':'InnoDB'
    }
    pl_id = Column(Integer, primary_key=True, index=True)
    s_id = Column(Integer, ForeignKey("Products.p_id", ondelete="CASCADE"), nullable=False)
    a_id = Column(Integer, ForeignKey("Products.p_id", ondelete="CASCADE"), nullable=False)
    o_id = Column(Integer, ForeignKey("Products.p_id", ondelete="CASCADE"), nullable=False)
    s_name = Column(String(20))
    a_name = Column(String(20))
    o_name = Column(String(20))
    s_invest = Column(Integer)
    a_invest = Column(Integer)
    o_invest = Column(Integer)
    s_one_selected = Column(Boolean, default=False)
    s_two_selected = Column(Boolean, default=False)
    a_one_selected = Column(Boolean, default=False)
    a_two_selected = Column(Boolean, default=False)
    o_one_selected = Column(Boolean, default=False)
    o_two_selected = Column(Boolean, default=False)


