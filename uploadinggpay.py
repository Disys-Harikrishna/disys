import math
import random

class Google_pay:                                                                               
    
    def __init__(self,Name,mobile_number,email,acc):                                                                  
        self.name=Name
        self.phone=mobile_number
        self.Email=email
        self.account_numb=acc
        self.pan_number = ''
        
        
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
        
        pan=input('enter the pan number')
        print('pannumber='+pan)
        
        if (len(pan) == 10):
            print("pan card verified")
        else:
            raise ValueError("Invalid Pan_number")
    
    def Bank_details(self):
        Bank=input('enter the account nymber=')
        print('account number='+Bank)
        if type(self.account_numb)== str:
            if len(self.account_numb) <=30:
                print('yes account exist')
            else:
                raise ValueError('account not found')
        
   

    
    

    def set_Pin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print('your pin is successfully created')
        else:
            raise ValueError('Invalid pin_number')

    def Enter_pin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print('ok')
        else:
            raise ValueError("pin not matched")

hari=Google_pay('kh204579@gmail.com','8005978921','hari','5000123457')
hari.googlepay()
hari.email_verification()
hari.mobile()
hari.user_name()
hari.PanCard()
hari.Bank_details()



hari.set_Pin("5656")
hari.Enter_pin(8059,8059)

class Phone_pe(Google_pay):                                                                                          
    def __init__(self,Name,mobile_number,email,acc):
        super().__init__(Name,mobile_number,email,acc)

    def open_phonepe(self):
        print("Phone pe")
        
hari=Phone_pe('kh204579@gmail.com','8005978921','hari','5000123457')
hari.open_phonepe()
hari.email_verification()
hari.mobile()
hari.user_name()
hari.PanCard()
hari.Bank_details()
hari.otp_verification(345678,345678)
hari.set_Pin("5696")
hari.Enter_pin(8058,8058)

def generateOTP() :
    
 
   
    digits = "01234567895"
    OTP = ""
 

    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
    

kotp=generateOTP()

print("OTP of 4 digits:", kotp)

votp=input("enter otp")

if(kotp==votp):
    print('sucessfull')
else:
    ValueError('check your OTP')



receptants=[{'name':'balaji','number':9884700382,'mon':100},
         {'name':'ajith','number':9940313776,'mon':500},
         {'name':'kingsly','number':874554295,'mon':800},
         {'name':'ram','number':874554279,'mon':100},
         {'name':'dinesh','number':746954295,'mon':0},
         {'name':'raj','number':8753951295,'mon':0},
         {'name':'lijo','number':9865314295,'mon':545},
         {'name':'kingsly','number':7538639512,'mon':900},
         {'name':'khan','number':6359854295,'mon':475},
         {'name':'june','number':874554291,'mon':500},
         {'name':'jane','number':874568978,'mon':0},
         {'name':'james','number':6354852512,'mon':0},
         {'name':'kadamba','number':874666695,'mon':0},
         {'name':'wandra','number':8747856375,'mon':5},
         {'name':'mandip','number':6396378941,'mon':6},
         {'name':'fahad','number':6365474232,'mon':4},
         {'name':'mahesh','number':871259175,'mon':5},
         {'name':'akash','number':7874579856,'mon':400},
         {'name':'ahalila','number':7445669988,'mon':100},
         {'name':'anju','number':8954674896,'mon':400},
         {'name':'amal','number':7822344111,'mon':100},
         {'name':'anu','number':7255669941,'mon':0},
         {'name':'sanjay','number':6363639696,'mon':2300},
         {'name':'kannan','number':8945674896,'mon':500},
         {'name':'kaala','number':8954674444,'mon':85},
         {'name':'kokila','number':8999674896,'mon':800},
         {'name':'jiten','number':8954671111,'mon':0},
         {'name':'raju','number':6236664896,'mon':20},
         {'name':'sakthi','number':8954677979,'mon':1000},
         {'name':'hira','number':8954888886,'mon':555},
         {'name':'liwan','number':9222674896,'mon':20},
         {'name':'prakas','number':8954612312,'mon':10000},
         {'name':'prajal','number':7777484896,'mon':0},
         {'name':'kunal','number':6969636565,'mon':9890},
         {'name':'anju','number':8954674896,'mon':482},
         {'name':'laju','number':8954674869,'mon':600},
         {'name':'arunila','number':8954778496,'mon':88},
         {'name':'arun','number':9854674896,'mon':0},
         {'name':'ravi','number':8954671312,'mon':584},
         {'name':'anil','number':6547417418,'mon ':600},
         {'name':'aju','number':8955200012,'mon':44},
         {'name':'majunu','number':9000006666,'mon':0},
         {'name':'hayagriva','number':6059596579,'mon':1},
         {'name':'supriya','number':6230060032,'mon':700},
          {'name':'anupriya','number':7000224896,'mon':100},
         {'name':'jay','number':6363009696,'mon':200},
         {'name':'sanj','number':6363639600,'mon':77},
         {'name':'palak','number':6000639696,'mon':555},
         {'name':'sanjay','number':7897639696,'mon':300},
         {'name':'saji','number':6363630000,'mon':0},
         {'name':'balal','number':6363646464,'mon':87},
         {'name':'kiruji','number':7400000099,'mon':800},
         {'name':'srini','number':7890000664,'mon':100},
         {'name':'jira','number':7890000064,'mon':0},
         {'name':'kuwan','number':8008009007,'mon':565},
         {'name':'kubuvan','number':9222555999,'mon':0},
         {'name':'kumba','number':9333674896,'mon':4000},
         {'name':'kalam','number':9666333111,'mon':48},
         {'name':'kombila','number':9222555693,'mon':3330},
         {'name':'kiriti','number':8000174896,'mon':442},
         {'name':'kaani','number':92226127836,'mon':2220},
         {'name':'litan','number':9220004896,'mon':600},
         {'name':'vinalan','number':7489674896,'mon':300},
         {'name':'jraja','number':7890111164,'mon':400},
         {'name':'raman','number':7890232364,'mon':200},
         {'name':'maya','number':8510000064,'mon':0},
         {'name':'kitu','number':7333300064,'mon':2222},
         {'name':'asraf','number':7444400064,'mon':50},
         {'name':'jitu','number':7333300045,'mon':1},
         {'name':'kiruj','number':8422000099,'mon':223},
         {'name':'srjni','number':8490000664,'mon':123},
         {'name':'lira','number':9990000064,'mon':31},
         {'name':'owan','number':6608009007,'mon':660},
         {'name':'uvan','number':9992555999,'mon':550},
         {'name':'tumba','number':8663674896,'mon':878},
         {'name':'salam','number':2366333111,'mon':0},
         {'name':'mombila','number':7422555693,'mon':22},
         {'name':'siriti','number':6330174896,'mon':66},
         {'name':'paani','number':741926127836,'mon':889},
         {'name':'kitttan','number':4710004896,'mon':0},
         {'name':'lallanalan','number':6349674896,'mon':85},
         {'name':'jraja','number':7890111164,'mon':996},
         {'name':'raaaman','number':7880232364,'mon':3},
         {'name':'gaya','number':8310000364,'mon':554},
         {'name':'situ','number':7888800064,'mon':1000},
         {'name':'kiranla','number':7444411264,'mon':60},
         {'name':'hitu','number':7232300045,'mon':99},
         {'name':'balajiiiii','number':9774700382,'mon':100},
         {'name':'kaaajith','number':9940317336,'mon':2022},
         {'name':'silly','number':753554295,'mon':2003},
         {'name':'rammmm','number':8745572860,'mon':2012},
         {'name':'gaanesh','number':476954295,'mon':2020},
         {'name':'suraj','number':8003951295,'mon':62},
         {'name':'liiijo','number':9864514278,'mon':55},
         {'name':'kingsly','number':7538639512,'mon':20},
         {'name':'khan','number':6359854295,'mon':500},
         {'name':'june','number':874554291,'mon':87},
         {'name':'jane','number':874568978,'mon':99},
         {'name':'james','number':6354852512,'mon':3220},
         {'name':'kadamba','number':874666695,'mon':82222},
         {'name':'wandra','number':8747856375,'mon':0},
         {'name':'mandip','number':6396378941,'mon':898},
         {'name':'fahad','number':6365474232,'mon':555},
         {'name':'mahesh','number':871259175,'mon':78},
         {'name':'akash','number':7874579856,'mon':2021},
         {'name':'ahalila','number':7445669988,'mon':25},
         {'name':'anju','number':8954674896,'mon':2200},
         {'name':'palraj','number':7773951295,'mon':20},
         {'name':'jojo','number':4685514278,'mon':200},
         {'name':'manssly','number':9833639512,'mon':9090},
         {'name':'haaaan','number':6639854295,'mon':88580},
         {'name':'pune','number':879994291,'mon':1000000},
         {'name':'bane','number':647968978,'mon':747},
         {'name':'thames','number':77414852512,'mon':5660},
         {'name':'boombaba','number':877766695,'mon':30},
         {'name':'kunddra','number':3347856375,'mon':5000},
         {'name':'gandip','number':7733378941,'mon':999999},
         {'name':'maahad','number':6365476232,'mon':8810},
         {'name':'kamalesh','number':888259175,'mon':2003},
         {'name':'shantanu','number':7874579111,'mon':100},
         {'name':'ahal','number':74444669988,'mon':21010},
         {'name':'achuu','number':89000674896,'mon':3303},
         {'name':'jaes','number':2004852512,'mon':14460},
         {'name':'kadaba','number':834666695,'mon':55000},
         {'name':'mandra','number':89947856375,'mon':0},
         {'name':'kunndip','number':7416378941,'mon':1050},
         {'name':'llahad','number':7065474232,'mon':1050},
         {'name':'magesh','number':511259175,'mon':0},
         {'name':'ashwin','number':7874539856,'mon':1000},
         {'name':'lila','number':7444664988,'mon':2005},
         {'name':'waju','number':8954677796,'mon':9090},
         {'name':'busraj','number':7777751295,'mon':99990},
         {'name':'sojo','number':23105514278,'mon':10000},
         {'name':'minssly','number':9610639512,'mon':33060},
         {'name':'hassaan','number':66743854295,'mon':64220},
         {'name':'manne','number':745994291,'mon':154320},
         {'name':'kaaane','number':647968977,'mon':0},
         {'name':'thame','number':77454852512,'mon':500},
         {'name':'baambaba','number':870066695,'mon':0},
         {'name':'kundda','number':334856375,'mon':20},
         {'name':'gandi','number':773338941,'mon':2000},
         {'name':'malhad','number':636547232,'mon':820},
         {'name':'kamalesh nath','number':848259175,'mon':330},
         {'name':'shantanu','number':7874579111,'mon':220},
         {'name':'aalu','number':74444665888,'mon':90},
         {'name':'achsu','number':891410674896,'mon':400},
         {'name':'rani','number':6653951295,'mon':30},
         {'name':'nijo','number':94445314295,'mon':0},
         {'name':'mesly','number':7538999512,'mon':50},
         {'name':'kandan','number':6359856295,'mon':100},
         {'name':'jaaane','number':874154291,'mon':20},
         {'name':'gane','number':874568558,'mon':0},
         {'name':'jades','number':6365852512,'mon':200},
         {'name':'hadamba','number':333666695,'mon':700},
         {'name':'jandra','number':8747800375,'mon':880},
         {'name':'mand','number':6396355941,'mon':500},
         {'name':'sahad','number':63120474232,'mon':900},
         {'name':'sarveshesh','number':7771259175,'mon':233},
         {'name':'makssh','number':3374579856,'mon':20},
         {'name':'kaila','number':74456698,'mon':22},
         {'name':'manjujuuu','number':89546745896,'mon':88},
         {'name':'kumal','number':7822399111,'mon':99}]



for i in receptants:                                                                                                             
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")


        
    







    

