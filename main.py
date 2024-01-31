
# Libraries
from flask import Flask, request, redirect, url_for, render_template, send_file
import csv

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
   return render_template('landing_page.html')

# Registration route
@app.route('/register', methods=['POST'])
def register():
   name = request.form.get('name')
   email = request.form.get('email')
   phone = request.form.get('phone')
   time_slot = request.form.get('time_slot')
   date = request.form.get('date')

   with open('spreadsheet.csv', 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([name, email, phone, time_slot, date, 'Pending'])

   return redirect(url_for('confirmation'))

# Confirmation route
@app.route('/confirmation')
def confirmation():
   with open('spreadsheet.csv', 'r') as file:
      reader = csv.reader(file)
      registrations = list(reader)

   return render_template('confirmation.html', registrations=registrations)

# Download route
@app.route('/download')
def download():
   return send_file('spreadsheet.csv', as_attachment=True)

# Main driver
if __name__ == '__main__':
   app.run(debug=True)
