Ex1: Nếu một số được kết thúc ở 0.5, thì Python làm tròn xuống hay lên? 
Ví dụ:
- round(42.5) = 42
- round(43.5) = 44

=> Python làm tròn theo cơ chế làm tròn theo số nguyên chẵn gần nhất


Ex2: Thông điệp: Hãy cứ làm và mắc lỗi.
1, Điều gì xảy ra nếu thêm một dấu cộng nữa ở 2 số, ví dụ như 2++2?
thì đáp số vẫn như là 2+2 = 4
Nếu 2+-2 thì sao? đáp án là =0;
2, Điều gì xảy ra nếu không có "operator" nào ở giữa? như là 4 2? bị lỗi
3, Gọi 1 hàm như round(42.5), thì bỏ dấu ngoặc ở đầu hoặc cuối thì sao?
- Bỏ ngoặc ở đầu, Python chỉ tham chiếu đến hàm round thôi, chứ không hoạt động (SyntaxError) vì cú pháp không hợp lệ
- Bỏ ngoặc ở sau, SyntaxError, do Python vẫn chờ hàm round đóng


Ex3: Gọi được type của các giá trị
- 765: int
- 2.718: float
- '2 pi': string
- abs(-7): int
- abs(-7.0): float
- abs: builtin-function-or-method
- int: type
- type: type


Ex4: 
1, Có 42 * 60 + 42 = 2562 seconds ở trong 42 minutes 42 seconds
2, có 1.61 * 10 = 16.1 kilometers
3, Nếu chạy 10km trong 42m42s, thì tốc độ là 10 * (10^3) / (42 * 60 + 42) =  3.903 m/s
