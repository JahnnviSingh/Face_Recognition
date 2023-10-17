from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://lg-attendance-661e4-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        employee_id = request.form['id']
        position = request.form['position']
        starting_year = request.form['starting_year']
        # Save image to local directory
        image = request.files['image']
        image.save(os.path.join("Images", f"{employee_id}.png"))

        # Add data to Firebase
        ref = db.reference('Employees')
        data = {
            employee_id: {
                "name": name,
                "position": position,
                "starting_year": starting_year
            }
        }
        ref.update(data)
        return redirect(url_for('add_employee'))
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)

