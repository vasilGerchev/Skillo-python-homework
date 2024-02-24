class Human:
    def __init__(self, height, weight, nationality):
        self.height = height
        self.weight = weight
        self.nationality = nationality

    def __str__(self):
        return "Human\n" + f"Gender: {self.gender()}\n" + \
            f"Nationality: {self.nationality}\n" + f"Weight: {self.weight}\n" + f"Height: {self.height}\n"

    def get_height(self):
        return self.height

    def set_height(self):
        self.height = height

    def gender(self):
        pass


class Man(Human):
    #  def __str__(self):
    # return super().__str__() + f" Gender: {self.gender()}"

    def gender(self):
        return 'Male'


class Women(Human):
    def __str__(self):
        return super().__str__() + f"Gender: {self.gender()}"

    def gender(self):
        return 'Female'


man = Man(180, 80, 'Bulgarian')
woman = Women(155, 45, 'Bulgarian')

print(man)
print(woman)
