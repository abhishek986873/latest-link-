import re

counter = 1  # Initialize counter to 1
while True:
    # Prompt user for CloudFront MP4 video link
    cloudfront_link = input("Enter CloudFront MP4 video link (or press Enter to exit): ")

    # Exit loop if user presses Enter
    if not cloudfront_link:
        break

    # Extract video ID from CloudFront link
    match = re.search(r'https:\/\/.*\.cloudfront\.net\/([a-zA-Z0-9-_]+)\/', cloudfront_link)
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
