import cv2
from ultralytics import YOLO
import random
import os

def extract_segments_yolo(video_path, output_file):
    # Tải mô hình YOLOv8 
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Không thể mở video!")
        return

    segments = []
    segment_id = 1
    frame_idx = 0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while cap.isOpened() and frame_idx < frame_count:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            break

        # Nhận diện đối tượng bằng YOLOv8
        results = model(frame, verbose=False)
        for det in results[0].boxes:
            cls = int(det.cls[0])
            obj_name = model.names[cls]
            if obj_name not in ["person", "car", "bicycle"]:
                continue
            x, y, w, h = det.xywh[0].tolist() 
            confidence = det.conf[0].item()

            segments.append({
                "id": segment_id,
                "video_id": "video2",
                "object_name": obj_name,
                "activity_name": random.choice(["moving", "walking"] if obj_name == "person" else ["moving"]),  # Giả lập hoạt động
                "prop": random.choice(["red", "blue", "black"]),  # Giả lập thuộc tính
                "start_frame": frame_idx,
                "end_frame": min(frame_idx + int(fps), frame_count), 
                "spatial_y": float(y),
                "spatial_z": 0.0
            })
            segment_id += 1

        frame_idx += int(fps // 2)  # Xử lý mỗi 0.5 giây để giảm tải

    cap.release()

    with open(output_file, 'w') as f:
        f.write("segments = [\n")
        for seg in segments:
            f.write(f"    {seg},\n")
        f.write("]\n")
    print(f"Đã lưu dữ liệu vào {output_file}")

if __name__ == "__main__":
    video_path = "data/datatest.mp4"
    output_file = "data/sample_data.py"
    if not os.path.exists(video_path):
        print(f"Video {video_path} không tồn tại!")
    else:
        extract_segments_yolo(video_path, output_file)