from bedrock_agentcore_starter_toolkit import Runtime
import time

# Initialize AgentCore Runtime
agentcore_runtime = Runtime()

print("Checking AgentCore Runtime status...")
status_response = agentcore_runtime.status()
status = status_response.endpoint['status']
end_status = ['READY', 'CREATE_FAILED', 'DELETE_FAILED', 'UPDATE_FAILED']

while status not in end_status:
    print(f"Current status: {status}")
    time.sleep(10)
    status_response = agentcore_runtime.status()
    status = status_response.endpoint['status']

print(f"\nFinal status: {status}")

if status == 'READY':
    print("✓ Agent is ready to use!")
else:
    print(f"✗ Deployment ended with status: {status}")
