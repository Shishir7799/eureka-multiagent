import os

# Google Cloud Config
PROJECT_ID = os.getenv('GCP_PROJECT_ID', 'eureka-hackathon')
REGION = 'europe-west1'

# Agent Endpoints (will be updated after deployment)
AGENT_ENDPOINTS = {
    'agent1': 'https://agent1-xxxxx.run.app',
    'agent2': 'https://agent2-xxxxx.run.app',
    'agent3': 'https://agent3-xxxxx.run.app',
    'agent4': 'https://agent4-xxxxx.run.app',
    'agent5': 'https://agent5-xxxxx.run.app',
    'agent6': 'https://agent6-xxxxx.run.app',
    'agent7': 'https://agent7-xxxxx.run.app',
}

# AI Studio Config
AI_STUDIO_API_KEY = os.getenv('AI_STUDIO_API_KEY')
GEMINI_MODEL = 'gemini-1.5-pro'

# GPU Config
GPU_TYPE = 'nvidia-tesla-l4'
GPU_COUNT = 1
