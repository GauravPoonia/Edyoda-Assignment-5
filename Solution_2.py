# create your own builtin class methods

x = int(input("Enter the number : "))
n = int(input("Enter the power : "))

class power:
    
    def pow(self,x,n):
        data = x ** n
        print(data)

power_obj = power()
power_obj.pow(x,n)