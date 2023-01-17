from fastapi import FastAPI, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import JSON
import schemas
import models
import database
from typing import Union
from models import Cards, Products, Flags, CustServit, ProductLaunch
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




app = FastAPI()


################ View Only ##################
# To view All Data
@app.get("/cards")
def getCards(db: Session = Depends(get_database_session)):
    cards = db.query(models.Cards).all()
    return cards

@app.get("/products")
def getProducts(db: Session = Depends(get_database_session)):
    products = db.query(models.Products).all()
    return products

@app.get("/flags")
def getFlags(db: Session = Depends(get_database_session)):
    flags = db.query(models.Flags).all()
    return flags

@app.get("/custservit")
def getCustServit(db: Session = Depends(get_database_session)):
    custservit = db.query(models.CustServit).all()
    return custservit

@app.get("/productlaunch")
def getProductLaunch(db: Session = Depends(get_database_session)):
    productlaunch = db.query(models.ProductLaunch).all()
    return productlaunch

####################### View by specific ID ########

# To View Specific Id's Data
@app.get("/cards/{c_id}")
async def read_cards(c_id: int, db: Session = Depends(get_database_session)):
    cards = db.query(models.Cards).get(c_id)
    return cards

@app.get("/products/{p_id}")
async def read_products(p_id: int, db: Session = Depends(get_database_session)):
    products = db.query(models.Products).get(p_id)
    return products

@app.get("/flags/{f_id}")
async def read_flags(f_id: int, db: Session = Depends(get_database_session)):
    flags = db.query(models.Flags).get(f_id)
    return flags

@app.get("/custservit/{ci_id}")
async def read_custservit(ci_id: int, db: Session = Depends(get_database_session)):
    custservit = db.query(models.CustServit).get(ci_id)
    return custservit

@app.get("/productlaunch/{pl_id}")
async def read_productlaunch(pl_id: int, db: Session = Depends(get_database_session)):
    productlaunch = db.query(models.ProductLaunch).get(pl_id)
    return productlaunch

##################### Create a data ################

#To Post/Create New Data
@app.post("/cards")
async def create_cards(c_id: int, c_name: str, c_invest: int, c_desc: str, selected: bool, db: Session = Depends(get_database_session)):
    cards = Cards(c_id=c_id, c_name=c_name, c_invest=c_invest, c_desc=c_desc, selected=selected)
    db.add(cards)
    db.commit()

@app.post("/products")
async def create_products(p_id: int, p_name: str, p_invest: int, p_desc: str, selected: bool, db: Session = Depends(get_database_session)):
    products = Products(p_id=p_id, p_name=p_name, p_invest=p_invest, p_desc=p_desc, selected=selected)
    db.add(products)
    db.commit()

@app.post("/flags")
async def create_flags(f_id: int, f_name: str, f_invest: int, f_desc: str, selected: bool, db: Session = Depends(get_database_session)):
    flags = Flags(f_id=f_id, f_name=f_name, f_invest=f_invest, f_desc=f_desc, selected=selected)
    db.add(flags)
    db.commit()

@app.post("/custservit")
async def create_custservit(ci_id: int, it_low: bool, it_med: bool, it_high: bool, serv_low: bool, serv_med: bool, serv_high: bool, it_invest: int,serv_invest: int, db: Session = Depends(get_database_session)):
    custservit = CustServit(ci_id=ci_id, it_low=it_low, it_med=it_med, it_high=it_high, serv_low=serv_low, serv_med=serv_med, serv_high=serv_high, it_invest=it_invest,serv_invest=serv_invest)
    db.add(custservit)
    db.commit()
    
@app.post("/productlaunch")
async def create_productlaunch(pl_id: int, s_id: int,a_id: int,o_id: int,s_name: str,a_name: str,o_name: str,s_invest:int,a_invest:int,o_invest:int,s_one_selected: bool,s_two_selected: bool,a_one_selected: bool,a_two_selected: bool,o_one_selected: bool,o_two_selected: bool, db: Session = Depends(get_database_session)):
    productlaunch = ProductLaunch(pl_id=pl_id,s_id=s_id,a_id=a_id,o_id=o_id,s_name=s_name,a_name=a_name,o_name=o_name,s_invest=s_invest,a_invest=a_invest,o_invest=o_invest,s_one_selected=s_one_selected,s_two_selected=s_two_selected,a_one_selected=a_one_selected,a_two_selected=a_two_selected,o_one_selected=o_one_selected,o_two_selected=o_two_selected)
    db.add(productlaunch)
    db.commit()

####################### Delete by ID ################

#To Delete the data by id
@app.delete("/cards/{c_id}")
async def delete_cards(c_id: int, db: Session = Depends(get_database_session)):
    cards = db.query(Cards).get(c_id)
    db.delete(cards)
    db.commit()

@app.delete("/products/{p_id}")
async def delete_products(p_id: int, db: Session = Depends(get_database_session)):
    products = db.query(Products).get(p_id)
    db.delete(products)
    db.commit()

@app.delete("/flags/{f_id}")
async def delete_flags(f_id: int, db: Session = Depends(get_database_session)):
    flags = db.query(Flags).get(f_id)
    db.delete(flags)
    db.commit()

@app.delete("/custservit/{ci_id}")
async def delete_custservit(ci_id: int, db: Session = Depends(get_database_session)):
    custservit = db.query(CustServit).get(ci_id)
    db.delete(custservit)
    db.commit()

@app.delete("/productlaunch/{pl_id}")
async def delete_productlaunch(pl_id: int, db: Session = Depends(get_database_session)):
    productlaunch = db.query(ProductLaunch).get(pl_id)
    db.delete(productlaunch)
    db.commit()

####################### Update data By Id #################

#To update The data by id
@app.put("/cards/{c_id}")
async def cards(c_id: int, request:schemas.Cards, db:Session=Depends(get_database_session)):
    cards = db.query(models.Cards).filter(models.Cards.c_id == c_id)
    if not Cards.c_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'old_account with the id {c_id} is not available')
    cards = db.query(Cards.c_id == c_id)
    db.add(cards)
    db.commit()
    return {"code":"success","message":"card updated successfully"}
