from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Your personal information
PERSONAL_INFO = {
    'name': 'Udit Raj Parihar',  # Replace with your actual name
    'phone': '+1 (226) 123-1234'  # Replace with your actual phone number
}

# HTML template with modern styling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Information</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            padding: 40px;
            text-align: center;
            max-width: 500px;
            width: 100%;
            animation: fadeInUp 0.6s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .profile-icon {
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            margin: 0 auto 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            color: white;
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.5em;
            font-weight: 300;
        }
        
        .subtitle {
            color: #666;
            margin-bottom: 40px;
            font-size: 1.1em;
        }
        
        .info-card {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 25px;
            margin: 20px 0;
            border-left: 5px solid #667eea;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }
        
        .info-label {
            font-weight: 600;
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        
        .info-value {
            font-size: 1.3em;
            color: #333;
            font-weight: 500;
        }
        
        .phone-link {
            color: #667eea;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .phone-link:hover {
            color: #764ba2;
        }
        
        .footer {
            margin-top: 30px;
            color: #999;
            font-size: 0.9em;
        }
        
        @media (max-width: 480px) {
            .container {
                padding: 30px 20px;
            }
            
            h1 {
                font-size: 2em;
            }
            
            .info-value {
                font-size: 1.1em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="profile-icon">
            👤
        </div>
        
        <h1>{{ personal_info.name }}</h1>
        <p class="subtitle">Personal Information</p>
        
        <div class="info-card">
            <div class="info-label">Name</div>
            <div class="info-value">{{ personal_info.name }}</div>
        </div>
        
        <div class="info-card">
            <div class="info-label">Phone Number</div>
            <div class="info-value">
                <a href="tel:{{ personal_info.phone.replace(' ', '').replace('(', '').replace(')', '').replace('-', '') }}" 
                   class="phone-link">{{ personal_info.phone }}</a>
            </div>
        </div>
        
        <div class="footer">
            Flask Application • Personal Info Display
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def display_info():
    return render_template_string(HTML_TEMPLATE, personal_info=PERSONAL_INFO)

@app.route('/api/info')
def api_info():
    """API endpoint to get personal information in JSON format"""
    return PERSONAL_INFO

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    print("🚀 Starting Flask application...")
    print(f"📱 Personal Info: {PERSONAL_INFO['name']} - {PERSONAL_INFO['phone']}")
    print(f"🌐 Server will be available at: http://localhost:{port}")
    print("💡 To update your information, edit the PERSONAL_INFO dictionary in the code")
    
    app.run(debug=True, host='0.0.0.0', port=port)

