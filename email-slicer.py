def main():
    print("Welcome to the email slicer\n")
    
    email_input = input("Ingresa tu mail ")
    (username,domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")
    
main()