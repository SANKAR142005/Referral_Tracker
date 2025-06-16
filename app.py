from flask import Flask, request, render_template
from db_config import getconnection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dob = request.form['dob']
    age = request.form['age']
    gender = request.form['gender']
    referral_by = request.form['referral_by']

    try:
        conn = getconnection()
        cursor = conn.cursor()
        query = """
            INSERT INTO clients (name, dob, age, gender, referral_by)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (name, dob, age, gender, referral_by)
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
        return "✅ Data inserted successfully!"

    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
