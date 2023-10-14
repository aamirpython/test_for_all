from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, status
from fastapi import APIRouter
from mytestapp.pydantic_models import *
from . models import *


from fastapi.responses import JSONResponse
from fastapi_login import LoginManager
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Request, Form
from pathlib import Path
import secrets
from fastapi.staticfiles import StaticFiles
from PIL import Image

from datetime import datetime, timedelta
from slugify import slugify

import typing
import pandas as pd
from typing import List
import re
import psycopg2
from pydantic import BaseModel





router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory=str(
    Path(BASE_DIR, "mytestapp/templates")))
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = 'your-secret-key'
manager = LoginManager(SECRET, token_url='/auth/token')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)




@router.post("/Subjects/")
async def create_category(data: subjects):
    if await Subjects.filter(sub_name=data.sub_name).exists():
        return {"message": "subjects already exists"}
    else:
        category_obj = await Subjects.create(sub_name=data.sub_name, slug=slugify(data.sub_name))

        return {"message": " subjects added"}



@router.post("/store_data")
async def store_data( sname_id: int,file: UploadFile = File(...)):
    
    try:
        df = pd.read_csv(file.file)

        data = df.to_dict(orient="records")
        await Questions.bulk_create([Questions(**item,sname_id=sname_id) for item in data])

        return {"message": "Data stored successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
