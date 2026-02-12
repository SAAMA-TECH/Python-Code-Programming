'''AIM: Develop a Python program that reads a text file and prints words of specified lengths
(e.g.,) three,four,five,etc.) found within the file.
Name: Sayyed Affan Ahmed Maqsood Ahmed
UIN: 251P088'''

print("Word Length Filter from file")
file_path ="Sample.txt"
length = int(input("Enter the word length to filter: "))
with open(file_path,'r') as file:
    content = file.read()
    words = content.split()
    filtered_words = []
    for word in words:
        if len(word) == length:
            filtered_words.append(word)
    print(f"Words of length(length):")
    for word in filtered_words:
        print(word)
