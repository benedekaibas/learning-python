#C:\Users\kaiba\OneDrive\Asztali gép\learning-python\fb_bot.py
#TODO: make the import workable, because it has missing elements problems
#making a facebook bot
from fbchat import Client
from fbchat.models import Message
from fbchat.models import *


#sigzer187@gmail.com
#sodigeci9

def main():
    username = str(input("Enter your email address: \n"))
    password = input("Enter your password: \n")
    client = Client(username, password)

    #login 
    if not client.isLoggedIn():
        client.login()
    else:
        print("Error")
    




if __name__ == "__main__":
    main()