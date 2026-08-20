from pathlib import Path
import shutil


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(extension):
    """Return the category for a given file extension."""
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files(folder_path):
    """Organize files in a folder according to their file types."""
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    for file in folder.iterdir():

        if not file.is_file():
            continue

        category = get_category(file.suffix)

        destination = folder / category
        destination.mkdir(exist_ok=True)

        shutil.move(str(file), str(destination / file.name))

    print("Files organized successfully!")


if __name__ == "__main__":
    folder = input("Enter folder path: ")
    organize_files(folder)