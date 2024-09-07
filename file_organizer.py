import os
import shutil

DIRECTORY_TO_ORGANIZE = r'C:\Users\Startklar\Downloads'

FOLDER_NAMES = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['txt', 'pdf', 'docx', 'xlsx'],
    'Videos': ['mp4', 'avi', 'mov'],
    'Archives': ['zip', 'rar', 'tar']
}


def file_organizer(directory):

    # Create folders if they don't exist
    for folder_name in FOLDER_NAMES.keys():
        folder_path = os.path.join(directory, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files to corresponding folders
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Indicates if current file is of unknown type
        unknown_type = True

        if os.path.isfile(file_path):
            file_extension = file_name.split('.')[-1].lower()

            for folder, extensions in FOLDER_NAMES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, folder)

                    shutil.move(file_path, os.path.join(destination_folder, file_name))
                    unknown_type = False
                    break

            # If the file is of unknown type, 'Others' folder is created in case it does not already exist
            # The file is then stored in this folder
            if unknown_type:
                destination_folder_path = os.path.join(directory, 'Others')

                if not os.path.exists(destination_folder_path):
                    os.makedirs(destination_folder_path)

                shutil.move(file_path, os.path.join(destination_folder_path, file_name))


if __name__ == '__main__':
    file_organizer(DIRECTORY_TO_ORGANIZE)
    print('Directory is successfully organized!')