import product

product_detail = product.product

class Product_info:
    def __init__(self):
        pass
    def lst(self):
        return product.product
'''def list_of_products():
    for i in range(len(product_detail)):
        lst = list(filter(lambda x: x['name'], product_detail))
    for i in lst:
        print(i['name'])'''

def category_of_products():
    cat = set()
    for i in product_detail:
        cat.add(i['category'])
    for x in cat:
        print(x)
        
class WashingMachine:
    def __init__(self, name, machine_capacity, machine_rpm, type, cost, currency, colour, category = 'washing_machine', id = len(product.product)+1):
        self.name = name
        self.machine_capacity = machine_capacity
        self.machine_rpm = machine_rpm
        self.type = type
        self.cost = cost
        self.currency = currency
        self.colour = colour
        self.category = category
        self.id = id
    def new(self):
        product_details = dict({'machine_capacity':self.machine_capacity, 'machine_rpm':self.machine_rpm, 'type':self.type})
        newly_added = dict({'id':self.id, 'name':self.name, 'product_details':product_details, 'cost':self.cost, 'currency':self.currency, 'category':self.category, 'colour':self.colour})
        product_detail.append(newly_added)
        product.product = product_detail
        return product.product

class Mobile:
    def __init__(self, name, ram, processor, screen_size, cost, currency, colour, category = 'mobile', id = len(product.product)+1):
        self.name = name
        self.ram = ram
        self.processor = processor
        self.screen_size = screen_size
        self.cost = cost
        self.currency = currency
        self.colour = colour
        self.category = category
        self.id = id
    def new(self):
        product_details = dict({'ram':self.ram, 'processor':self.processor, 'screen_size':self.screen_size})
        newly_added = dict({'id':self.id, 'name':self.name, 'product_details':product_details, 'cost':self.cost, 'currency':self.currency, 'category':self.category, 'colour':self.colour})
        product_detail.append(newly_added)
        product.product = product_detail
        return product.product

class Tv:
    def __init__(self, name, issmart, resolution, screen_size, cost, currency, colour, category = 'tv', id = len(product.product)+1):
        self.name = name
        self.issmart = issmart
        self.resolution = resolution
        self.screen_size = screen_size
        self.cost = cost
        self.currency = currency
        self.colour = colour
        self.category = category
        self.id = id
    def new(self):
        product_details = dict({'issmart':self.issmart, 'resolution':self.resolution, 'screen_size':self.screen_size})
        newly_added = dict({'id':self.id, 'name':self.name, 'product_details':product_details, 'cost':self.cost, 'currency':self.currency, 'category':self.category, 'colour':self.colour})
        product_detail.append(newly_added)
        product.product = product_detail
        return product.product
class Del:
    def __init__(self, id):
        self.id = id
    def new(self):
        return product.product.pop(int(self.id)-1)
