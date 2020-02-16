import logging
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#logging.basicConfig(stream=sys.stdout, level=logging.debug)

def stringToLower(inStr):
    return inStr.lowwer()
    