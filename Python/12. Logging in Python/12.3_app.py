import logging

## Basic logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    res = a + b
    logger.debug(f"Adding {a} + {b} = {res}")
    return res

def subtract(a,b):
    res = a - b 
    logger.debug(f"Subtracting {a} - {b}={res}")
    return res


def multiply(a,b):
    res = a * b 
    logger.debug(f"Multiplying {a} * {b}={res}")
    return res


def divide(a,b):
    try:
        res = a / b
        logger.debug(f"Dividing {a}/{b}={res}")
        return res
    except ZeroDivisionError:
        logger.debug("Division by Zero Error")
        return None
    
add(10,15)
subtract(15,10)
multiply(10,20)
divide(20,10)
