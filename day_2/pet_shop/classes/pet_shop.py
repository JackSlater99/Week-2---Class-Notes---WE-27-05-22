class PetShop:
    def __init__(self, name, stock, total_cash):
        self.name = name
        self.stock = stock
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.stock)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, cash_value):
        self.total_cash += cash_value

    def remove_pet(self, pet):
        self.stock.remove(pet)

    def find_pet_by_name(self, name):
        for pet in self.stock:
            if pet.name == name:
                return pet
        
    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        if not customer.cash >= pet.price:
            return
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.remove_pet(pet)
        self.increase_pets_sold()
        customer.add_pet(pet)

