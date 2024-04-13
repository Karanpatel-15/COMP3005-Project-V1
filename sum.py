results = []
for i in range(1, 11):
    try:
        with open(f"Q_{i}.csv") as file:
            next(file)  # Skip the header
            total = sum(float(line.split(",")[1]) for line in file if line.strip())
        results.append((i, total))  # Store question number and sum
    except FileNotFoundError:
        continue  # Skip file if not found

for result in results:
    print(f"Question {result[0]}: {result[1]}")
