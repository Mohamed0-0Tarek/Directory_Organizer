import os
import shutil
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

# Configure logging
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define file categories and their extensions
file_categories = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Executables": [".exe", ".bat", ".sh", ".bin", ".msi"],
    "Others": []  # For files that don't match any category
}

def organize_files(directory):
    try:
        # Ensure the directory exists
        if not os.path.exists(directory):
            logging.error(f"The directory '{directory}' does not exist.")
            messagebox.showerror("Error", f"The directory '{directory}' does not exist.")
            return

        logging.info(f"Organizing files in directory: {directory}")

        # Create subdirectories for each category
        for category in file_categories.keys():
            category_path = os.path.join(directory, category)
            os.makedirs(category_path, exist_ok=True)
            logging.info(f"Ensured directory exists: {category_path}")

        # Organize files
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Skip directories
            if os.path.isdir(file_path):
                logging.info(f"Skipped directory: {file_path}")
                continue

            # Find the category for the file
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    destination = os.path.join(directory, category, filename)
                    shutil.move(file_path, destination)
                    logging.info(f"Moved '{filename}' to '{destination}'")
                    moved = True
                    break

            # Move to "Others" if no matching category
            if not moved:
                destination = os.path.join(directory, "Others", filename)
                shutil.move(file_path, destination)
                logging.info(f"Moved '{filename}' to '{destination}'")

        messagebox.showinfo("Success", "Files have been organized successfully!")
        logging.info("File organization completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

# Create the Tkinter GUI
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x300")
root.resizable(False, False)

# Create and place GUI elements
label = tk.Label(root, text="File Organizer", font=("Arial", 20))
label.pack(pady=20)

label = tk.Label(root, text="Select a directory to organize files:", font=("Arial", 12))
label.pack(pady=20)

select_button = tk.Button(root, text="Select Directory", command=select_directory, font=("Arial", 12))
select_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
