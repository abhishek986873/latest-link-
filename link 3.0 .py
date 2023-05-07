import re
import time
import clipboard

counter = 1  # Initialize counter to 1
previous_link = ""

while True:
    # Check if a new link has been copied
    current_link = clipboard.paste()

    if current_link != previous_link:
        previous_link = current_link

        # Extract video ID from CloudFront link
        match = re.search(r'https:\/\/.*\.cloudfront\.net\/([a-zA-Z0-9-_]+)\/', current_link)
        if not match:
            print("Error: invalid CloudFront link.")
            continue
        video_id = match.group(1)

        # Create 1DM download link
        one_dm_link = f"https://prourl.xyz/1dm?vid={video_id}"

        # Print the labeled link
        print(f"{counter}. {one_dm_link}")

        # Increment the counter
        counter += 1

    # Sleep for a short duration to avoid high CPU usage
    time.sleep(1)
