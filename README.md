## Giới thiệu

RS-Tree Video Analysis là một ứng dụng Python phân tích video sử dụng cấu trúc dữ liệu R-tree để lưu trữ và truy vấn dữ liệu không gian-thời gian (spatial-temporal). Dự án tích hợp YOLOv8 để nhận diện đối tượng (car, person, bicycle) trong video, lưu thông tin vào R-tree.

### Tính năng
- **Nhận diện đối tượng**: Sử dụng YOLOv8 để phát hiện đối tượng trong video.
- **Lưu trữ không gian-thời gian**: R-tree lưu trữ thông tin đối tượng (tọa độ x, y, z, khung thời gian).
- **Truy vấn**:
  - Tìm video chứa đối tượng, hoạt động, hoặc thuộc tính.
  - Tìm đối tượng, hoạt động, hoặc thuộc tính trong video theo khoảng thời gian.
### Ứng dụng
- Phân tích video giao thông, giám sát, hoặc các ứng dụng cần truy vấn không gian-thời gian.
- Demo nghiên cứu về R-tree và nhận diện đối tượng.

## Yêu cầu

- Python 3.8+
- Thư viện:
  - `rtree`
  - `opencv-python`
  - `ultralytics`
  - `ttkbootstrap`
- Hệ điều hành: Windows, macOS, hoặc Linux
- Video đầu vào: MP4

## Cài đặt
   ```bash
   git clone https://github.com/tienanh443/rstree_project.git
   cd rstree_project
   pip install -r requirements.txt
   python -m src.main
