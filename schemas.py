from pydantic import BaseModel, Field, HttpUrl
from typing import Union
from typing import List


class Cards(BaseModel):
    c_id: int
    c_name: str
    c_invest: int = Field(gt=0, description="The price must be greater than zero")
    c_desc: Union[str, None] = Field(
        default=None, title="The Strategy Idea of the Cards ", max_length=700)
    selected: bool = False
    unselected: bool = True

class Products(BaseModel):
    p_id: int
    p_name: str
    p_invest: int = Field(gt=0, description="The price must be greater than zero")
    p_desc: Union[str, None] = Field(
        default=None, title="The Products related to Strategy Cards", max_length=700)
    selected: bool = False
    unselected: bool = True

class Flags(BaseModel):
    f_id: int
    f_name: str
    f_invest: int = Field(gt=0, description="The price must be greater than zero")
    f_desc: Union[str, None] = Field(
        default=None, title="The Flags Investment in Store, Agent, and Online ", max_length=700)
    selected: bool = False
    unselected: bool = False

class CustServit(BaseModel):
    ci_id: int
    it_low: bool
    serv_low: bool
    it_med: bool
    serv_med: bool
    it_high: bool
    serv_high: bool
    it_invest: int = Field(gt=0, description="The price must be greater than zero")
    serv_invest: int = Field(gt=0, description="The price must be greater than zero")

class ProductLaunch(BaseModel):
    pl_id = int
    s_id = int
    a_id = int
    o_id = int
    s_name = str
    a_name = str
    o_name = str
    s_invest = int
    a_invest = int
    o_invest = int
    s_one_selected = bool
    s_two_selected = bool
    a_one_selected = bool
    a_two_selected = bool
    o_one_selected = bool
    o_two_selected = bool

    class Config:
        orm_mode = True