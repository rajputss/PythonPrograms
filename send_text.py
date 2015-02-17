from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd8bb11ffdae926f737fd68ae4c30053a"
auth_token  = "c8e1d7f10d5908872a346da401e8a7d6"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Tashe please?! Leave her alone <3",
    to="+15406285866",    # Replace with your phone number
    from_="+14433643133") # Replace with your Twilio number
print message.sid


