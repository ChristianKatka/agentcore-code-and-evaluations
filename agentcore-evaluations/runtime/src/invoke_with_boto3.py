import boto3
import json
from boto3.session import Session

# You need to set these values from your deployment
# Get them from deploy.py output or check_status.py
AGENT_ARN = input("Enter your Agent ARN: ")

boto_session = Session()
region = boto_session.region_name

agentcore_client = boto3.client('bedrock-agentcore', region_name=region)

prompt = input("Enter your prompt (or press Enter for default): ") or "What is 2+2?"

print(f"\nInvoking agent with prompt: '{prompt}'")
print("-" * 50)

response = agentcore_client.invoke_agent_runtime(
    agentRuntimeArn=AGENT_ARN,
    qualifier="DEFAULT",
    payload=json.dumps({"prompt": prompt})
)

# Process response
if "text/event-stream" in response.get("contentType", ""):
    content = []
    for line in response["response"].iter_lines(chunk_size=1):
        if line:
            line = line.decode("utf-8")
            if line.startswith("data: "):
                line = line[6:]
                print(line)
                content.append(line)
else:
    try:
        events = []
        for event in response.get("response", []):
            events.append(event)
        if events:
            print(json.loads(events[0].decode("utf-8")))
    except Exception as e:
        print(f"Error reading response: {e}")
