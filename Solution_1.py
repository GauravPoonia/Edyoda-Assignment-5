# create your own builtin class methods

class power:

    def __init__(self):
        x = int(input("Enter the number : "))
        n = int(input("Enter the power : "))
        self.x = x
        self.n = n

    def set_x(self,x):
        self.x = x
    
    def get_x(self):
        return self.x

    def set_n(self,n):
        self.n = n
    
    def get_n(self):
        return self.n

    def pow(self):
        print(self.x ** self.n)


power_obj = power()
power_obj.pow()