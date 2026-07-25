import time
user = int(input("Enter your time:"))
user = user + 1
for i in range(1, user):
    print(i)
    time.sleep(1)
print("Done.")