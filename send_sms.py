from twilio.rest import Client # modual import
# Twilio {software library} Rest {sub library} Client {class}

from secrets import auth_token
from secrets import myNum
from secrets import roboNum
# Private info is in a unpublished secrets.py

# Your Account SID from twilio.com/console
account_sid = "ACdfe47e56dcfad7f49f741761f44d5b5b"
# Your Auth Token from twilio.com/console
# auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

def error_msg(webName = 'one of your URL'):
    message = client.messages.create(
        to= myNum,
        from_= roboNum,
        body = webName+" is down!")
    print(message.sid)