## Thông tin sinh viên
- Họ và tên: Phạm Tiến Anh
- MSSV: N21DCCN100

## Exercises_07
This project pertains to the design and implementation of RS-trees. To successfully complete this project, we encourage you to review material both in this chapter and in Section 4.5.
### Design and implement an algorithm that reads a segment table containing objects as input and that returns an RS-tree and an OBJECTARRAY containing the relevant information as output.
### Implement each of the eight functions listed below on top of the RS-tree constructed above:
- FindVideoWithObject(o)
- FindVideoWithActivity(a)
- FindVideoWithActivityandProp(a, p, z)
- FindVideoWithObjectandProp(o, p, z)
- FindObjectsInVideo(v, s, e)
- FindActivitiesInVideo(v, s, e)
- FindActivitiesAndPropsinVideo(v, s, e)
- FindObjectsAndPropsinVideo(v, s, e)
### Design a graphical user interface from which the user can execute each of the functions listed above.
### Demonstrate the operation of your algorithm by showing how it accesses a small video of 80-100 frames.
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
