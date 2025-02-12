class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"

def main():
    products = {}
    while True:
        print("\n1. Add a new product")
        print("2. Update stock of a product")
        print("3. View product details")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            name = input("Enter product name: ").strip()
            if name in products:
                print("Error: Product already exists.")
                continue
            try:
                price = float(input("Enter product price: "))
                stock = int(input("Enter product stock: "))
                products[name] = Product(name, price, stock)
                print("Product added successfully!")
            except ValueError:
                print("Invalid input. Please enter valid numbers for price and stock.")
        
        elif choice == '2':
            name = input("Enter product name to update: ").strip()
            if name not in products:
                print("Error: Product not found.")
                continue
            try:
                quantity = int(input("Enter quantity to add/remove: "))
                products[name].update_stock(quantity)
                print("Stock updated successfully!")
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")
        
        elif choice == '3':
            name = input("Enter product name: ").strip()
            if name not in products:
                print("Error: Product not found.")
                continue
            print(products[name])
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()