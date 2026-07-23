# SIMPLE KEY-VALUE FILE PARSER

def parse_custom_file(file_path):
    """Reads a text file and parses key-value pairs into structured data."""
    parsed_data = []
    current_record = {}

    try:
        # Open the file safely using 'with'
        with open(file_path, 'r') as file:
            for line in file:
                # Remove extra whitespace and skip completely blank lines
                line = line.strip()
                if not line:
                    continue
                
                # Split each line by the first colon ':' found
                if ":" in line:
                    key, value = line.split(":", 1)
                    
                    # Clean up keys and values (remove spaces)
                    key = key.strip()
                    value = value.strip()
                    
                    # If we hit 'Name', it means a new person's record is starting
                    if key == "Name" and current_record:
                        parsed_data.append(current_record)
                        current_record = {} # Reset for the next record
                    
                    # Save the key-value pair to the current record
                    current_record[key] = value

            # Don't forget to append the final record after the loop finishes
            if current_record:
                parsed_data.append(current_record)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return []

    return parsed_data

# --- Execution Example ---
if __name__ == "__main__":
    # 1. Create a dummy file to parse
    with open("Text_Files/data.txt", "w") as f:
        f.write("Name: Alice\nAge: 25\nRole: Data Intern\n\nName: Bob\nAge: 30\nRole: Developer")

    # 2. Run the parser
    result = parse_custom_file("Text_Files/data.txt")
    
    # 3. Print the cleanly structured output
    print("Successfully Parsed Data:")
    for record in result:
        print(record)