import random
import mongodb
import time
ccount = 0
def new_num():
    return  random.randint(3,8)
coord = ['13.12179317637144, 77.6124743815768', '13.123641693773697, 77.61889555934393','13.116640852369846, 77.61295899876677']
def insert():
    for i in coord:
        mongodb.new_value_insert(i,new_num(),'new')
def update():
    for i in coord:
        mongodb.update_values(i,new_num())

while True:
    update()
    ccount = 0
    print('updated')
    time.sleep(10)