MINIMUM_LENGTH = 4


def main():
    password = password_length(MINIMUM_LENGTH)
    password_asterisk(password)


def password_length(minimum_length):
    password = input("Enter a password: ")
    while minimum_length > len(password):
        print("Error: Password length invalid! Password length must be at least 4.")
        password = input("Please enter a password: ")
    return password


def password_asterisk(password):
        print("*" * len(password))


main()
