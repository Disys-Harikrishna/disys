class Google_pay:                                                                               
    
    def __init__(self,Name,mobile_number,email,acc):                                                                  
        self.name=Name
        self.phone=mobile_number
        self.Email=email
        self.account_numb=acc
        
    def googlepay(self):
        print("Google Pay")

    def user_name(self):
        if type(self.name) == str:
            if len(self.name) <= 30:                                                                                
                print("name verified")
            else:
                raise ValueError("the name does not exist")
        else:
            raise TypeError("the name should contain only alphabets")
        
    def mobile(self):
        if type(self.phone) == str:
            if (len(self.phone)<=10):
                print("mobile verified")
            else:
                raise TypeError("the mobile should  only contain integers ")
            
        else:
            raise ValueError("the mobile number is invalid")


        
    def email_verification(self):
        if type(self.Email) == str:                                                                           
            if len(self.Email) <=20:                                                                              
                print("email verified")
            else:
                raise ValueError("The email is not correct")
        else:
            raise TypeError("invalid emailid")
        
    def PanCard(self):
        self.pan_number="BI2390K234"
        if (len(self.pan_number) == 10):
            print("pan card verified")
        else:
            raise ValueError("Inavlid Pan_number")
    
    def Bank_details(self):
        if type(self.account_numb)== str:
            if len(self.account_numb) <=30:
                print('yes account exist')
            else:
                raise ValueError('account not found')
        
   
        
    def otp_verification(self,code,otp):
        if(otp==code):
            print("otp verified")
        else:
            raise ValueError("otp not verified")

    
    

    def set_Pin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pin_number")

    def Enter_pin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print("DONE")
        else:
            raise ValueError("pin not matched")
