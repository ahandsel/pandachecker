from twilio.rest import Client # modual import
# Twilio {software library} Rest {sub library} Client {class}

# Your Account SID from twilio.com/console
account_sid = "ACdfe47e56dcfad7f49f741761f44d5b5b"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)