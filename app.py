from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    message = '''
    <html>
        <head>
            <title>Insta Media Downloader Updated</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;  
                    height: 100vh;
                    background: #f2f2f2;
                    padding-top: 50px;
                }
                .card {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 600px;
                    width: 90%; 
                }
                h1 {
                    color: #333;
                    font-size: 24px;
                    margin-bottom: 20px;
                }
                p {
                    color: #555;
                    font-size: 16px;
                    margin-bottom: 20px;
                }
                a {
                    text-decoration: none;
                    color: white;
                    background-color: #007bff;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 18px;
                    transition: background-color 0.3s;
                }
                a:hover {
                    background-color: #0056b3;
                }

                /* Media Query for small screens (mobile devices) */
                @media (max-width: 600px) {
                    body {
                        padding-top: 20px; 
                    }
                    .card {
                        padding: 20px;  
                    }
                    h1 {
                        font-size: 20px; 
                    }
                    p {
                        font-size: 14px;
                    }
                    a {
                        font-size: 16px; 
                        padding: 8px 15px; 
                    }
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Insta Media Downloader has been updated!</h1>
                <p>The domain has changed. Please click the button below to visit the <b>new site</b>:</p>
                <a href="https://insta-media-downloader.up.railway.app/">Click here</a>
            </div>
        </body>
    </html>
    '''
    return render_template_string(message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
