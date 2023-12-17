status=False
people=[
    {
        'username':'Sadil123',
        'password':'Hello123'
    },
    {
        'username':'sumpumm69',
        'password':'ilu'
    }
]
def login():
    global status
    name=input('enter username')
    password=input('enter password')
    for i in people:
        if i['username']==name and i['password']==password:
            print('You are logged in')
            status=True
            break
        
        
    if(status==False):
        print("Invalid Credentials")
    
            
def register():
    name=input('create a username')
    password=input('create a password')
    people.append({'username':name,'password':password})   
    print("You are registered")
    
    
def logout():
    global status
    if status==True:
      status=False
      print('you are logged out')
    else:
        print('please login first')
        login()
def menu():
    print('menu')
    print("""
          1.login
          2.register
          3.logout
          4.exit
          """)
    choice=int(input("Enter choice : "))
    if choice==1:
        login()
        menu()
    elif choice==2:
        register()
        menu()
    elif choice==3:
        logout()
        menu()
    else:
        print('exit')
        exit()
        
        
menu()
        
    
    
       