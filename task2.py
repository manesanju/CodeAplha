import os
import shutil

def move_jpg_files():
    """Simple program to move all JPG files from one folder to another"""
    
    print("📁 JPG File Mover")
    print("=" * 20)
    print("💡 Tip: Enter folder paths like:")
    print("   Windows: C:\\Users\\YourName\\Pictures")
    print("   Or use: C:/Users/YourName/Pictures")
    print("=" * 20)
    
    # Get folder paths from user
    source_folder = input("Enter source folder path: ")
    destination_folder = input("Enter destination folder path: ")
    
    # Check if source folder exists and is actually a directory
    if not os.path.exists(source_folder):
        print("❌ Source folder does not exist!")
        return
    
    if not os.path.isdir(source_folder):
        print("❌ Source path is not a folder! Please enter a folder path, not a file path.")
        print(f"You entered: {source_folder}")
        return
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"✅ Created destination folder: {destination_folder}")
    
    # Find JPG files
    jpg_files = []
    for file in os.listdir(source_folder):
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
            jpg_files.append(file)
    
    # Check if any JPG files found
    if len(jpg_files) == 0:
        print("ℹ️  No JPG files found!")
        return
    
    print(f"📸 Found {len(jpg_files)} JPG files:")
    
    # Move each JPG file
    moved_count = 0
    for file in jpg_files:
        source_path = os.path.join(source_folder, file)
        dest_path = os.path.join(destination_folder, file)
        
        try:
            shutil.move(source_path, dest_path)
            print(f"  ✅ Moved: {file}")
            moved_count += 1
        except:
            print(f"  ❌ Failed to move: {file}")
    
    print(f"\n🎉 Successfully moved {moved_count} files!")

# Run the program
if __name__ == "__main__":
    move_jpg_files()