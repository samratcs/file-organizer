# File Organizer

A simple Python automation tool that organizes files into folders based on their file types.

## Features

- Organizes images
- Organizes documents
- Organizes videos
- Organizes audio files
- Organizes archives
- Places unknown file types into an `Others` folder

## Supported File Types

| Category | Extensions |
|---|---|
| Images | JPG, JPEG, PNG, GIF, WEBP |
| Documents | PDF, DOC, DOCX, TXT, XLSX, CSV |
| Videos | MP4, MKV, AVI, MOV |
| Audio | MP3, WAV, FLAC |
| Archives | ZIP, RAR, 7Z |

## Project Structure

```text
file-organizer/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   └── organizer.py
└── tests/
    └── test_organizer.py

```
## How to Run

Clone the repository:

- git clone https://github.com/YOUR_USERNAME/file-organizer.git

Go to the project:

- cd file-organizer

Run the program:

- python src/organizer.py

Enter the folder you want to organize.

Example

Before:

Downloads/
├── photo.jpg
├── report.pdf
├── movie.mp4
└── song.mp3

After:

Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Videos/
│   └── movie.mp4
└── Audio/
    └── song.mp3

## Technologies
- Python
- pathlib
- shutil


---


# Part 7 — Add requirements


Your current project doesn't need an external package, so `requirements.txt` can contain:


```text
# No external dependencies required

```

