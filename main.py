10/2/24
import os
import requests
import time

# List of URLs to download
urls = [
    # Add URLs here, e.g., 'https://example.com/file1.mp3'
]

# Output directory for downloaded files
output_dir = r'.\Outputs'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to download a file and check if it was downloaded successfully
def download_file(url, output_dir):
    try:
        print(f"Downloading from {url}...")
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            file_name = os.path.basename(url)
            file_path = os.path.join(output_dir, file_name)
            
            # Write the content to a file
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # Filter out keep-alive chunks
                        f.write(chunk)
            
            print(f"Downloaded: {file_path}")
            
            # Check if the file exists and has been downloaded
            if os.path.exists(file_path):
                print(f"File {file_name} saved successfully!")
                return True
            else:
                print(f"Error: File {file_name} was not saved correctly.")
                return False
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")
        return False

# Iterate through the list of URLs and download them one by one
for url in urls:
    success = download_file(url, output_dir)
    
    # If the download was successful, wait for 1 second before downloading the next file
    if success:
        time.sleep(1)  # Adjust the sleep time as needed
    else:
        print(f"Skipping to the next file due to a download error.")
