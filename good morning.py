import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
name = input("Enter Your Name:- ").title()
hour=int(time.strftime("%H"))
if 4 <= hour <12:
    print("good mronig",name)
elif 12 <= hour < 17:
  print("Good Afternoon", name)
elif 17 <= hour < 21:
  print("Good Evening", name)
else:
  print("Good Night", name)