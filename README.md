# UploadMate

UploadMate is a Python-based terminal application that allows seamless uploading of videos to YouTube.

## Setup

Follow the steps below to set up the project:

1. Go to [Google Cloud Console](https://console.developers.google.com/).

2. Sign in to your Google Cloud account.

3. Create credentials by navigating to APIs & Services -> Credentials -> Create Credentials -> OAuth Client ID.

4. Choose the Desktop Application option.

5. Download the client ID JSON file as client_secret.json.

6. Enable the YouTube Data API v3 in the Library section of the Google Cloud Console.

7. Publish, Authenticate and Grant permission to your application to manage YouTube videos.

8. Install the required dependencies by running:
   
        pip install -r requirements.txt

## Screenshots

![Screenshot (30)](https://github.com/gv1shnu/UploadMate/assets/121789146/a1a1c383-65c7-4fe6-8d79-e2604f376d99)

## Usage

To upload a video, follow these steps:

1. Ensure that the video file path does not contain any spaces.
2. Run main program with the required parameters.
3. The video will be uploaded to YouTube.

Please note that the uploader currently supports Mp4 videos up to 1080p resolution. 
Videos with higher resolutions and other formats cannot be processed and uploaded.

## Disclaimer

This project is for educational purposes only. Use it responsibly and in compliance with YouTube's terms of service.

## License

This project is licensed under the [MIT License](LICENSE).