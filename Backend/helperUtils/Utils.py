"""
Module Name: Utils.py
Author: Arun
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="staticfiles"), name="static")
