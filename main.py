def main():
    menu_option = None
    password = ""
    encoded_password = ""
    while menu_option != '3':
        menu_option = input("Please enter an option: ")
        # Jason edit: encode password (add 3 to each int in string)
        if menu_option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = ""
            for num in password:
                encoded_password += str(int(num) + 3)
            print("Your password has been encoded and stored!")
        elif menu_option == '2':
            pass
            # print(f"The encoded password is {encoded_password}, and the original password is {password}.")


if __name__ == '__main__':
    main()
