# PyMedia Downloader Tool
A simple and fast tool built with Python to download media (video and audio) from various online sources using the powerful yt-dlp library.
Features

    1.Interactive command-line.
    2.Ability to download only video or only audio files.
    3.Displays a list of available quality and format options for selection.
    4.Option to choose a custom save path or use the current directory.

## Prerequisites
To run this code, you must have Python installed on your system.
### How to Run (For End Users)
Follow these steps to get the tool running on your machine:
1. Clone the Repository.
2. Install Required Libraries
Navigate into the project directory using your Terminal or Command Prompt and install all necessary libraries listed in the requirements.txt file using the following command:
`pip install -r requirements.txt`
3. Run the Tool
After successfully installing the requirements, you can run the script using the Python command:
`python your_script_name.py` or `python3 your_script_name.py` if you are on Linux/macOS
4. Usage Instructions
### When the script runs, you will see a welcome message and the logo. You will then be prompted to:
    1.Paste the media link (e.g., a YouTube link, or any site supported by yt-dlp).
    2.Choose the Type: Enter v for Video or a for Audio.
    3.Enter the Format ID: Select the numerical ID for your preferred quality/resolution from the displayed list.
    4.Specify the Save Path: Choose whether to save to the current path (y/n).
