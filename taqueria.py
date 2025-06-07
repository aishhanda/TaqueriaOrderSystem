menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0  # global variable

def main():
    print("📋 Menu:")
    for item in menu:
        print(f"{item}: ${menu[item]:.2f}")  # fixed f-string for clean display

    while True:
        try:
            items = input("Item: ").title()
            result = bill(items)
            if result:
                print(result)
        except EOFError:
            print("\nOrder complete.")
            break

def bill(items):
    global total
    if items in menu:
        total += menu[items]
        return f"Total: ${total:.2f}"

