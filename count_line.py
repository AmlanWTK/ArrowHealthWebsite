import os

extensions = [".html", ".css", ".js"]

total_lines = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                lines = len(f.readlines())

            print(f"{path}: {lines} lines")
            total_lines += lines

print("----------------------")
print(f"Total lines of code: {total_lines}")