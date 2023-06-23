import os
import time
import glob
import tkinter as tk
from PIL import Image, ImageTk


def upload_video(_title, filename):
    # Start measuring the time taken to upload
    start_time = time.time()

    # Build the command to upload the video
    cmd = 'python upload.py --file ' + filename + ' --title ' + _title

    # Execute the command
    os.system(cmd)

    # Calculate the time taken to upload
    elapsed_time = time.time() - start_time

    print("Time taken to upload:", round(elapsed_time, 2), 'seconds')


def upload_videos():
    global folder_entry
    path = folder_entry.get()

    # Get all mp4 files from the specified folder path
    files = glob.glob1(path, '*.mp4')

    for file in files:
        # Print the file path
        print('\n' + os.path.join(path, file))

        # Set the video title as the file name
        title = str(file)

        # Call the main function to upload the video
        upload_video(title, os.path.join(path, file))


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("400x400")
    window.title("UploadMate")

    # Attaching background image
    img_loc = r'img.jpg'
    img = Image.open(img_loc)
    photo = ImageTk.PhotoImage(img)
    lab = tk.Label(image=photo)
    lab.pack()

    folder_content = tk.Label(window, text="Path to media folder: ", font=('calibre', 10, 'normal'))
    folder_content.place(x=40, y=40)
    folder_entry = tk.Entry(window, width=25, font=('calibre', 10, 'normal'))
    folder_entry.place(x=200, y=40)

    btn = tk.Button(window, text='Upload!', bd='5', command=upload_videos)
    btn.place(x=90, y=200)

    window.mainloop()