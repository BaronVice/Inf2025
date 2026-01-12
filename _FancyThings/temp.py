import cv2
import os

video_path = "C:\\Users\\BaronVice\\Downloads\\Most Expensive Warehouse Fails Caught on Camera - #Mind Warehouse (1080p, h264).mp4"
output_directory = "D:\\warehouse_images"

vidcap = cv2.VideoCapture(video_path)

count = 0
while True:
    success, image = vidcap.read()
    if not success:
        break  # Break the loop if no more frames are available

    if count % 100 == 0:
        # Save the extracted frame
        frame_filename = os.path.join(output_directory, f"frame_{count:04d}.jpg")
        cv2.imwrite(frame_filename, image)

    count += 1

# Release the VideoCapture object
vidcap.release()
print(f"Extracted {count} frames to {output_directory}")
