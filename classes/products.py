# 1. Базовый класс Product и производные классы для различных типов продуктов

class Product:
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def product_name(self):
        return self.name
    def get_details(self):
        return f"Продукт: {self.name}, Цера: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period
    
    def product_name(self):
        return self.name

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material
        
    def product_name(self):
        return self.name

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."
    
    
class Household_chemicals(Product):
     """
    Класс, представляющий бытовую химию, наследующий класс Product.
    """
     def __init__(self, name, price, expiration_date, marka):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.marka = marka
        
     def product_name(self):
        return self.name
     def get_details(self):
        return f"Бытовая химия: {self.name}, Марка: {self.marka}, Цена: {self.price} руб, Срок годности: {self.expiration_date} лет"