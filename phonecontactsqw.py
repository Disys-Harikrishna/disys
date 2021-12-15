class friend():
    def __init__(self,numb,nam,nic):
        self.number=numb
        self.contacts=nam
        self.adamo=nic
        
        

    

    def mobile_verification(self):
        if type(self.number) == str:
            if (len(self.number))== 10:
                print('indian number')
            else:
                raise ValueError('it is a non indian number')
        else:
            raise TypeError('it is not a phone number')
        
    def verification(self):
        if type(self.contacts) == str:
            if (len(self.contacts)) <=10:
                print('right person')
            else:
                raise ValueError('it is wrong name surely')
        else:
            raise TypeError('it is not the person')
        
    def nick(self):
        if type(self.adamo) == str:
            print('nick name correct')
        else:
            raise ValueError('it is not the right person')

    

        
   
            






