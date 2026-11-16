
def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    UserFile = open("Users.txt", "a")  
    while True:
        username = GetUserName()  
        if username.upper() == "END":
            break
        userpwd = GetUserPassword()  
        userrole = GetUserRole()  
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
    UserFile.close()  

def GetUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd


def GetUserRole():
    return "User"
    
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")  
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)

def Login():
    
    pass


CreateUsers()
printuserinfo()
