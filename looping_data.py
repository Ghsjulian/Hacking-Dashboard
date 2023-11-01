
from flask import Flask, render_template

app = Flask(__name)

# Sample data to loop through
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22},
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    

"""
<!DOCTYPE html>
<html>
<head>
    <title>Data Looping Example</title>
</head>
<body>
    <h1>Data Looping Example</h1>

    <ul>
        {% for item in data %}
            <li>Name: {{ item['name'] }}, Age: {{ item['age'] }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""