date = input("Enter the date:")
rate = input ("rate your day out of 10!")
thoughts = input("How did u feel today??" '\n')

with open(f"../bonus/{date}.txt","w") as file:
    file.write("Date:-" + date + '\n')
    file.write("rating:-" + rate + 2*'\n')
    file.write("Thoughts on the day:-" + thoughts)