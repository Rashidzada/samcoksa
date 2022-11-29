class Apples:
    def __init__(self):
        self.name = 'my good best way of apples'
        self.price = 400
        self.qty = 'best'

    def showinfo(self):
        print(self.name)
        print(self.price)
        print(self.qty)
class Bananas(Apples):
    def __init__(self):
        super(Bananas, self).__init__()
        self.name = 'My bananas for the last time to the '
        self.price = 500
        self.qty = ' good'
        self.name += ' this is a testing for the last itaem'
        print(self.name)
if __name__ == '__main__':

    object = Bananas()