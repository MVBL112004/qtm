from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    try:
        # Nhận dữ liệu từ Client
        data = request.json.get('text')
        if not data:
            return {"error": "No data provided"}, 400
        
        # Tạo mã QR từ chuỗi văn bản hoặc URL
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        
        # Tạo ảnh mã QR
        img = qr.make_image(fill='black', back_color='white')
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Trả ảnh mã QR cho Client
        return send_file(buffer, mimetype='image/png')
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
