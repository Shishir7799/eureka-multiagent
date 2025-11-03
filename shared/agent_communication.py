import json
import os
from typing import Dict, Any
from google.cloud import firestore

class AgentCommunication:
    def __init__(self, project_id):
        self.db = firestore.Client(project=project_id)
        self.project_id = project_id
    
    def send_message(self, from_agent: str, to_agent: str, message: Dict[str, Any]):
        """Send message from one agent to another"""
        doc_id = f"{from_agent}_to_{to_agent}_{int(time.time())}"
        self.db.collection('messages').document(doc_id).set({
            'from': from_agent,
            'to': to_agent,
            'message': message,
            'timestamp': firestore.SERVER_TIMESTAMP,
            'status': 'pending'
        })
        return doc_id
    
    def receive_message(self, agent_name: str):
        """Receive messages for an agent"""
        docs = self.db.collection('messages')\
            .where('to', '==', agent_name)\
            .where('status', '==', 'pending')\
            .stream()
        
        messages = []
        for doc in docs:
            data = doc.to_dict()
            messages.append(data)
            # Mark as processed
            doc.reference.update({'status': 'processed'})
        
        return messages
    
    def store_result(self, agent_name: str, result: Dict[str, Any]):
        """Store agent result"""
        self.db.collection('agent_results').document(agent_name).set({
            'agent': agent_name,
            'result': result,
            'timestamp': firestore.SERVER_TIMESTAMP
        })

import time
