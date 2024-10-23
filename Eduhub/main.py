from fastapi import FastAPI
from database import get_db
from model import User,Exam,Course,Enrollment,Application,Job


app=FastAPI()