from pet import Pet


from pet import Pet

class Wolf(Pet):
    def __init__(self, name):
        super().__init__(name)

    def noise(self):
        super().noise()
        print ('hoooowwl!')
        return self

