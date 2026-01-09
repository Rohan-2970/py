#write aprogram to find wheteher  a given username 
# contains less than 10 characters or not 
username=input("Enter your username : ")
if not username:
    print("there is no username")
if(len(username)<=10):
    print("contains less than 10 characters",username)
else:
    print("contains more than 10 characters",username)
