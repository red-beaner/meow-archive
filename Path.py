from pathlib import Path

# === SETTINGS ===
input_file = "art.html"         # Your large HTML fragment
lines_per_chunk = 500             # Adjust this based on how big each file should be
output_prefix = "artpart"            # Output file prefix: part1.html, part2.html, etc.

# === SCRIPT START ===
with open(input_file, encoding="utf-8") as f:
    lines = f.readlines()

# Split into chunks
for i in range(0, len(lines), lines_per_chunk):
    chunk = lines[i:i + lines_per_chunk]
    part_num = (i // lines_per_chunk) + 1
    output_file = f"{output_prefix}{part_num}.html"

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("<!DOCTYPE html>\n<html>\n<head>\n")
        out.write(f"<meta charset='UTF-8'>\n<title>Part {part_num}</title>\n</head>\n<body>\n")
        out.writelines(chunk)
        out.write("\n</body>\n</html>")

    print(f"Created {output_file} with {len(chunk)} lines.")
