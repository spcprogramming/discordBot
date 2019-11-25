def read():
    try:
        text = open("token.txt", "r")
        token = str(text.readline().rstrip())
        text.close()
        return token
    except:
        print("Token not set.\nFind it under Bot in you Discord Application page.\nPaste it into the token file")
        return
