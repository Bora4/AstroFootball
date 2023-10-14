from flask import Flask, request

app = Flask(__name__)

@app.route('/upload-video', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    return f"Received form data:\nName: {name}\nEmail: {email}\nMessage: {message}"

if __name__ == '__main__':
    app.run(debug=True)
