import os
file_name=input('enter file name')
def create():
    try:
        open(file_name,"x")
    except Exception as e:
        print('file already exists')
        
def write():
    global file_name
    with open(file_name,"a") as f:
        content=input('Enter what you want to add')
        f.write('\n,content')
        
def delete():
    delete=input('enter the file name you want to delete')
    os.remove(file_name)
    
print('''
      1.Create file
      2.Append to file
      3.delete a file''')

choice=int(input('enter a Number'))
if choice==1:
    create()
elif choice==2:
    write()
elif choice==3:
    delete()
else:
    exit()
    
    
    