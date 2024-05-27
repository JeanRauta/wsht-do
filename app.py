import os
from flask import Flask, jsonify
import demucs.api
from gunicorn.app.base import BaseApplication

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

class GunicornApp(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '5000'),
        'workers': 1,
        'timeout': 960,  # Ajuste o valor de timeout conforme necessário
    }
    GunicornApp(app, options).run()
