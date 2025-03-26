# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

def main():
    words = input("Enter a comma separated sequence of words: ").split(",")
    words = list(set(words))
    words.sort()
    print("Unique words in sorted form: ", end="")
    print(", ".join(words))

if __name__ == "__main__":
    main()
    