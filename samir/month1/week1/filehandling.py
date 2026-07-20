# Simple File Parser with TXT File

filename = "sample.txt"


def read_lines(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def write_lines(file_name, lines):
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def add_line(file_name, line_text):
    lines = read_lines(file_name)
    lines.append(line_text)
    write_lines(file_name, lines)
    print("Line added successfully.")


def update_line(file_name, line_number, new_text):
    lines = read_lines(file_name)
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_text
        write_lines(file_name, lines)
        print("Line updated successfully.")
    else:
        print("Invalid line number.")


def delete_line(file_name, line_number):
    lines = read_lines(file_name)
    if 1 <= line_number <= len(lines):
        removed = lines.pop(line_number - 1)
        write_lines(file_name, lines)
        print(f"Deleted line: {removed}")
    else:
        print("Invalid line number.")


def show_lines(file_name):
    lines = read_lines(file_name)
    if not lines:
        print("The file is empty.")
        return

    print("\nContents of the file:")
    for index, line in enumerate(lines, start=1):
        print(f"Line {index}: {line}")

    print("\nTotal lines:", len(lines))


if __name__ == "__main__":
    while True:
        print("\n===== FILE PARSER MENU =====")
        print("1. Add line")
        print("2. View file")
        print("3. Update line")
        print("4. Delete line")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to add: ")
            add_line(filename, text)

        elif choice == "2":
            show_lines(filename)

        elif choice == "3":
            line_no = int(input("Enter line number to update: "))
            new_text = input("Enter new text: ")
            update_line(filename, line_no, new_text)

        elif choice == "4":
            line_no = int(input("Enter line number to delete: "))
            delete_line(filename, line_no)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
