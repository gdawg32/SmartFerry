from twilio.rest import Client

SID = 'AC9d6fc6ca2d7f00474fc2dc1d798920cd'
AUTH_TOKEN = '6329b1c492fdbefaf6e1b9fba9858780'

cl = Client(SID, AUTH_TOKEN)

def send_sms():
    cl.messages.create(body='BOAT ENGINE TEMPERARTURE UNSTABLE. SEND RESCUE TEAM', from_='+15075160910', to='+918308621345')