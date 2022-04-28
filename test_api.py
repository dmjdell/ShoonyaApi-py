import imp
from api_helper import ShoonyaApiPy
import logging
import datetime

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = ShoonyaApiPy()

#credentials
user    ='FA58202'
pwd     ='Dennov@16'
factor2 ='AVQPJ5261K'
vc      ='FA58202_U'
apikey  ='11db1bd7fb468128da47d0eed55695a0'
imei    ='abc1234'
#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=apikey, imei=imei)


feed_opened = False

def event_handler_order_update(order):
 print(f"order feed {order}")

def event_handler_feed_update(tick_data):
 print(f"feed update {tick_data}")

def open_callback():
 global feed_opened
 feed_opened = True

api.start_websocket( order_update_callback=event_handler_order_update,
 subscribe_callback=event_handler_feed_update, 
socket_open_callback=open_callback)
while(feed_opened==False):
 pass


# subscribe to a single token 
api.subscribe('NSE|22')


print(ret)

