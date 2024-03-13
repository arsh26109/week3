class Person :
    
    def __init__(self):
        self.name="Sam"
        self.gender="Male"
        self.age=22

    def talk(self):
        print("Hi I'm ", self.name)

    def vote(self):
        if self.age<18:
            print("I am not eligible to vote")
        else :
            print("I am eligible to vote")

obj1= Person("Sam","Male",22)
obj2= Person("Jesse","Female",16)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()