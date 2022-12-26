class Fraction():
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator

    def show(self):
        print(self.numerator ,'/',self.denominator)

    def sum(self,other):
        new_numerator=(self.numerator * other.denominator) + (self.denominator * other.numerator )
        new_denominator=self.denominator * other.denominator
        result=Fraction(new_numerator,new_denominator)
        return result 

    def sub(self,other): 
        new_numerator=(self.numerator * other.denominator) - (self.denominator * other.numerator )
        new_denominator=self.denominator * other.denominator
        result=Fraction(new_numerator,new_denominator)
        return result 

    def mul(self,other):
        new_numerator=self.numerator * other.numerator
        new_denominator=self.denominator * other.denominator
        result=Fraction(new_numerator,new_denominator)
        return result
    def div(self,other):
        new_numerator=self.numerator * other.denominator
        new_denominator=self.denominator * other.numerator
        result=Fraction(new_numerator,new_denominator)
        return result

    def fraction_to_number(self):
        number=float(self.numerator / self.denominator)
        self_denominator=1
        result=Fraction(number,self_denominator)
        print(number)
        return result

    def simplify(self):
        new_numerator=self.numerator
        new_denominator=self.denominator
        for i in range(2,10,1):
            if new_numerator % i==0 and new_denominator % i==0:
                new_numerator=new_numerator / i
                new_denominator=new_denominator / i
        result=Fraction(new_numerator,new_denominator)
        return result
       
F1=Fraction(75,70)
F1.show()
F2=Fraction(12,32)
F2.show()

obj1=F1.sum(F2)
obj1.show()

obj2=F1.sub(F2)
obj2.show()

obj3=F1.mul(F2)
obj3.show()

obj4=F1.div(F2)
obj4.show()

obj5=F1.fraction_to_number()
obj5=F2.fraction_to_number()

obj6=F1.simplify()
obj6.show()
obj6=F2.simplify()
obj6.show()