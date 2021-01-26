class Complex ():
    def initComplex(self):
        self.real = int(input("Enter the Real Part: "))
        self.img = int(input("Enter the Imaginary Part: "))

    def display(self):
        print(self.real, "+", self.img, "i", sep="")

    def sum(self, c1, c2):
        self.real = c1.real + c2.real 
        self.img = c1.img + c2.img 

c1 = Complex()
c2 = Complex()
c3 = Complex()

print("Enter first complex number")
c1.initComplex()
print("First complex number: ", end="")
c1.display()

print("Enter second complex number")
c2.initComplex()
print("Second complex number: ", end="")
c2.display()

print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()



