from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/user_data/id')
async def get_user_data_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_data_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_data/')
async def post_user_data(raw_data: schemas.PostUserData, db: Session = Depends(get_db)):
    try:
        return await service.post_user_data(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_data/')
async def get_user_data(db: Session = Depends(get_db)):
    try:
        return await service.get_user_data(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_data/id/')
async def put_user_data_id(raw_data: schemas.PutUserDataId, db: Session = Depends(get_db)):
    try:
        return await service.put_user_data_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_data/id')
async def delete_user_data_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_data_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/demo-1')
async def post_demo_1(db: Session = Depends(get_db)):
    try:
        return await service.post_demo_1(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

