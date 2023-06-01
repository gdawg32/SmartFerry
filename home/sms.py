from twilio.rest import Client

SID = 'AC28f23440c235e7137603171a1b4f0dd2'
AUTH_TOKEN = '0f64e73feecae6354981e75709625090'

cl = Client(SID, AUTH_TOKEN)

def send_sms():
    cl.messages.create(body='BOAT ENGINE TEMPERARTURE UNSTABLE. SEND RESCUE TEAM', from_='+13612735622', to='+918308621345')
