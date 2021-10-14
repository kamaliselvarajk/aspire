class ProductClass:
    
    input_field = {
        'washing_machine': ['machine_capacity', 'machine_rpm', 'type'],
        'mobile':['ram', 'processor', 'screen_size'],
        'tv': ['issmart', 'resolution', 'screen_size'],
        'common_input' : ['id', 'name', 'cost', 'currency', 'category', 'color']
        }
    
    def __init__(self, product):
        self.product = product
    
    def view_product(self):
        for products in self.product:
            print(products)
            
    def add_product(self, input):
        self.product.append(self.get_input(input))
        return self.product

    def get_input(self, ip):
        comm_input = {}
        diff_input = {}
        print(ip)
        for common in self.input_field['common_input']: #miniimize
            comm_input[common] = input('Enter the {}'.format(common))

        for differ in self.input_field[ip]:
            diff_input[differ] = input('Enter the {}'.format(differ))

        comm_input.update({'product_details':diff_input})
        return comm_input
        
    def delete_product(self, id):
        for index, products in enumerate(self.product):
            if(id == products['id']):
                self.product.pop(index)
        return self.product
        
