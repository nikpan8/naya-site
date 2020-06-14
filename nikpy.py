import csv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/<site_name>')
def site_name(site_name):
    return render_template(site_name)

@app.route('/')
def site():
    return render_template('index.html')    

# #this is for collecting the data of contact grne manxe haru
# def collect_data(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n {email}, {subject}, {message}') 

def write_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
        return 'form submitted mero vai'
    else:
        return 'feri try gara yar'