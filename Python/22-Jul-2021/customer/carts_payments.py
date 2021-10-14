class Cart:
    def __init__(self, product):
        self.product = product

    def add(self, item): 
        self.product.append(item)

    def view(self):
        return self.product

    def delete(self, name):
        for index, item in enumerate(self.product):
            if(name == item['name']):
                self.product.pop(index)
        return self.view()
    
    def clear_cart(self):
        self.product = []


