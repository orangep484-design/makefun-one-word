# make.fun entry: The Internet in One Word
# Writes a single word to /output/entry.txt
import os

WORD = "echo"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print("wrote:", WORD)

if __name__ == "__main__":
    main()
