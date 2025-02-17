class Parson():
    def __init__(self, name):
        self.name = name

class EmailParson(Parson):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

ep = EmailParson("nono", "nono@email")
print(ep.name, ep.email)
