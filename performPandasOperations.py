# Description: This script automates pandas operations from the command line. It reads operations from a file, applies them to a CSV file, and outputs the result.
import sys

def main():
    # Check if the filenames are provided as command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <data_filename> <operations_filename>")
        sys.exit(1)

    # Get the filenames from the command line arguments
    data_filename = sys.argv[1]
    operations_filename = sys.argv[2]

    # Prompt the user for the delimiter
    delimiter = input("Please enter the delimiter used in the file: ")

    # Load the data file into a DataFrame
    try:
        df = pd.read_csv(data_filename, delimiter=delimiter, dtype=str, encoding='utf-8')
    except Exception as e:
        print(f"Error reading the data file: {e}")
        sys.exit(1)

    # Read and execute each operation from the operations file
    try:
        with open(operations_filename, 'r', encoding='utf-8') as file:
            operations = file.readlines()

        # Use a dictionary to store the DataFrame and update it within exec
        local_vars = {'df': df}

        for operation in operations:
            operation = operation.strip()
            if operation:  # Ignore empty lines
                exec(operation, {}, local_vars)
        
        # Update the DataFrame after executing all operations
        df = local_vars['df']

    except Exception as e:
        print(f"Error processing operations file: {e}")
        sys.exit(1)

    # Output the DataFrame to a CSV file with the same delimiter
    try:
        df.to_csv('output.csv', index=False, sep=delimiter, encoding='utf-8')
        print("Output saved to output.csv")
    except Exception as e:
        print(f"Error writing the output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
