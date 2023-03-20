

import os
import shutil
import time

now = time.time()

# path to download folder
download_folder = "C:/Users/user/Downloads"

# path to to_delete folder
to_delete_folder = "C:/Users/user/Downloads/to_delete"

# loop through files in download folder
for f in os.listdir(download_folder):

    # get the path to the file
    file_path = os.path.join(download_folder, f)

    # get the last modified time of the file
    last_modified_time = os.path.getmtime(file_path)

    # check if the file is older than 30 days
    if (now - last_modified_time) > (30 * 24 * 60 * 60):

        # move the file to to_delete folder
        shutil.move(file_path, to_delete_folder)