import os
import random
import string

# List of valid font file extensions
FONT_EXTENSIONS = ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.svg', '.pfb', '.pfa', '.fon', '.bmf', '.ttc', '.otc', '.aat']

def random_name(length=8):
    """Generate a random string of uppercase letters and digits."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def is_font_file(filename):
    """Check if the file is a font based on its extension."""
    return any(filename.lower().endswith(ext) for ext in FONT_EXTENSIONS)

def cleanup_directory(folder_path='.'):
    """Rename all font files to random names and delete non-font files."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            if is_font_file(filename):
                # Generate new random name for the font file
                new_filename = random_name() + os.path.splitext(filename)[1].upper()  # Retain original extension
                new_path = os.path.join(folder_path, new_filename)
                
                # Make sure we don't accidentally overwrite an existing file
                while os.path.exists(new_path):
                    new_filename = random_name() + os.path.splitext(filename)[1].upper()
                    new_path = os.path.join(folder_path, new_filename)
                
                os.rename(file_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')
            else:
                # Delete non-font files
                os.remove(file_path)
                print(f'Deleted: {filename}')

# Example usage
cleanup_directory()  # By default, works in the current folder

