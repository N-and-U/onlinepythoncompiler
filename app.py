from flask import Flask, redirect, render_template, url_for, request
from flask import Flask
from compiler import compile_script
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/codefile',methods = ['POST'])
def CodeFile():
    if request.method == 'POST':
        file = request.files['file1'].read()
        with open("code.txt","w") as rnr: 
            rnr.write(file.decode('utf-8'))
        print(file)
        compile_script()
    return render_template('index.html')

@app.route('/inputfile',methods = ['POST'])
def InputFile():
    if request.method == 'POST':
        file = request.files['file2'].read()
        with open("input.txt","w") as rnr: 
            rnr.write(file.decode('utf-8'))
        print(file)
    return render_template('index.html')

@app.route('/codetext',methods = ['POST'])
def CodeText():
    if request.method == 'POST':
        code = request.form['code1']
        with open("code.txt","w") as rnr: 
            rnr.write(code.decode('utf-8'))
        print(code)
    return render_template('index.html')

@app.route('/inputtext',methods = ['POST'])
def InputText():
    if request.method == 'POST':
        code = request.form['code2']
        with open("input.txt","w") as rnr: 
            rnr.write(code.decode('utf-8'))
        print(code)
    return render_template('index.html')



if __name__ == '__main__':
   app.run(debug=False)