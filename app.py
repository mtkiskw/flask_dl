import os
from flask import Flask, render_template, request, send_file, Response, jsonify
import tempfile, csv

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET','POST'])
def download():
    if request.method == 'POST':
        fake_namefile = tempfile.NamedTemporaryFile(mode='w', dir=os.getcwd()+'/output', delete=False)
        with open(fake_namefile.name, 'w') as fake_csv:
            fake_writer = csv.writer(fake_csv)
            fake_writer.writerows(["hoge", "fuga", "piyo"])

        splited_filename = fake_namefile.name.split('/')
        return jsonify({"url": splited_filename[6]})

    return None

@app.route('/getfile/<name>')
def get_file(name):
    # TODO: delete temporary file
    file_name = os.getcwd() + '/output/' + name
    with open(file_name, 'rb') as f:
        resp = Response(f.read())
    resp.headers["Content-Disposition"] = "attachment; filename={0}.csv".format(name)
    resp.headers["Content-type"] = "text/csv"
    return resp



if __name__ == "__main__":
    app.run(debug=True)

