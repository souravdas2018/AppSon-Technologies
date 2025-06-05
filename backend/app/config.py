# import os

# class Config:
#     SQLALCHEMY_DATABASE_URI = 'postgresql://local_user:##123##@localhost/local_user_db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://local_user:%23%23123%23%23@localhost/local_user_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
