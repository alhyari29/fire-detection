from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("bbest.pt")

# Load video
video_path = "test 2.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ ERROR: Cannot open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Output video settings
out = cv2.VideoWriter("output6.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

frame_count = 0  # Track number of processed frames

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("✅ Video processing complete.")
        break

    print(f"Processing frame {frame_count + 1}/{total_frames}...")  # Debugging output

    # Run YOLO inference
    results = model.predict(frame, conf=0.5)
    annotated_frame = results[0].plot()

    # Write processed frame
    out.write(annotated_frame)
    frame_count += 1

cap.release()
out.release()

print(f"✅ Finished processing {frame_count}/{total_frames} frames.")
