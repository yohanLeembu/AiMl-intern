def parse_file(sample_file):
    try:
        with open(sample_file, 'r') as file:
            content = file.read()

        line = content.splitlines()
        words = content.split()
        characters = len(content)

        print("===== file contents =====")
        print(content)

        print("\n===== file statistics =====")
        print(f"Number of lines: {len(line)}")
        print(f"Number of words: {len(words)}") 
        print(f"Number of characters: {characters}")

    except FileNotFoundError:
        print(f"Error: The file '{sample_file}' was not found.")

def main():
    sample_file = input("Enter the path to the file you want to parse: ")
    parse_file(sample_file)

if __name__ == "__main__":
    main()
    