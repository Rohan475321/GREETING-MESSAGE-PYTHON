# Exercise 2
# GOOD MORNING SIR

# import time
# timestamp=(time.strftime('%H:%M:%S'))
# print(timestamp)

# timestamp=int(time.strftime('%H'))
# print(timestamp)
# timestamp=int(time.strftime('%M'))
# print(timestamp)
# timestamp=int(time.strftime('%S'))
# print(timestamp)


a=int(input("enter time in 24 hr"))

if(a>4 and a<12):
    print("GOOD MORNING SIR")
elif(a>=12 and a<16):
    print("GOOD AFTERNOON SIR")
elif(a>=16 and a<20):
    print("GOOD EVENING SIR")
else:
    print("GOOD NIGHT SIR")