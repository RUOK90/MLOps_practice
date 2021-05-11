from flask import Flask, render_template, request
import functions


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def health_check():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기


@app.route('/addition', methods=['GET'])
def addition():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None:
        num1 = 0
    if num2 is None:
        num2 = 0
    return render_template('addition.html', num1=num1, num2=num2, addition=functions.addition(float(num1), float(num2)))


@app.route('/subtraction', methods=['GET'])
def subtraction():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None:
        num1 = 0
    if num2 is None:
        num2 = 0
    return render_template('subtraction.html', num1=num1, num2=num2, subtraction=functions.subtraction(float(num1), float(num2)))


@app.route('/multiplication', methods=['GET'])
def multiplication():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None:
        num1 = 0
    if num2 is None:
        num2 = 0
    return render_template('multiplication.html', num1=num1, num2=num2, multiplication=functions.multiplication(float(num1), float(num2)))


@app.route('/division', methods=['GET'])
def division():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None:
        num1 = 0
    if num2 is None:
        num2 = 0
    return render_template('division.html', num1=num1, num2=num2, division=functions.division(float(num1), float(num2)))


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port='80', debug=True)
    # app.run(host='127.0.0.1', port='80', debug=True)
    app.run(debug=True)
