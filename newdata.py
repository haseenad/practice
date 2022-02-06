class hass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('{} and {} is equal to {} '.format(self.a,self.b,self.a+self.b))
    def mul(self):
        print('{} and {} is equal to {}'.format(self.a,self.b,self.a*self.b))
z=hass(2,5)
z.add()
z.mul()