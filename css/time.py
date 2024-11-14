import time
my_counter = 0
max_count = 25
while my_counter < max_count: 
    my_counter += 1
    print("current count: " + str(my_counter))
    time.sleep(2)

print("Loop has ended.")





#import time  

#my_counter = 0  
#while True: 
# my_counter += 1 
# print("current count: " + str(my_counter))  
# stop = input("Press 'q' to stop or Enter to continue: ")
# if stop.lower() == 'q':
# print("Loop has ended.") 
# break
# "break" works as a way of exiting the loop