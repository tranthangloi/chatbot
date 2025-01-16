from flask import Flask, request, jsonify
import google.generativeai as genai

# Khởi tạo Flask app
app = Flask(__name__)

# Cấu hình Gemini API
GEMINI_API_KEY = 'AIzaSyCGPIpIWIDzy_0SQ4ZwtXkuFN7gRqS8Cw4'  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro') # Use 'gemini-pro' or 'gemini-pro-vision'


# API endpoint nhận dữ liệu từ Roblox
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    username = data.get('username')
    message = data.get('message')

    if not username or not message:
        return jsonify({'error': 'Thiếu username hoặc message'}), 400

    try:
        # Create a prompt (can add more context here if needed)
        prompt = f"User: {message}"
        response = model.generate_content(prompt)

        if response.text:
            return jsonify({'reply': response.text})
        else:
            return jsonify({'error': 'Không có phản hồi từ Gemini API'}), 500
        
    except Exception as e:
       print(f"Error calling Gemini API: {str(e)}")  # Log the error
       return jsonify({'error': f'Lỗi: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)