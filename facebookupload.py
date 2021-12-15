import math
import random
class facebook:                                                                               
    
        def __init__(self):                                                                  
            self.name=''
            self.phone=''
            self.Email=''
            self.pet=''
            self.con=''
            
        

        def user_name(self):
            name=input('your account name')
            print('hello'+name)
            if type(self.name) == str:
                if len(self.name) <= 30:                                                                                
                    print("name verified")
                else:
                    raise ValueError("the name does not exist")
            else:
                raise TypeError("the name should contain only alphabets")
        
        def mobile(self):
            phone=input('enter the mobile')
            print('your number'+phone)
            if type(self.phone) == str:
                if (len(self.phone)<=10):
                    print("mobile verified")
                else:
                    raise TypeError("the mobile should  only contain integers ")
                
            else:
                raise ValueError("the mobile number is invalid")
        
        def email_verification(self):
            Email=input('enrter the email')
            print('your email'+Email)
            if type(self.Email) == str:                                                                           
                if len(self.Email) <=20:                                                                              
                    print("email verified")
                else:
                    raise ValueError("The email is not correct")
            else:
                raise TypeError("invalid emailid")


        def security_quest(self):
            
            pet=input('your pet name')
            

            zet=input('pet name=')
            if (pet==zet):
                print('verified')
            
            else:
                raise ValueError('not correct pet')

        def confirm(self):
            con=input('do u want to  open friends list')
            if (con=='y'):
                print('okay')
            else:
                raise ValueError('not correct response')
            
            


        def generateOTP():
            digits = "01234567895"
            OTP = ""
            for i in range(5) :
                OTP += digits[math.floor(random.random() * 10)]
            return OTP
    

        otp=generateOTP()

        print("OTP of 5 digits:",otp)

        votp=input("enter otp")

        if(otp==votp):
            print('verified')
        else:
            ValueError('check your OTP')



hari=facebook()
hari.user_name()
hari.mobile()
hari.email_verification()
hari.security_quest()
hari.confirm()




contact=[{"name":"vijay","groupname":"boys","Groupcount":25},
{"name":"ajith","groupname":"boys","Groupcount":25},
{"name":"surya","groupname":"boys","Groupcount":25},
{"name":"abisheik","groupname":"boys","Groupcount":25},
{"name":"vishnu","groupname":"boys","Groupcount":25},
{"name":"vimal","groupname":"boys","Groupcount":25},
{"name":"sarnath","groupname":"boys","Groupcount":25},
{"name":"riyaz","groupname":"boys","Groupcount":25},
{"name":"anbu","groupname":"boys","Groupcount":25},
{"name":"vinod","groupname":"boys","Groupcount":25},
{"name":"amal","groupname":"boys","Group":25},
{"name":"snehan","groupname":"boys","Group":25},
{"name":"jayanth","groupname":"boys","Group":25},
{"name":"sindura","groupname":"boys","Group":25},
{"name":"sowmiya","groupname":"boys","Group":25},
{"name":"sara","groupname":"boys","Group":25},
{"name":"madan","groupname":"boys","Group":25},
{"name":"preethika","groupname":"boys","Group":25},
{"name":"swetha","groupname":"boys","Group":25},
{"name":"kumarnath","groupname":"boys","Group":25},
{"name":"sheela","groupname":"boys","Group":25},
{"name":"arun","groupname":"boys","Group":25},
{"name":"priya","groupname":"boys","Group":"25"},
{"name":"pradeep","groupname":"boys","Group":25},
{"name":"praveen","mutualfriend":"karthi","relation":"closefriend"},
 {"name":"lakshman","mutualfriend":"prugu","relation":"brother"},
 {"name":"sam","mutualfriend":"vishnu","relation":"friend"},
 {"name":"sathish","mutualfriend":"prince","relation":"friend"},
 {"name":"diana","mutualfriend":"kavya","relation":"sister"},
 {"name":"abi","mutualfriend":"priju","relation":"sister"},
 {"name":"krithi","mutualfriend":"sneha","relation":"friend"},
 {"name":"arunpriya","mutualfriend":"shalini","relation":"friend"},
 {"name":"sivan","mutualfriend":"melkis","relation":"friend"},
 {"name":"boo","mutualfriend":"rajesh","relation":"closefriend"},
 {"name":"balaji","mutualfriend":"vino","relation":"closefriend"},
 {"name":"santham","mutualfriend":"vichu","relation":"brother"},
 {"name":"akash","mutualfriend":"vineeth","relation":"friend"},
 {"name":"sanjay","mutualfriend":"adhi","relation":"friend"},
 {"name":"surya","mutualfriend":"dharshan","relation":"brother"},
 {"name":"ramesh","mutualfriend":"selva","relation":"cousin"},
 {"name":"selva","mutualfriend":"sathish","relation":"cousin"},
 {"name":"gopi","mutualfriend":"bala","relation":"brother"},
 {"name":"krithika","mutualfriend":"mahesh","relation":"sister"},
 {"name":"babu","mutualfriend":"mohan","relation":"brother"},
 {"name":"preethika","mutualfriend":"aswetha","relation":"friend"},
 {"name":"bathraa","mutualfriend":"varatha","relation":"friend"},
 {"name":"mukesh","mutualfriend":"avinash","relation":"friend"},
 {"name":"abilash","mutualfriend":"anbu","relation":"friend"},
 {"name":"baby","mutualfriend":"jayanthi","relation":"friend"}]
  
for i in contact:
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")







