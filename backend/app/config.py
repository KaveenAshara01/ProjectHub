import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    #use this DB URI for local development
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

   #use this DB URI for Docker Compose
   # SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:rootpass@db/projecthub"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")
