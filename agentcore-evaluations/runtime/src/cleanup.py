import boto3
from boto3.session import Session

# You need to set these values from your deployment
# Get them from deploy.py output
AGENT_ID = input("Enter your Agent ID: ")
ECR_REPOSITORY_NAME = input("Enter your ECR repository name: ")

boto_session = Session()
region = boto_session.region_name

agentcore_control_client = boto3.client('bedrock-agentcore-control', region_name=region)
ecr_client = boto3.client('ecr', region_name=region)

print("Deleting AgentCore Runtime...")
try:
    runtime_delete_response = agentcore_control_client.delete_agent_runtime(
        agentRuntimeId=AGENT_ID
    )
    print("✓ AgentCore Runtime deleted")
except Exception as e:
    print(f"✗ Error deleting runtime: {e}")

print("\nDeleting ECR repository...")
try:
    ecr_delete_response = ecr_client.delete_repository(
        repositoryName=ECR_REPOSITORY_NAME,
        force=True
    )
    print("✓ ECR repository deleted")
except Exception as e:
    print(f"✗ Error deleting ECR repository: {e}")

print("\nCleanup complete!")
