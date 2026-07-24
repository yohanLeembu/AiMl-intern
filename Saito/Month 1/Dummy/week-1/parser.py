def parser_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("===== Parsed File Content =====")
        print(f"total lines: {len(lines)}")

        for number, line in enumerate(lines, start=1):
            print(f"Line {number}: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"an eroor occurred: {e}")

def main():
    filename = input("Enter the filename to parse: ")
    parser_file(filename)

if __name__ == "__main__":
    main()