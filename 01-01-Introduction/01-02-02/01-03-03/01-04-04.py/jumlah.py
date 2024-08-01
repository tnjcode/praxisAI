string = "budimukidi"
huruf_count = {}

for huruf in string:
    if huruf in huruf_count:
        huruf_count[huruf] += 1
    else:
        huruf_count[huruf] = 1

for huruf, count in huruf_count.items():
    print(f"{huruf}:{count}")