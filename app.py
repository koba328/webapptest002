from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = '''<!DOCTYPE html>
<html lang=" ja\>
<head>
 <meta charset=\UTF-8\>
 <meta name=\viewport\ content=\width=device-width initial-scale=1.0\>
 <title>Flask 1ファイルサンプル!!!</title>
 <style>
 body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f8ff; margin: 0; padding: 24px; }
 .card { max-width: 700px; margin: 40px auto; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.1); }
 h1 { color: #1f4b9f; }
 table { width: 100%; border-collapse: collapse; margin-top: 16px; }
 th, td { text-align: left; border-bottom: 1px solid #ddd; padding: 8px; }
 th { background: #eef3ff; }
 </style>
</head>
<body>
 <div class=\card\>
 <h1>{{ greeting }}！</h1>
 <p>今日のおすすめ商品一覧です。</p>
 <table>
 <thead>
 <tr><th>商品名</th><th>価格 (円)</th></tr>
 </thead>
 <tbody>
 {% for item in items %}
 <tr><td>{{ item.name }}</td><td>{{ item.price }}</td></tr>
 {% endfor %}
 </tbody>
 </table>
 </div>
</body>
</html>'''

@app.route('/')
def index():
 items = [
 {'name': 'りんご', 'price': 120},
 {'name': 'バナナ', 'price': 80},
 {'name': 'みかん', 'price': 100},
 ]
 from datetime import datetime
 hour = datetime.now().hour
 if hour < 10:
 greeting = 'おはようございます'
 elif hour < 18:
 greeting = 'こんにちは'
 else:
 greeting = 'こんばんは'
 return render_template_string(TEMPLATE, greeting=greeting, items=items)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)
