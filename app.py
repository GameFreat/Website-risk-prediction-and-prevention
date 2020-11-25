from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    num = request.form['num1']
    sum = str(num)

    return render_template('index.html', sum=sum)


if __name__ == ' __main__':
    app.debug = True
    app.run()
