import socket
from playwright.sync_api import sync_playwright

def lay_chi_tiet(stock_symbol, stock_name):
    with sync_playwright() as playwright:
        # Khởi động trình duyệt Chromium không ở chế độ headless
        browser = playwright.chromium.launch(headless=False)  
        page = browser.new_page()

        # Điều hướng đến trang iBoard SSI
        page.goto("https://iboard.ssi.com.vn/", timeout=0)

        # Chờ ô chứa mã chứng khoán và nhấp vào nó
        stock_symbol_selector = f'div[role="gridcell"][col-id="stockSymbol"]:has-text("{stock_symbol}")'
        page.wait_for_selector(stock_symbol_selector)
        page.click(stock_symbol_selector)  # Nhấp vào mã chứng khoán

        # Chờ một chút để giá cổ phiếu xuất hiện
        page.wait_for_timeout(3000)  # Thời gian chờ có thể thay đổi

        # Lấy giá cổ phiếu từ phần tử có class .stock-header-price
        price_element = page.wait_for_selector('.stock-header-price', timeout=15000)

        if price_element:
            # Lấy giá hiện tại
            current_price = price_element.query_selector('.text-3xl > div').inner_text() if price_element.query_selector('.text-3xl > div') else 'Không tìm thấy giá'
            
            # Lấy thêm thông tin khác về cổ phiếu
            open_price = price_element.query_selector('div.flex > div.text-color-down').inner_text() if price_element.query_selector('div.flex > div.text-color-down') else 'Không tìm thấy'
            low_price = price_element.query_selector('div.flex:nth-child(2) > div.text-color-down').inner_text() if price_element.query_selector('div.flex:nth-child(2) > div.text-color-down') else 'Không tìm thấy'
            high_price = price_element.query_selector('div.flex:nth-child(2) > div.text-color-ref').inner_text() if price_element.query_selector('div.flex:nth-child(2) > div.text-color-ref') else 'Không tìm thấy'
            total_volume = price_element.query_selector('div.flex:nth-child(3) > div.text-color-tertiary').inner_text() if price_element.query_selector('div.flex:nth-child(3) > div.text-color-tertiary') else 'Không tìm thấy'
            
            # Trả về kết quả dưới dạng từ điển
            return {
                'current_price': current_price,
                'open_price': open_price,
                'low_price': low_price,
                'high_price': high_price,
                'total_volume': total_volume
            }
        else:
            return {'error': 'Không tìm thấy phần tử giá cổ phiếu.'}
        
        # Đóng trình duyệt
        browser.close()

def main():
    # Tạo socket cho server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server đang chạy tại 127.0.0.1:12345...")

    while True:
        # Chờ kết nối từ client
        client_socket, addr = server_socket.accept()
        print(f'Kết nối từ {addr}')
        
        # Nhận mã chứng khoán từ client
        data = client_socket.recv(1024).decode().strip()
        stock_symbol, stock_name = data.split(',')  # Giả định client gửi mã chứng khoán và tên cổ phiếu cách nhau bằng dấu phẩy
        print(f'Nhận mã chứng khoán: {stock_symbol}, Tên cổ phiếu: {stock_name}')

        # Gọi hàm lấy chi tiết cổ phiếu và gửi kết quả về client
        result = lay_chi_tiet(stock_symbol, stock_name)
        client_socket.send(str(result).encode())
        
        # Đóng kết nối với client
        client_socket.close()

if __name__ == "__main__":
    main()
