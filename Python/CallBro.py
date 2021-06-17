class Bros :

    def __init__(self) :
        self.conversation = iter(["Hey bro", "Wassup"])
        self.n = 0

    def bros1(self) :
        print(self.bros1.__name__ + " : " + next(self.conversation))
        if (self.n < 1) :
            self.n += 1
            self.bros2()
        else :
            print()

    def bros2(self) :
        print(self.bros2.__name__ + " : " + next(self.conversation))
        if (self.n < 1) :
            self.n += 1
            self.bros1()
        else :
            print()


if __name__ == "__main__" :

    Bros1 = Bros()
    Bros1.bros1()

    Bros2 = Bros()
    Bros2.bros2()