# a basic python password manager, if you are familiar with keys then you can use fernet keys to make it more effective

def see():
    with open('pass.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user : " , user, "password : ", passw)
            
def add():
    name=input('account name : ')
    password=input('password : ') 
    # we use with as to not manually close the file pass.tx
    with open('pass.txt','a') as f
        f.write(name + '|' + password + "/n")
while True :
    mode = input("view or add or q").lower()
    if mode == "q":
        break
        
    if mode == "view":
        see()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue
    
        
