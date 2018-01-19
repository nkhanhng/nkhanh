n = int(input("What time is it?"))
w = int(input("The number of hours do u want to wait?"))

# i = w // 24
s = n + (w - w//24)

print("The clock will goes off at", s,"o'clock")
