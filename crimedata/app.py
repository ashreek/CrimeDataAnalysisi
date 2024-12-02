from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # Use double underscores here

# Route for survey form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']

        # Append responses to CSV file
        with open('responses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, gender, q1, q2, q3, q4, q5])

        return render_template('submission.html', name=name)

if __name__ == '__main__':  # Use double underscores here as well
    app.run(debug=True)
