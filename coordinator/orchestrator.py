import os
try:
    import requests  # type: ignore
except Exception:
    # Lightweight fallback using urllib when 'requests' is not installed.
    import urllib.request
    import json as _json

    class SimpleResponse:
        def __init__(self, body_bytes):
            self._body = body_bytes

        def json(self):
            return _json.loads(self._body.decode('utf-8'))

        @property
        def text(self):
            return self._body.decode('utf-8')

    class requests:
        @staticmethod
        def post(url, json=None):
            body = None
            headers = {}
            if json is not None:
                body = _json.dumps(json).encode('utf-8')
                headers['Content-Type'] = 'application/json'
            req = urllib.request.Request(url, data=body, headers=headers, method='POST')
            with urllib.request.urlopen(req) as resp:
                return SimpleResponse(resp.read())

class EurekaOrchestrator:
    def __init__(self):
        self.agent_urls = {
            'agent1': os.getenv('AGENT1_URL', 'http://localhost:8001'),
            'agent2': os.getenv('AGENT2_URL', 'http://localhost:8002'),
            'agent3': os.getenv('AGENT3_URL', 'http://localhost:8003'),
            'agent4': os.getenv('AGENT4_URL', 'http://localhost:8004'),
            'agent5': os.getenv('AGENT5_URL', 'http://localhost:8005'),
            'agent6': os.getenv('AGENT6_URL', 'http://localhost:8006'),
            'agent7': os.getenv('AGENT7_URL', 'http://localhost:8007'),
        }

    def run_workflow(self, domain: str):
        print(f"\n🚀 Starting workflow for domain: {domain}\n")

        # Agent 1
        r1 = requests.post(f"{self.agent_urls['agent1']}/analyze", json={'domain': domain})
        analysis = r1.json()
        print("Agent 1 completed")

        # Agent 2
        r2 = requests.post(f"{self.agent_urls['agent2']}/find-patterns", json={'domain': domain, 'analysis': analysis})
        patterns = r2.json()
        print("Agent 2 completed")
 # Agent 3
        r3 = requests.post(f"{self.agent_urls['agent3']}/find-connections", json={'patterns': patterns['patterns']})
        connections = r3.json()
        print("Agent 3 completed")

        # Agent 4
        r4 = requests.post(f"{self.agent_urls['agent4']}/generate", json={'connections': connections['connections']})
        hypotheses = r4.json()
        print("Agent 4 completed")

        # Agent 5
        r5 = requests.post(f"{self.agent_urls['agent5']}/simulate", json={'hypotheses': hypotheses['hypotheses']})
        simulations = r5.json()
        print("Agent 5 completed")

        # Agent 6
        r6 = requests.post(f"{self.agent_urls['agent6']}/validate", json={'best_hypothesis': simulations['best_hypothesis']})
        validation = r6.json()
        print("Agent 6 completed")

      # Agent 7
        r7 = requests.post(f"{self.agent_urls['agent7']}/generate-paper", json={
            'best_hypothesis': simulations['best_hypothesis'],
            'validation': validation
        })
        paper = r7.json()
        print("Agent 7 completed")

        return {
            "analysis": analysis,
            "patterns": patterns,
            "connections": connections,
            "hypotheses": hypotheses,
            "simulations": simulations,
            "validation": validation,
            "paper": paper
        }

if __name__ == '__main__':
    orchestrator = EurekaOrchestrator()
    result = orchestrator.run_workflow('renewable_energy')

    print("\n=== WORKFLOW COMPLETE ===\n")
    print(result['paper']['paper'])
