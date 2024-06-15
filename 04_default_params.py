def say_hello(name, email=None, address=None):
    print(f"Hello {name}.")

    if address:
        print(f"You live in {address}")
    
    if email:
        print(f"Your email is {email}")

say_hello("Csaba", address="Pécs")