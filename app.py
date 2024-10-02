from flask import Flask, Response, request, jsonify, render_template, send_file
import subprocess
import os

app = Flask(__name__)

# Route voor de homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route om de content op te slaan in content.txt
@app.route('/save-content', methods=['POST'])
def save_content():
    data = request.get_json()
    content = data.get('content')

    # Sla de content op in content.txt
    with open('content.txt', 'w') as file:
        file.write(content)

    return jsonify({"message": "Content opgeslagen"}), 200

# Streaming route voor het uitvoeren van het script
@app.route('/stream')
def stream():
    # Generator voor real-time log output van het Python-script
    def generate():
        # Voer het script uit en schakel buffering uit
        process = subprocess.Popen(
            ['python', '-u', 'podcast_script_kind.py'],  # '-u' schakelt buffering uit
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Zorg ervoor dat zowel stdout als stderr worden meegenomen
            universal_newlines=True,  # Zorgt ervoor dat output regels zijn
            bufsize=1  # Line-buffered
        )

        # Lees stdout en stuur deze regel voor regel door naar de client
        for line in iter(process.stdout.readline, ''):
            yield f"data:{line}\n\n"

        # Als het proces klaar is, stuur een einde boodschap
        process.stdout.close()
        yield "data:--- SCRIPT KLAAR ---\n\n"

    return Response(generate(), mimetype='text/event-stream')

# Route om het final_output.mp3-bestand te verzenden
@app.route('/final_output')
def final_output():
    mp3_path = 'final_output.mp3'

    # Controleer of het bestand bestaat voordat het wordt verzonden
    if os.path.exists(mp3_path):
        return send_file(mp3_path, mimetype='audio/mpeg')
    else:
        return "MP3-bestand niet gevonden", 404

if __name__ == '__main__':
    app.run(debug=True)
