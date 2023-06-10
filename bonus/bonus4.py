def get_average():
    with open("temp.txt","r") as f:
        data = f.readlines()

    value = data[1:]

    value = [float(i) for i in value]

    average_local = sum(value) / len(value)
    return average_local

average = get_average()
print("The average of temperatures is:-",average)