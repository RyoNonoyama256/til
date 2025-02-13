class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")

car = Car()
yugo = Yugo()
car.exclaim()
yugo.exclaim()