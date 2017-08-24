from twilio.rest import Client # modual import
# Twilio {software library} Rest {sub library} Client {class}

from secrets import auth_token

# Your Account SID from twilio.com/console
account_sid = "ACdfe47e56dcfad7f49f741761f44d5b5b"
# Your Auth Token from twilio.com/console
# auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

def error_msg(webName = 'one of your URL'):
    message = client.messages.create(
        to="+16503051219",
        from_="+18316107144",
        body = webName+"is down!")
    print(message.sid)