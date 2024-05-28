import os
from flask import Flask, jsonify
import demucs.api

app = Flask(__name__)

separator = demucs.api.Separator()

@app.route('/')
def process_audio():
    audio_file_path = './audio.wav'

    if not os.path.exists(audio_file_path):
        return jsonify({'message': 'Arquivo de áudio não encontrado'}), 404

    try:
        _, separated_sources = separator.separate_audio_file(audio_file_path)
    except Exception as e:
        return jsonify({'message': f'Erro ao processar o arquivo de áudio: {str(e)}'}), 500

    return jsonify({'message': 'Processamento concluído'}), 200

if __name__ == '__main__':
    app.run()
