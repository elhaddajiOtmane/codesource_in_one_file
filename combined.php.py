
import glob
import os

def concatenate_php_files(start_path, output_file_path):
    """
    Concatenates all .php files within a directory and its subdirectories into one file.
    """
    # Find all .php files within the directory, including subdirectories
    php_files = [y for x in os.walk(start_path) for y in glob.glob(os.path.join(x[0], '*.php'))]

    # Open the output file (or create it if it doesn't exist)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in php_files:
            # Write the file path as a comment for reference
            output_file.write(f'// File: {file_path}\n')
            # Read the current file's content and write it to the output file
            with open(file_path, 'r', encoding='utf-8') as current_file:
                output_file.write(current_file.read())
            # Add a couple of newlines for separation
            output_file.write('\n\n')

# Example usage:
extracted_folder_path = 'app.mygoodies.fr' 
combined_file_path = 'combined.php'        
concatenate_php_files(extracted_folder_path, combined_file_path)

print(f"Combined PHP file created at: {combined_file_path}")
