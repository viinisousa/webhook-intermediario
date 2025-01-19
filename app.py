from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/get-file', methods=['GET'])
def get_file():
    # Link direto do Google Drive
    file_url = "https://drive.google.com/uc?id=15tD7e2vNFlIJyx1LZ91It9GLvi421MQ4&export=download"

    # Fazer o download do arquivo
    response = requests.get(file_url)

    # Retornar o arquivo com os headers corretos
    return Response(
        response.content,
        mimetype="application/octet-stream",
        headers={
            "Content-Disposition": "attachment; filename=arquivo.pdf"
        }
    )

if __name__ == '__main__':
    app.run(debug=True)