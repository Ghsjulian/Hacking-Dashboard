from flask import Flask, request

app = Flask(__name)

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        form_data = request.form
        # Access form fields by name
        name = form_data.get('name')
        email = form_data.get('email')
        # Process the form data as needed
        return f"Received data: Name - {name}, Email - {email}"
    else:
        return "Invalid request method"

if __name__ == '__main__':
    app.run(debug=True)
    