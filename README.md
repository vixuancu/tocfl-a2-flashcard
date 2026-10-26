# TOCFL A2 Flashcard

Ứng dụng học bộ **500 mục từ do người dùng cung cấp**, chia **20 Unit × 25 thẻ** theo đúng thứ tự STT trong Excel. Giao diện và cách học kế thừa [HSK4 Flashcard của vixuancu](https://github.com/vixuancu/hsk4-flashcard).

**[Mở trang học từ vựng](https://vixuancu.github.io/tocfl-a2-flashcard/)**

## Cách học

- Chọn Unit, nhìn chữ Hán rồi tự nhớ pinyin và nghĩa.
- **Nhớ / →**: ghi T và chuyển thẻ.
- **Lật xem / Space**: hiện đáp án, ghi F một lần. Sau đó dùng nút Tiếp, ←, Space hoặc Enter.
- **⭐ / B**: thêm hoặc bỏ dấu sao; ôn riêng trong danh sách Đã đánh dấu.
- **Từ cứng đầu**: các thẻ có tổng số F trong lịch sử từ 5 trở lên. Đây là bộ lọc lịch sử, không phải thuật toán lên lịch ôn cách quãng.
- Xem lịch sử T/F từng thẻ, tiến độ từng Unit và kết quả mỗi lượt. Có thể học lại bài.
- Reset Unit xóa lịch sử của Unit đó. Reset từ cứng đầu xóa lịch sử của các thẻ đang thuộc nhóm. Reset Đã đánh dấu chỉ bỏ sao và giữ lịch sử T/F.

## Lưu tiến độ

Tiến độ và dấu sao lưu tự động trong LocalStorage của trình duyệt, riêng với bản HSK4. Tải lại trang vẫn giữ lịch sử, nhưng mỗi lượt học bắt đầu lại từ thẻ đầu khi chọn Unit. Không đồng bộ giữa thiết bị, hồ sơ trình duyệt hoặc tên miền. Xóa dữ liệu trang sẽ mất tiến độ.

## Dữ liệu

- Nguồn: `Check list vocabs A.xlsx`, sheet `Trang tính1`, cột STT / Từ hán / Pinyin / Nghĩa tiếng việt. Dòng giới thiệu trong file ghi TOCFL Mastery.
- Giữ nguyên chữ Hán, pinyin, nghĩa và các biến thể ngăn bằng `/` trong nguồn. Các cột trạng thái và bài tập Excel không nhập vào ứng dụng.
- Giữ đủ 500 mục, kể cả các từ lặp `去年`, `得`, `還`. Mỗi mục có ID riêng để lịch sử không bị lẫn.
- Dùng bộ từ người dùng lựa chọn; không tuyên bố đây là toàn bộ danh sách thi chính thức.

## Chạy và cập nhật

Trang tĩnh, không cần backend. Có thể mở `index.html` hoặc phục vụ qua một máy chủ HTTP / GitHub Pages.

```sh
python -m pip install -r requirements.txt
python import_vocab.py "đường/dẫn/Check list vocabs A.xlsx"
python build_flashcard.py
python -m http.server 8000
```

`import_vocab.py` kiểm tra STT 1–500, đủ trường và 25 mục mỗi Unit. Sửa dữ liệu ở Excel rồi nhập lại, hoặc chỉnh `a2_vocab.json` và chạy lại build. Giữ ID ổn định cho cùng mục từ để bảo toàn lịch sử học.

## Kiểm thử

```sh
npm install
npm test
```

Yêu cầu Google Chrome cài trên máy. Có thể đặt `TEST_BROWSER=msedge` để dùng Edge. Đặt `TEST_URL` để chạy lại bộ kiểm thử trên một URL đã triển khai; bộ test sử dụng hồ sơ trình duyệt tạm riêng.

Kiểm thử tạo máy chủ localhost, kiểm tra dữ liệu và các luồng học trên trình duyệt thật, xuất báo cáo JSON cùng ảnh màn hình vào `test-results/`. Xem `TESTING.md` để biết kết quả trước khi phát hành.

## Triển khai

GitHub Pages: chọn nhánh `main`, thư mục `/ (root)`. `index.html` đã chứa dữ liệu và mã ứng dụng; `.nojekyll` giữ cách phục vụ trang tĩnh. Font Inter và Noto Sans TC tải từ Google Fonts, có font hệ thống dự phòng.
