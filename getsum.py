print(list(sum(float(x.split(",")[1]) for x in open(f"Q_{i}.csv").read().split("\n")[1:-1]) for i in range(1, 11)))
