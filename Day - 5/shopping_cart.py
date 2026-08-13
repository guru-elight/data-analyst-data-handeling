import csv
import os


PRODUCT_FILE = "products.csv"
ORDER_FILE = "orders.csv"


class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def display(self):
        print(
            f"{self.product_id:<8}"
            f"{self.name:<20}"
            f"{self.category:<15}"
            f"{self.price:<10.2f}"
            f"{self.stock:<8}"
        )


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > product.stock:
            print("Insufficient stock available.")
            return

        if product.product_id in self.items:
            new_quantity = self.items[product.product_id]["quantity"] + quantity

            if new_quantity > product.stock:
                print("Requested quantity exceeds available stock.")
                return

            self.items[product.product_id]["quantity"] = new_quantity
        else:
            self.items[product.product_id] = {
                "product": product,
                "quantity": quantity
            }

        print("Product added to cart successfully.")

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print("Product removed from cart.")
        else:
            print("Product not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("\nCart Items")
        print("-" * 70)

        total = 0

        print(
            f"{'ID':<8}"
            f"{'Product':<20}"
            f"{'Quantity':<10}"
            f"{'Price':<10}"
            f"{'Subtotal':<10}"
        )

        print("-" * 70)

        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity

            print(
                f"{product.product_id:<8}"
                f"{product.name:<20}"
                f"{quantity:<10}"
                f"{product.price:<10.2f}"
                f"{subtotal:<10.2f}"
            )

            total += subtotal

        print("-" * 70)
        print(f"Total Amount: {total:.2f}")

    def calculate_total(self):
        total = 0

        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity

        return total

    def clear_cart(self):
        self.items.clear()


class ShoppingApplication:
    def __init__(self):
        self.products = []
        self.cart = ShoppingCart()
        self.categories = set()

        self.load_products()

    def create_product_file(self):
        if not os.path.exists(PRODUCT_FILE):
            products = [
                ["P101", "Laptop", "Electronics", 55000, 10],
                ["P102", "Headphones", "Electronics", 2500, 20],
                ["P103", "Keyboard", "Accessories", 1500, 15],
                ["P104", "Backpack", "Bags", 1800, 12],
                ["P105", "Mouse", "Accessories", 800, 25],
                ["P106", "Smart Watch", "Electronics", 4500, 8]
            ]

            with open(PRODUCT_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["ID", "Name", "Category", "Price", "Stock"]
                )
                writer.writerows(products)

    def load_products(self):
        self.create_product_file()

        try:
            with open(PRODUCT_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    product = Product(
                        row["ID"],
                        row["Name"],
                        row["Category"],
                        float(row["Price"]),
                        int(row["Stock"])
                    )

                    self.products.append(product)
                    self.categories.add(product.category)

        except (FileNotFoundError, ValueError):
            print("Unable to load product data.")

    def display_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nAvailable Products")
        print("-" * 70)

        print(
            f"{'ID':<8}"
            f"{'Product':<20}"
            f"{'Category':<15}"
            f"{'Price':<10}"
            f"{'Stock':<8}"
        )

        print("-" * 70)

        for product in self.products:
            product.display()

        print("-" * 70)

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def add_to_cart(self):
        self.display_products()

        product_id = input("Enter Product ID: ").strip().upper()

        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return

        try:
            quantity = int(input("Enter Quantity: "))
            self.cart.add_item(product, quantity)

        except ValueError:
            print("Invalid quantity. Please enter a number.")

    def remove_from_cart(self):
        self.cart.view_cart()

        if not self.cart.items:
            return

        product_id = input(
            "Enter Product ID to remove: "
        ).strip().upper()

        self.cart.remove_item(product_id)

    def search_product(self):
        search_term = input(
            "Enter product name or category: "
        ).strip().lower()

        found = False

        print("\nSearch Results")
        print("-" * 70)

        for product in self.products:
            if (
                search_term in product.name.lower()
                or search_term in product.category.lower()
            ):
                product.display()
                found = True

        if not found:
            print("No matching products found.")

    def checkout(self):
        if not self.cart.items:
            print("Your cart is empty.")
            return

        self.cart.view_cart()

        confirm = input(
            "\nConfirm purchase? (yes/no): "
        ).strip().lower()

        if confirm != "yes":
            print("Checkout cancelled.")
            return

        total = self.cart.calculate_total()

        try:
            with open(ORDER_FILE, "a", newline="") as file:
                writer = csv.writer(file)

                for item in self.cart.items.values():
                    product = item["product"]
                    quantity = item["quantity"]

                    writer.writerow([
                        product.product_id,
                        product.name,
                        quantity,
                        product.price,
                        product.price * quantity
                    ])

                    product.stock -= quantity

            print(f"Payment successful.")
            print(f"Total amount paid: {total:.2f}")
            print("Order placed successfully.")

            self.cart.clear_cart()

        except OSError:
            print("Unable to save order details.")

    def show_categories(self):
        if not self.categories:
            print("No categories available.")
            return

        print("\nAvailable Categories")

        for category in sorted(self.categories):
            print(f"- {category}")

    def run(self):
        while True:
            print("\n========== Shopping Cart System ==========")
            print("1. View Products")
            print("2. Search Products")
            print("3. View Categories")
            print("4. Add Product to Cart")
            print("5. Remove Product from Cart")
            print("6. View Cart")
            print("7. Checkout")
            print("8. Exit")
            print("==========================================")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_products()

            elif choice == "2":
                self.search_product()

            elif choice == "3":
                self.show_categories()

            elif choice == "4":
                self.add_to_cart()

            elif choice == "5":
                self.remove_from_cart()

            elif choice == "6":
                self.cart.view_cart()

            elif choice == "7":
                self.checkout()

            elif choice == "8":
                print("Thank you for using the Shopping Cart System.")
                break

            else:
                print("Invalid choice. Please select 1 to 8.")


if __name__ == "__main__":
    application = ShoppingApplication()
    application.run()