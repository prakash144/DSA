class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def print(self):
        print(self.ingredients)
        
class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "paneer-patty"]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ["bun", "tomatoe", "lettuce", "cheese", "paneer-patty"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)
    
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()
    