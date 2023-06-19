import os
import time
import glob


def main(_title, filename):
    # Start measuring the time taken to upload
    start_time = time.time()

    # Build the command to upload the video
    cmd = 'python upload.py --file ' + filename + ' --title ' + _title

    # Execute the command
    os.system(cmd)

    # Calculate the time taken to upload
    elapsed_time = time.time() - start_time

    print("Time taken to upload:", round(elapsed_time, 2), 'seconds')


if __name__ == '__main__':
    # Get the folder path from the user
    path = input('Enter folder path: ')

    # Get all mp4 files from the specified folder path
    files = glob.glob1(path, '*.mp4')

    for file in files:
        # Print the file path
        print('\n' + os.path.join(path, file))

        # Set the video title as the file name
        title = str(file)

        # Call the main function to upload the video
        main(title, os.path.join(path, file))
