
import os
from os import environ

class Config:

########## GENERAL ##########
  SECRET_KEY = 'jhagdsiua6t87dgvbiu^R&%UDFVIUF^D*%^I&C'

  if os.environ.get('ENV')== 'production':
    app.config['DEBUG']= False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
  else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://fantaso:4oZe0EPTgV@localhost/fantaso'
    app.config['DEBUG']= True

  app.run(port=3000)
