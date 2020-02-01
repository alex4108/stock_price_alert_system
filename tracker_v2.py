import time
import requests
import boto3

HIGHEST_BOUND = 0.30
HIGH_BOUND = 0.25
LOW_BOUND = 0.18
LOWEST_BOUND = 0.17

PHONE_NUM = '+64274556736'

BITSTAMP_API = 'https://www.bitstamp.net/api/v2/ticker/xrpusd/'

CLIENT = boto3.client('sns', 'us-east-1')

response = requests.get(BITSTAMP_API)
message_sent = False

while response.status_code == 200:
    response = response.json()
    asking_price = float(response['ask'])

    if asking_price < LOWEST_BOUND:
        message = "Rate is at $" + str(asking_price) + ". Lowest bound: <$" + str(LOWEST_BOUND) + " threshold breached"
        message_sent = True
    if asking_price < LOW_BOUND:
        message = "Rate is at $" + str(asking_price) + ". Lowser bound: <$" + str(LOW_BOUND) + " threshold breached"
        message_sent = True

    if asking_price > HIGHEST_BOUND:
        message = "Rate is at $" + str(asking_price) + ". Highest bound: >$" + str(HIGHEST_BOUND) + " threshold breached"
        message_sent = True
    if asking_price > HIGH_BOUND:
        message = "Rate is at $" + str(asking_price) + ". Higher bound: >$" + str(HIGH_BOUND) + " threshold breached"
        message_sent = True

    if message_sent:
        CLIENT.publish(PhoneNumber=PHONE_NUM, Message=message)
        print('Message sent. Will update in 15 minutes')
        time.sleep(900)
        message_sent = False

    time.sleep(1)
    response = requests.get(BITSTAMP_API)

print(response.status_code)