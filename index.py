from flask import Flask, request,jsonify,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax', methods=['POST'])
def ajax_example():
    data = request.get_json()
    response_data = {'message': 'This is a response from the server. Received data: {}'.format(data)}
    print(response_data)
    return jsonify(response_data)




if __name__ == '__main__':
    app.run(debug=True)
