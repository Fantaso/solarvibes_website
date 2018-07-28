
import os
from os import environ

class Config:

########## GENERAL ##########
  SECRET_KEY = 'jhagdsiua6t87dgvbiu^R&%UDFVIUF^D*%^I&C'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
