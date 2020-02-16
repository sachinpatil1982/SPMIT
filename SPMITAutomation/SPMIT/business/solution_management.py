import logging
import sys
import os.path
import infrastructure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def stringLenghtTest(inStr):
    return len(inStr)

def test_infrastucture(some_string):
    print(infrastructure.stringLenghtTest_file(some_string))