number = int(input("intrer votre nombre"))
table = list(range(1 , 12))

for tab in table:
    print(f"{tab} * {number} = {tab * number}")
    
    

num = 1
while num < 11:
    print(num)
    num += 1 
    

userString = input('votre string svp')
if len(userString) > 10:
    print(" String too long")
else:
    print(" string is shoot")
    
        
    

for i in list(range(1 , len(stg))):
     print(stg[0:i + 1])