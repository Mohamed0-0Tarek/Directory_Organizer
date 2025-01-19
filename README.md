# File Organizer App 🔐

## Overview
The **File Organizer App** is a user-friendly tool designed to help you organize files in a selected directory into categorized subfolders. With a simple and intuitive GUI powered by **Tkinter**, this app makes file management effortless and efficient.

---

## Features
- **Categorized Organization**: Automatically sorts files into categories like Videos, Images, Music, Documents, Archives, and more.
- **Customizable Categories**: Easily extend or modify the file categories and their associated extensions.
- **Graphical User Interface (GUI)**: No command-line interaction needed—just select a directory and click!
- **Error Handling**: Handles unexpected issues gracefully and provides helpful error messages.
- **Logging**: Keeps a detailed log of all actions in a `file_organizer.log` file for review and debugging.

---

## How It Works
1. **Select Directory**: Use the "Select Directory" button to choose the folder you want to organize.
2. **File Sorting**: The app identifies files by their extensions and moves them to appropriate subfolders.
3. **Completion**: A success message will notify you once the organization process is complete.

---

## Categories
The app supports the following file categories by default:

| Category       | Extensions                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Videos**     | `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.wmv`, `.webm`                    |
| **Images**     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp`          |
| **Music**      | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`, `.wma`                    |
| **Documents**  | `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.txt`, `.ppt`, `.pptx`, `.odt`  |
| **Archives**   | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`                               |
| **Executables**| `.exe`, `.bat`, `.sh`, `.bin`, `.msi`                                      |
| **Programming**| `.py`, `.java`, `.cpp`, `.c`, `.js`, `.html`, `.css`, `.php`, `.json`, `.xml` |
| **Others**     | Files that don't match any of the above categories                         |

You can add or modify these categories in the code to fit your specific needs.

---

## Requirements
- **Python 3.x**
- **Tkinter** (Included in the standard Python library)

---

## Installation
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-repo/file-organizer-app.git
   cd file-organizer-app
   ```
2. Run the script:
   ```bash
   python file_organizer_gui.py
   ```

---

## Usage
1. Launch the app by running the script.
2. Click **"Select Directory"** to choose the folder you want to organize.
3. Sit back and let the app sort your files into neatly categorized subfolders!

---

## Logging
All actions performed by the app are logged in a file named `file_organizer.log`. This includes:
- Files moved and their destinations.
- Any errors encountered during the process.

---

## Screenshots
![image](https://github.com/user-attachments/assets/62471b2a-1223-4722-852d-c93ec0cd290b)

![image](https://github.com/user-attachments/assets/65a8892e-c12b-48b4-8203-db619cf0264c)

---

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements.



