import csv
import random

# Output file name
filename = 'insurance_data.csv'

# Number of data points
num_rows = 100

# Generate and write data
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['age', 'bought_insurance'])  # header

    for _ in range(num_rows):
        age = random.randint(18, 55)
        
        if age < 35:
            bought_insurance = 0 if random.random() < 0.8 else 1
        else:
            bought_insurance = 1 if random.random() < 0.8 else 0

        writer.writerow([age, bought_insurance])

print(f"{num_rows} records written to '{filename}' successfully.")
