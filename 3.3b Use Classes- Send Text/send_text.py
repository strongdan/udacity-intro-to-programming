# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

#from twilio.rest import TwilioRestClient

# Your code here.

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC467b689902eb6f5aa0a2ac930019e881"
auth_token  = "be8cc6b2a9711e1cabc2b3f282d860bb"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Well, hello there... world",
    to="+19072090409",    # Replace with your phone number
    from_="+15107687323") # Replace with your Twilio number
print ( message.sid )
