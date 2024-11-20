from logger import logging

def add(a,b):
    logging.debug("The Addition Operation is taking place")
    return a+b

logging.debug("The Addition function is called")
add(10,15)