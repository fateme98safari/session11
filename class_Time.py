class Time():
    def __init__(self,hour,minute,secound):
        self.hour=hour
        self.minute=minute
        self.secound=secound
        self.fix()
    def show(self):
        print(self.hour,":",self.minute,":",self.secound)

    def sum(self,other):
        new_hour=self.hour + other.hour
        new_minute=self.minute + other.minute
        new_secound=self.secound + other.secound
        result=Time(new_hour,new_minute,new_secound)
        return result

    def sub(self,other):
        new_hour=self.hour - other.hour
        new_minute=self.minute - other.minute
        new_secound=self.secound - other.secound
        result=Time(new_hour,new_minute,new_secound)
        return result

    def sec_to_time(self):
        return T3

    def time_to_sec(self):
        result= (self.hour * 3600) + (self.minute * 60) + self.secound
        print(result)
        return result

    def GMT_to_Tehran_time(self):
        new_hour= self.hour + 3
        new_minute= self.minute + 30
        new_secound= self.secound
        result=Time(new_hour,new_minute,new_secound)
        return result

    def fix(self):
        while self.secound >= 60:
            self.secound -= 60
            self.minute+=1

        while self.minute >= 60:
            self.minute-=60
            self.hour+=1

        while self.hour >= 24:
              self.hour -= 24

        while self.secound < 0:
            self.secound +=60
            self.minute -=1

        while self.minute < 0:
            self.minute +=60
            self.hour -=1

        while self.hour < 0:
              self.hour +=24

T1=Time(20,45,24)
T2=Time(3,12,3)
T3=Time(0,0,3624)
obj1=T1.sum(T2)
obj1.show()

obj2=T1.sub(T2)
obj2.show()

obj3=T3.sec_to_time()
obj3.show()

obj4=T1.time_to_sec()
#obj4.show()

obj5=T2.time_to_sec()
#obj5.show()
obj6=T1.GMT_to_Tehran_time()
obj6.show()

obj7=T2.GMT_to_Tehran_time()
obj7.show()
