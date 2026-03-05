from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session


region = "us-east-1"

# Initialize AgentCore Runtime
agentcore_runtime = Runtime()
agent_name = "strands_claude_getting_started"

# Configure deployment
print("Configuring AgentCore Runtime deployment...")
response = agentcore_runtime.configure(
    entrypoint="main.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    agent_name=agent_name
)




print("Configuration complete:")
print(response)

# Launch the agent
print("\nLaunching agent to AgentCore Runtime...")
launch_result = agentcore_runtime.launch()
print("Launch initiated!")
print(f"Agent ARN: {launch_result.agent_arn}")
print(f"Agent ID: {launch_result.agent_id}")
print(f"ECR URI: {launch_result.ecr_uri}")


# https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main 
# 
# 