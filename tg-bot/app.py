from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    process = subprocess.Popen(
        ["ollama", "run", "llamapizza"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )

    response_text, error_text = process.communicate(input=user_message)

    if process.returncode != 0:
        return jsonify({"response": "Ошибка: " + error_text.strip()})

    return jsonify({"response": response_text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
