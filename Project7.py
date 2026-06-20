binary_output = ' '.join(format(ord(char), '08b') for char in input("Enter letters only to convert it into binary: "))
print("Here is it in binary")
print(binary_output)