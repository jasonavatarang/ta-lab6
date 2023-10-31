def encode(password: str) -> str:
  return ' '.join(str(int(num) + 3) for num in password)


def decode(encoded_password):
  # partner codes this
  encoded_password= list(encoded_password)
  for i in range(0, len(encoder)):
    # if encoder[i] - 3 is less than 0
    if encoded_password[i] == '0':
      encoded_password[i] = '7'
    elif  encoded_password[i] == '1':
      encoded_password[i] = '8'
    elif  encoded_password[i] == '2':
      encoded_password[i] = '9'
    else:
      encoded_password[i] = int(encoded_password[i])
      encoded_password[i] = str(encoder[i] - 3)
  password = ''.join(encoded_password)
  return password


def main():
  menu_option = None
  password = ""
  encoded_password = ""
  while menu_option != '3':
      menu_option = input("Please enter an option: ")
      # Jason edit: encode password (add 3 to each int in string)
      if menu_option == '1':
          password = input("Please enter your password to encode: ")
          encoded_password = encode(password=password)
          print("Your password has been encoded and stored!")
      elif menu_option == '2':
          pass
          print(f"The encoded password is {encoded_password}, and the original password is {password}.")


if __name__ == '__main__':
  main()
