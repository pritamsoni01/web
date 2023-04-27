from flask import Flask, render_template
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'web_base'

mysql = MySQL(app)
   
@app.route('/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':   
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
 
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO formdata (name, email, subject, messages) VALUES (%s, %s, %s, %s)", (name, email, subject, message))
        mysql.connection.commit()
        cur.close()

        return 'Form data submitted successfully!'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/keywest_quotation')
def keywest_quotation():
    return render_template('keywest_quotation.html')

@app.route('/miami_quotation')
def miami_quotation():
    return render_template('miami_quotation.html')

@app.route('/tampa_quotation')
def tampa_quotation():
    return render_template('tampa_quotation.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
