from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

ORCHESTRATOR_URL = os.getenv('ORCHESTRATOR_URL', 'http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/discover', methods=['POST'])
def discover():
    try:
        data = request.json
        domain = data.get('domain', 'renewable_energy')
        
        # Import and run orchestrator by loading the module from the project root file path
        import importlib.util
        import os as _os
        # ensure project root (one level up from services) is resolved so orchestrator.py can be found
        project_root = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), '..'))
        orchestrator_path = _os.path.join(project_root, 'orchestrator.py')
        spec = importlib.util.spec_from_file_location("orchestrator", orchestrator_path)
        orchestrator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(orchestrator)
        EurekaOrchestrator = getattr(orchestrator, 'EurekaOrchestrator')
        
        orch = EurekaOrchestrator()
        result = orch.run_workflow(domain)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
