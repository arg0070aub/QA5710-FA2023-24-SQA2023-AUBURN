import logging

def create_helper(): 
    fileName  = '2023-11-09.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    return logging.getLogger('team-24-logger')

def info(logged_string):
    create_helper().info(logged_string)