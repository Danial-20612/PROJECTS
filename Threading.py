import threading
import time

# task 1 (thread 1)
def print_numbers():
    for i in range(6):
        print(i)
        time.sleep(4)

# task 2 (thread 2)
def print_letters():
    for letter in ["A" , "B", "C", "D", "E", "F"]:
        print(letter)
        time.sleep(4)
    
# creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

start = time.time()

t1.start()
t2.start()

# waiting
t1.join()
t2.join()
end = time.time()

print("Both threads finished the program")
print("The program finished " , round(end - start, 2), "seconds")


