# Kiểm thử trước phát hành

Ngày: 26/10/2026.

## Dữ liệu

- Đối chiếu trực tiếp 500 dòng từ Excel gốc với JSON: chữ Hán, pinyin và nghĩa khớp nguyên văn.
- Đủ 20 Unit, mỗi Unit 25 thẻ, theo thứ tự STT 1–500.
- 500 ID độc lập. Ba cách viết lặp được giữ nguyên: 去年 (99, 313), 得 (211, 212), 還 (246, 457).
- Kiểm tra nội dung thực tế của cả 500 thẻ trong DOM trình duyệt với JSON.

## Kiểm thử trình duyệt

Bộ `test_app.js` có 18 nhóm kiểm thử: chia Unit; trạng thái ban đầu; toàn bộ nội dung thẻ; T/F và chuyển thẻ; phím tắt; lưu lịch sử và dấu sao sau tải lại; kết thúc và học lại; ngưỡng từ khó; hủy reset và khóa phím khi mở modal; reset từng Unit; reset dấu sao; reset từ khó; độc lập giữa từ trùng; dữ liệu JSON hỏng; tiến độ/thống kê; các cỡ màn hình; lịch sử dài; lỗi JavaScript.

- Microsoft Edge: **18/18 đạt**.
- Google Chrome: **18/18 đạt**.
- Viewport: 1280×900, 820×1180, 390×844, 320×640.
- Kiểm tra thêm thẻ dài nhất với 81 dấu lịch sử: không tràn ngang hoặc chồng lên nút thao tác.
- Đã xem trực tiếp ảnh chụp desktop và điện thoại.

## Các lỗi kế thừa đã sửa

- Reset danh sách dấu sao trả về trạng thái trống đúng, giữ lịch sử T/F.
- Nội dung xác nhận reset dấu sao mô tả đúng hành động; nút reset trên điện thoại dùng chung logic.
- Phím tắt không ghi kết quả khi modal/menu đang mở hoặc phím đang bị giữ lặp.
- Chặn ghi kết quả sau cuối lượt và chặn chuyển tiếp khi chưa lật.
- Dùng ID thay cho chữ Hán để các mục trùng không dùng chung lịch sử.
- Lịch sử dài xuống dòng theo bố cục tự nhiên, tránh chồng vào đáp án.

## Giới hạn kiểm tra

Kiểm thử responsive thực hiện bằng viewport trình duyệt trên Windows, chưa chạy trên thiết bị iOS/Android vật lý. Tiến độ lưu tại trình duyệt, chưa có đồng bộ tài khoản.
