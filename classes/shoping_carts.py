# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, customer, admin):
        self.items = []
        self.customer = customer
        self.admin = admin

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})
        


    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        
        details = f"Пользователь: {self.customer} приобрел "
        for item in self.items:
            details += f" {item['Продукт'].product_name()}"
            
        details += f"\nОбщая сумма: {self.get_total()} руб"
        details += f"\nЗарегистрировал покупки пользователь {self.admin} "
        return details