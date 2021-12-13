class facebook:                                                                               
    
        def __init__(self,Name,mobile_number,email):                                                                  
            self.name=Name
            self.phone=mobile_number
            self.Email=email
            
            
        def fb(self):
            print("facebook")

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

        def your_pet(self,quest,just):
            self.quest=quest
            self.just=just
            if self.quest==self.just:
                print('ok')
            else:
                raise ValueError('not correct')
