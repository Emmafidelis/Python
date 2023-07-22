from twilio.rest import Client

account_sid = "AC0b8c71b27b24bde478880d1d7e6df561"
auth_token = "7df5891fb222a15ae5b0aba5c7c902dd"

client = Client(account_sid, auth_token)

call = client.messages.create(
  to="...",
  from_="...",
  body="This is our first message"
)
