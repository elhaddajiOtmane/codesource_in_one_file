import glob

# Function to concatenate all .js files into one
def concatenate_js_files(start_path, output_file_path):
    # Find all .js files within the directory, including subdirectories
    js_files = [y for x in os.walk(start_path) for y in glob.glob(os.path.join(x[0], '*.js'))]
    
    # Open the output file (or create it if it doesn't exist)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in js_files:
            # Write the file path as a comment for reference
            output_file.write(f'// File: {file_path}\n')
            # Read the current file's content and write it to the output file
            with open(file_path, 'r', encoding='utf-8') as current_file:
                output_file.write(current_file.read())
            # Add a couple of newlines for separation
            output_file.write('\n\n')
                
# Path to the combined file
combined_file_path = '/mnt/data/combined.js'

# Concatenate all .js files
concatenate_js_files(extracted_folder_path, combined_file_path)

# Return the path for download
combined_file_path
