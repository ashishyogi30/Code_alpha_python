import os
import shutil
import re
import requests

def move_jpg_files():
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()

    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: '{destination_folder}'")

    files = os.listdir(source_folder)
    jpg_files = [file for file in files if file.lower().endswith(".jpg")]

    if not jpg_files:
        print("No .jpg files found in the source folder.")
        return
    #source folder path :-> /home/ashish/Pictures/preety
    #destination source folder path:-> /home/ashish/Pictures/images

    for file in jpg_files:
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
        print(f"Moved: {file}")

    print(f"\nAll {len(jpg_files)} .jpg file(s) have been moved to '{destination_folder}'.")

def extract_emails():
    input_file = input("Enter the text file name to read from (e.g., sample.txt): ").strip()
    output_file = input("Enter the file name to save emails (e.g., emails.txt): ").strip()

    if not os.path.exists(input_file):
        print(f"File '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    emails = list(set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)))

    if emails:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("Extracted Email Addresses:\n")
            f.write("---------------------------\n")
            for email in emails:
                f.write(email + "\n")
        print(f"{len(emails)} email(s) extracted and saved to '{output_file}'.")
    else:
        print("No email addresses found in the file.")

def scrape_webpage_title():
    url = input("Enter the webpage URL (e.g., https://www.example.com): ").strip()
    output_file = input("Enter the file name to save the title (e.g., title.txt): ").strip()

    try:
        response = requests.get(url)
        response.raise_for_status()

        match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE)
        if match:
            title = match.group(1)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"Webpage URL: {url}\n")
                f.write(f"Title: {title}\n")
            print(f"Webpage title saved to '{output_file}'.")
        else:
            print("Could not find the title in the webpage HTML.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        
print("=== Python Task Automation ===")
print("Choose a task to perform:")
print("1. Move all .jpg files from a folder to another folder")
print("2. Extract all email addresses from a .txt file")
print("3. Scrape the title of a webpage")

choice = input("Enter your choice (1/2/3): ").strip()

if choice == "1":
    move_jpg_files()
elif choice == "2":
    extract_emails()
elif choice == "3":
    scrape_webpage_title()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
