import time as t

a = input("Enter your name: ")
current_time = t.strftime("%H:%M:%S")
hour = int(current_time[:2])

if hour < 12:
    print(f"Good morning, {a}. Time is {current_time}")
    
elif hour < 17:
    print(f"Good afternoon, {a}. Time is {current_time}")
    
else:
    print(f"Good evening, {a}. Time is {current_time}")



