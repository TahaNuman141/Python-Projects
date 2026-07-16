def count(address):
    c=0
    import os
    for file in os.listdir(address):
        c=c+1
    print(c)

def names(address):
    import os
    for file in os.listdir(address):
        print(file)

def sorta(address,r):
    import os
    files=sorted(os.listdir(address),reverse=r)
    for file in files:
        print(file)

def delete(address,file_name):
    import os
    full_path=os.path.join(address,file_name)
    if os.path.exists(full_path):
        os.remove(full_path)
        print("File Deleted:")
    else:
        print("File not found")
        

 



print("Enter the Address")
address=input("Address You Entered: ")
print("Address Imported Successfully")

while True:
 print("ENTER ONE TO DISPLAY COUNT OF FILES PRESENT")
 print("ENTER TWO TO DISPLAY NAMES OF FILES PRESENT")
 print("ENTER THREE TO DISPLAY FILES (A-Z OR Z-A)")
 print("ENTER FOUR TO DELETE FILES")
 print("ENTER FIVE TO EXIT")
 x=int(input("YOU ENTERED:   "))

 match x:
    case 1:
        count(address)
    case 2:
        names(address)
    case 3:
        print("A-Z Press 1")
        print("Z-A Press 2")
        order=int(input("You Entered:   "))
        r=0
        if order==1:
            r=False
        if order==2:
            r=True
        sorta(address,r)
    case 4:
         print("Enter File Name")
         file_name=input(r"You Entered: ")
         delete(address,file_name)
    case 5:
         break
    case _:
        print("Invalid Input")
    
    

   



    
    