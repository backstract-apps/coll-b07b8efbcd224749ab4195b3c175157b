from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_user_data_id(db: Session, id: int):

    query = db.query(models.UserData)
    query = query.filter(and_(models.UserData.id == id))

    user_data_one = query.first()

    user_data_one = (
        (
            user_data_one.to_dict()
            if hasattr(user_data_one, "to_dict")
            else vars(user_data_one)
        )
        if user_data_one
        else user_data_one
    )

    res = {
        "user_data_one": user_data_one,
    }
    return res


async def post_user_data(db: Session, raw_data: schemas.PostUserData):
    id: int = raw_data.id
    username: str = raw_data.username
    email: str = raw_data.email

    record_to_be_added = {"id": id, "email": email, "username": username}
    new_user_data = models.UserData(**record_to_be_added)
    db.add(new_user_data)
    db.commit()
    db.refresh(new_user_data)
    user_data_inserted_record = new_user_data.to_dict()

    res = {
        "user_data_inserted_record": user_data_inserted_record,
    }
    return res


async def get_user_data(db: Session):

    query = db.query(models.UserData)

    user_data_all = query.all()
    user_data_all = (
        [new_data.to_dict() for new_data in user_data_all]
        if user_data_all
        else user_data_all
    )
    res = {
        "user_data_all": user_data_all,
    }
    return res


async def put_user_data_id(db: Session, raw_data: schemas.PutUserDataId):
    id: int = raw_data.id
    username: str = raw_data.username
    email: str = raw_data.email

    query = db.query(models.UserData)
    query = query.filter(and_(models.UserData.id == id))
    user_data_edited_record = query.first()

    if user_data_edited_record:
        for key, value in {"id": id, "email": email, "username": username}.items():
            setattr(user_data_edited_record, key, value)

        db.commit()
        db.refresh(user_data_edited_record)

        user_data_edited_record = (
            user_data_edited_record.to_dict()
            if hasattr(user_data_edited_record, "to_dict")
            else vars(user_data_edited_record)
        )
    res = {
        "user_data_edited_record": user_data_edited_record,
    }
    return res


async def delete_user_data_id(db: Session, id: int):

    query = db.query(models.UserData)
    query = query.filter(and_(models.UserData.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_data_deleted = record_to_delete.to_dict()
    else:
        user_data_deleted = record_to_delete
    res = {
        "user_data_deleted": user_data_deleted,
    }
    return res


async def post_demo_1(db: Session):

    try:
        charlist = [
            {"name": "Rick Sanchez", "no_of_episodes": 51},
            {"name": "Morty Smith", "no_of_episodes": 51},
            {"name": "Summer Smith", "no_of_episodes": 42},
            {"name": "Beth Smith", "no_of_episodes": 42},
            {"name": "Jerry Smith", "no_of_episodes": 39},
            {"name": "Abadango Cluster Princess", "no_of_episodes": 1},
            {"name": "Abradolf Lincler", "no_of_episodes": 2},
            {"name": "Adjudicator Rick", "no_of_episodes": 1},
            {"name": "Agency Director", "no_of_episodes": 1},
            {"name": "Alan Rails", "no_of_episodes": 1},
            {"name": "Albert Einstein", "no_of_episodes": 1},
            {"name": "Alexander", "no_of_episodes": 1},
            {"name": "Alien Googah", "no_of_episodes": 1},
            {"name": "Alien Morty", "no_of_episodes": 1},
            {"name": "Alien Rick", "no_of_episodes": 1},
            {"name": "Amish Cyborg", "no_of_episodes": 1},
            {"name": "Annie", "no_of_episodes": 1},
            {"name": "Antenna Morty", "no_of_episodes": 2},
            {"name": "Antenna Rick", "no_of_episodes": 1},
            {"name": "Ants in my Eyes Johnson", "no_of_episodes": 1},
        ]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    temp = []  # Creating new list

    temp = charlist

    # Clear all elements from the list 'charlist'
    charlist.clear()
    res = {
        "charlist": charlist,
        "temp": temp,
    }
    return res
