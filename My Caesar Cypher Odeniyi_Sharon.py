# Beginner-Friendly Caesar Cipher without Emojis

print("🔐 Welcome to the Caesar Cipher!")

# Ask the user what to do
mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
message = input("Enter your message: ")
keyword = input("Enter a keyword: ")

# Calculate shift value from keyword
shift = 0
for char in keyword:
    if char.isalpha():
        shift += ord(char.lower())
shift = shift % 26  # Keep it between 0–25

# Reverse shift if decrypting
if mode == 'decrypt':
    shift = -shift

# Go through each character
result = ""
for char in message:
    if char.isalpha():
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')
        new_char = chr((ord(char) - base + shift) % 26 + base)
        result += new_char
    else:
        result += char  # Keep spaces and punctuation

# Show the result
print("\nYour result is:")
print(result)

