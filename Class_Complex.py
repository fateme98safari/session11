class Complex():
    def __init__(self, real , image):
        self.real=real
        self.image=image

    def show(self):
        print(self.real ,"+", self.image,"i")

    def sum(self,other):
        new_real=self.real + other.real
        new_image=self.image + other.image
        x=Complex(new_real , new_image)
        return x
    def sub(self,other):
        new_real=self.real - other.real
        new_image=self.image - other.image
        x=Complex(new_real , new_image)
        return x
    def mul(self,other):
        new_real=((self.real * other.real)-(self.image * other.image))
        new_image=((self.real * other.image) + (self.image * other.real))
        x=Complex(new_real , new_image)
        return x


a = Complex(5,8)
a.show()
b=Complex(7, 4)
b.show()
z= a.sum(b)
z.show()
k= a.mul(b)   
k.show()   
h=a.sub(b)
h.show()  