from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        city = request.form['city']
        color = request.form['color']
        message = request.form['message']
        return render_template('greeting.html', name=name, email=email, phone=phone, gender=gender, city=city, color=color, message=message)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
