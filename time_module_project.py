import time as t

a = input("Enter your name: ")

if t.strftime("%H:%M:%S") < "12:0:0":
    print(f"Good morning,{a} .Time is {t.strftime('%H:%M:%S')}")
    
elif t.strftime("%H:%M:%S") >= "12:0:0" and t.strftime("%H:%M:%S") < "17:0:0":
    print(f"Good afternaoon,{a} .Time is {t.strftime('%H:%M:%S')}")
    
elif t.strftime("%H:%M:%S") >= "17:0:0":
    print(f"Good evening,{a} .Time is {t.strftime('%H:%M:%S')}")



