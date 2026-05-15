class Laptop:
    company = "HP"

    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def show_info(self):
        print(f"Model: {self.model}")
        print(f"RAM: {self.ram} GB")


l1 = Laptop("EliteBook", 8)
l2 = Laptop("ProBook", 16)

l1.show_info()
print("----------")
l2.show_info()
