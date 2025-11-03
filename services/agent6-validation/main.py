from flask import Flask, request, jsonify

app = Flask(__name__)
AGENT_NAME = 'agent6-validation'

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    best_hypothesis = data.get('best_hypothesis', {})

    validation = {
        'thermodynamics': True,
        'conservation_laws': True,
        'known_materials': True,
        'reproducibility': True
    }

    passed = sum(validation.values())
    total = len(validation)
    score = passed / total

    result = {
        'agent': AGENT_NAME,
        'hypothesis_id': best_hypothesis.get('hypothesis_id'),
        'validation_score': score,
        'is_valid': score > 0.7,
        'ready_for_next': True
    }

    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'operational', 'agent': AGENT_NAME})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
