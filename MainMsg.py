from twilio.rest import Client

account_sid = ''          #your account SID in Twiliow
auth_token = ''             #Your Auth Code Below SID
client = Client(account_sid, auth_token)


def MainMsg():                                                     #MainMsg Function
    msg= client.messages.create(
                            from_='whatsapp: +14155238886',        # from twilow Number (You Can Buy customise number)
                            body='Testing Msg 2',                  # Main message
                            to= 'whatsapp:+919918745589'           #Verified Mobile Number
    )
    print(msg.sid)

if __name__ == "__main__":
    MainMsg()  
