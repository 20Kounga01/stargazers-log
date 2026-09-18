age = 60
if age >= 18 and age < 30: 
   print("You are an adult.")
elif age > 30 and age < 60:
    print("You are in your prime.")
elif age < 18:
    print("You are a minor.")
elif age < 15:
    print("You are a child.")
elif age == 60:
    print("You are a senior.")
else:
    print("You are not a human.")

for b in range(10):
 for b in range(5):
    pass
 if b % 2 != 0:
    continue
 
 print(b)    

for outer_number in range(10):
    for inner_number in range(5):
        pass

    if outer_number % 2 != 0:
        continue

    print(outer_number)