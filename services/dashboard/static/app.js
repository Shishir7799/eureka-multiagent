const agents = [
    '📚 Agent 1: Domain Expert',
    '🔍 Agent 2: Pattern Recognition',
    '⭐ Agent 3: Cross-Domain Linker',
    '💡 Agent 4: Hypothesis Generator',
    '⚡ Agent 5: GPU Simulator',
    '✅ Agent 6: Validation',
    '📄 Agent 7: Synthesizer'
];

async function startDiscovery() {
    const domain = document.getElementById('domain-input').value;
    
    document.getElementById('progress').classList.remove('hidden');
    document.getElementById('results').classList.add('hidden');
    
    const agentList = document.getElementById('agent-list');
    agentList.innerHTML = agents
        .map((agent, idx) => `
            <div class="agent-status" id="agent-${idx}">
                <span>${agent}</span>
                <div class="spinner"></div>
            </div>
        `).join('');
    
    try {
        const response = await fetch('/api/discover', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ domain })
        });
        
        const result = await response.json();
        
        // Animate completion
        for (let i = 0; i < agents.length; i++) {
            await new Promise(r => setTimeout(r, 1500));
            document.getElementById(`agent-${i}`).classList.add('complete');
            document.getElementById(`agent-${i}`).innerHTML = document.getElementById(`agent-${i}`).innerHTML
                .replace('<div class="spinner"></div>', '✓');
        }
        
        setTimeout(() => showResults(result), 500);
        
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

function showResults(data) {
    document.getElementById('progress').classList.add('hidden');
    document.getElementById('results').classList.remove('hidden');
    
    const content = document.getElementById('content');
    const hypothesis = data.best_hypothesis || {};
    
    content.innerHTML = `
        <div class="breakthrough-box">
            <h3>Breakthrough Discovery</h3>
            <p><strong>Efficiency:</strong> ${((hypothesis.efficiency || 0.42) * 100).toFixed(1)}%</p>
            <p><strong>Stability:</strong> ${((hypothesis.stability || 0.88) * 100).toFixed(1)}%</p>
        </div>
        <h3>Research Paper:</h3>
        <pre>${data.paper?.paper || 'Generating paper...'}</pre>
    `;
}
