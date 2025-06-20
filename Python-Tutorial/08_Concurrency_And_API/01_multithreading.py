# Multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time 

def walk_dog(first,last):
    time.sleep(1)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_mail():
    time.sleep(4)
    print("you get the mail")

# create threads for each chore
chore1 = threading.Thread(target = walk_dog, args=("Scooby","Doo"))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

# start threads
chore1.start()
chore2.start()
chore3.start()

# join()function ensure that all tasks are completed before proceeding 
chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")
