import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pipelines')))
import shutil


class MoveTextFiles:
    
    def __init__(self,source_folder, destination_folder):
        self. source_folder = source_folder, 
        self. destination_folder = destination_folder

    def move_txt_files(self):
        
        # Checking if the destination folder exists, if it does not, it will create it.
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

        # Listing all the files in the source folder
        self.files = os.listdir(self.source_folder)

        for file in self.files:
            # Checking files with .txt extension
            if self.file.endswith('.txt'):
                self.source_file = os.path.join(self.source_folder, 
                                        self.file)
                self.destination_file = os.path.join(self.destination_folder, 
                                                self.file)
                # Moving the file to the new destination
                shutil.move(self.source_file, self.destination_file)
                print(f'I moved: {self.source_file} -> {self.destination_file}')