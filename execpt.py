import os

# def create_file(filename):
#     try:
#         with open(filename, 'w') as f:
#             f.write("Hello, World!\n")
#         print("File '" + filename + "' created successfully.")
#     except:
#         print("Error: could not create file '" + filename + "'")

# def read_file(filename):
#     try:
#         with open(filename, 'r') as f:
#             contents = f.read()
#         print(contents)
#     except:
#         print("Error: could not read file '" + filename + "'")

# def append_to_file(filename, text):
#     try:
#         with open(filename, 'a') as f:
#             f.write(text)
#         print("Text appended to file '" + filename + "' successfully.")
#     except:
#         print("Error: could not append to file '" + filename + "'")

# def rename_file(filename, new_filename):
#     try:
#         os.rename(filename, new_filename)
#         print("File" + filename + " renamed to '" + new_filename + "'")

#     except IDError:
#         print("Error: could not rename file '" + filename + "'")

# def delete_file(filename):
#     try:
#         os.remove(filename)
#         print("File" + filename + "deleted successfuly")
#     except IDError:
#         print("Could not delete file:" + filename)

# if __name__ == "__main__":
#     filename = "example2.txt"
#     new_filename = "new_example.txt"

#     create_file(filename)
#     read_file(filename)
#     append_to_file(filename , "This is some additional text.\n")
#     read_file(filename)
#     rename_file(filename , new_filename)
#     read_file(new_filename)
#     delete_file(new_filename)



# # open file 
# with open("sample3.txt" , "r") as file:
#     print(file.read())

# if os.path.exists("sample3.txt"):
#     print("File exists: ")
# else:
#     print("File not found: ")
 
numbers = []
while True:
    for i in range(4):
        numbers = int(input("Enter a numbers: "))
        
    
print(numbers)
