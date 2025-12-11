id_ranges = []
ids = []

with open("input.txt") as f:
    is_range_section = True
    for line in f:
        line = line.strip()
        if not line:
            is_range_section = False
            continue
        
        if is_range_section:
            id_ranges.append(line)
        else:
            ids.append(int(line))

# print("id_ranges:", id_ranges)
# print("ids:", ids)

answer = 0

for i in range(len(id_ranges)):
    start, end = map(int, id_ranges[i].split('-'))
    id_ranges[i] = (start, end)

for id in ids:
    for start, end in id_ranges:
        if start <= id <= end:
            answer += 1
            break

print("answer:", answer)