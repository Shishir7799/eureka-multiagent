from flask import Flask, request, jsonify
import random

app = Flask(__name__)
AGENT_NAME = 'agent4-hypothesis-generator'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    connections = data.get('connections', [])

    hypotheses = []

    for connection in connections:
        for i in range(3):
            hypothesis = {
                'id': f"h_{i}_{random.randint(1000, 9999)}",
                'hypothesis': f"{connection['hypothesis']} (Variant {i+1})",
                'confidence': connection['confidence'] - (i * 0.05),
                'testable': True
            }
            hypotheses.append(hypothesis)

    result = {
        'agent': AGENT_NAME,
        'hypotheses_generated': len(hypotheses),
        'hypotheses': hypotheses,
        'ready_for_next': True
    }

    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'operational', 'agent': AGENT_NAME})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
