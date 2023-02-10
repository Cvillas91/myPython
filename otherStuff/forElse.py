
import threading
import time

numbers = [18, 14, 29, 109, 178, 44, 18, 36, 99, 103]

for number in numbers:
    if number % 5 == 0:
        print(f"Found a number! {number} is divisible by 5!")
        break
    else:
        print(f"{number} is not divisible by 5!")
else:
    print("No number divisible by 5 was found!")



done = False

def end_loop():
    global done
    input("Press enter to terminate loop...\n")
    done = True

threading.Thread(target=end_loop).start()

for i in range(18):
    print(i)
    if done:
        break
    time.sleep(1)
else:
    print("Loop completed without any manual interruption!")
