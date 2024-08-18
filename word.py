
import os

import os

def replace_first_word_in_files(folder_path, replacements):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Process only .txt files
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            # Read the file content
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Process each line
            updated_lines = []
            for line in lines:
                # Split the line into words
                words = line.split()
                
                # Check if the first word is in the dictionary
                if words and words[0] in replacements:
                    # Replace the first word with the corresponding value from the dictionary
                    words[0] = replacements[words[0]]

                # Join the words back into a line
                updated_line = ' '.join(words)
                updated_lines.append(updated_line)

            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.writelines(updated_lines)
            print(f'Processed file: {filename}')




folder_path = 'data/palmdata/train/labels'
replacements = {
    'Tree': "0"
}

replace_first_word_in_files(folder_path, replacements)
