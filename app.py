from flask import Flask, render_template, Response
import subprocess
import os

app = Flask(__name__)

@app.route('/static/styles.css')
def styles():
    css = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f5;
        color: #333;
        line-height: 1.6;
    }

    h1 {
        color: #fff;
        text-align: center;
        margin: 40px 0;
        font-size: 3em;
        text-transform: uppercase;
        letter-spacing: 2px;
        background: linear-gradient(135deg, #007bff, #00bcd4);
        -webkit-background-clip: text;
        background-clip: text;
        padding: 10px;
        display: inline-block;
        position: relative;
        z-index: 1;
        transition: color 0.3s ease, text-shadow 0.3s ease;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }

    h1:hover {
        color: #ffffff;
        text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);
    }

    .container {
        width: 85%;
        max-width: 1000px;
        margin: auto;
        padding: 25px;
        background: linear-gradient(to right, #ffecd2, #fcb69f);
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        border: 1px solid #ddd;
    }

    .row-custom {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

    .col-custom {
        flex: 1 1 calc(50% - 20px);
        display: flex;
        align-items: stretch;
    }

    .btn-custom {
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: #fff;
        background-color: #007bff;
        font-weight: 600;
        font-size: 18px;
        padding: 20px;
        border: 2px solid #007bff;
        border-radius: 8px;
        text-align: center;
        transition: background-color 0.3s, color 0.3s, transform 0.3s;
        height: 100%;
        width: 100%;
        box-sizing: border-box;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .btn-custom:hover {
        background-color: #0056b3;
        color: #fff;
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    footer {
        background: #343a40;
        color: #fff;
        text-align: center;
        padding: 20px 0;
        position: fixed;
        bottom: 0;
        width: 100%;
        box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
    }

    @media (max-width: 768px) {
        .container {
            width: 90%;
            padding: 20px;
        }

        h1 {
            font-size: 2em;
        }

        .btn-custom {
            font-size: 16px;
            padding: 15px;
        }

        .col-custom {
            flex: 1 1 100%;
        }
    }
    """
    return Response(css, mimetype='text/css')

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Run Python Scripts</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>Claim Your Insurance</h1>
                <div class="row row-custom">
                    <div class="col col-custom">
                        <a href="/run/cancer" class="btn btn-custom">Cancer Insurance</a>
                    </div>
                    <div class="col col-custom">
                        <a href="/run/senior" class="btn btn-custom">Senior Insurance</a>
                    </div>
                    <div class="col col-custom">
                        <a href="/run/cardiac" class="btn btn-custom">Cardiac Insurance</a>
                    </div>
                    <div class="col col-custom">
                        <a href="/run/vectorborn" class="btn btn-custom">Vectorborne Insurance</a>
                    </div>
                </div>
            </div>
           
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
    '''

@app.route('/run/<script_name>')
def run_script(script_name):
    script_map = {
        'cancer': ('cancer.py', 'cancer.html'),
        'senior': ('senior.py', 'senior.html'),
        'cardiac': ('cardiac.py', 'cardiac.html'),
        'vectorborn': ('vectorborn.py', 'vectorborn.html')
    }

    if script_name in script_map:
        script_file, template_file = script_map[script_name]
        
        try:
            # Execute the script and capture output if needed
            result = subprocess.run(['python', script_file], check=True, text=True, capture_output=True)
            return render_template(template_file)
        except subprocess.CalledProcessError as e:
            return f"Failed to execute {script_file}: {str(e)}"
    else:
        return "Script not found!"

if __name__ == '__main__':
    app.run(debug=True)
