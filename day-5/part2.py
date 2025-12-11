id_ranges = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        a, b = map(int, line.split('-'))
        id_ranges.append((a, b))

# Sort by start value
id_ranges.sort()

merged = []
for start, end in id_ranges:
    if not merged:
        merged.append([start, end])
        continue

    last_start, last_end = merged[-1]

    # Overlap?
    if start <= last_end:
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])

# Count all fresh IDs
total = 0
for start, end in merged:
    total += end - start + 1

print("Total fresh IDs:", total)