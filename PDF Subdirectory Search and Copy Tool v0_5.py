# v0.5
# pdf folder below given directory
# adds files by date modified, use this to sort

import os
import shutil

def sort_files_by_modification_date(files):
    # Function to sort files by modification date in descending order
    return sorted(files, key=lambda x: os.path.getmtime(x), reverse=True)

def search_pdfs_and_create_folder(main_directory):
    try:
        # Validate if main_directory exists
        if not os.path.exists(main_directory):
            raise FileNotFoundError(f"The directory '{main_directory}' does not exist.")

        # Determine if the path is a network path
        if os.path.isdir(main_directory) and main_directory.startswith('\\\\'):
            raise OSError(f"Network path '{main_directory}' not supported for folder creation.")

        # Create the new folder name
        new_folder_name = f"All Reports {os.path.basename(main_directory)}"
        new_folder_path = os.path.join(main_directory, new_folder_name)

        # Create the new folder if it doesn't exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        else:
            print(f"The folder '{new_folder_path}' already exists.")

        # Search for PDFs in subdirectories and sort them by modification date
        for root, dirs, files in os.walk(main_directory):
            pdf_files = [os.path.join(root, file) for file in files if file.lower().endswith(".pdf")]
            pdf_files_sorted = sort_files_by_modification_date(pdf_files)

            # Copy PDF files to the new folder
            for file in pdf_files_sorted:
                src_path = file
                dst_path = os.path.join(new_folder_path, os.path.basename(file))
                try:
                    shutil.copy2(src_path, dst_path)
                    print(f"Copied '{os.path.basename(file)}' to '{new_folder_path}'")
                except FileNotFoundError:
                    print(f"File '{os.path.basename(file)}' not found.")

        print(f"All PDF files have been copied to '{new_folder_path}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    main_directory = input("Enter the main directory path: ")
    search_pdfs_and_create_folder(main_directory)
