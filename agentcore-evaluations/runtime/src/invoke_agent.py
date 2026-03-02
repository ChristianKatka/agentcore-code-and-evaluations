from bedrock_agentcore_starter_toolkit import Runtime
import sys

# Initialize AgentCore Runtime
agentcore_runtime = Runtime()

# Get prompt from command line or use default
if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
else:
    prompt = "How is the weather now?"

print(f"Invoking agent with prompt: '{prompt}'")
print("-" * 50)

# Invoke the agent
invoke_response = agentcore_runtime.invoke({"prompt": prompt})

# Display response
if 'response' in invoke_response:
    response_text = invoke_response['response'][0]
    print(response_text)
else:
    print("Response:", invoke_response)
