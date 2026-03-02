from bedrock_agentcore_starter_toolkit import Evaluation
from boto3.session import Session
import sys
import os

# Initialize boto session
boto_session = Session()
region = boto_session.region_name

# Initialize Evaluation client
eval_client = Evaluation(region=region)

# Get config_id from command line, file, or prompt
if len(sys.argv) > 1:
    config_id = sys.argv[1]
elif os.path.exists("eval_config_id.txt"):
    with open("eval_config_id.txt", "r") as f:
        config_id = f.read().strip()
    print(f"Using config ID from file: {config_id}")
else:
    config_id = input("Enter your Online Evaluation Configuration ID: ")

print(f"\nChecking online evaluation configuration...")
print("-" * 50)

# Get configuration details
config_details = eval_client.get_online_config(config_id=config_id)

print("\nConfiguration Details:")
print(f"Config ID: {config_details.get('onlineEvaluationConfigId')}")
print(f"Config Name: {config_details.get('onlineEvaluationConfigName')}")
print(f"Status: {config_details.get('status')}")
print(f"Sampling Rate: {config_details.get('samplingRate')}%")
print(f"Description: {config_details.get('description')}")

print("\nEvaluators:")
for evaluator in config_details.get('evaluators', []):
    print(f"  - {evaluator.get('evaluatorId')}")

print("\n✓ Configuration is active and monitoring your agent!")
print("\nTo view evaluation results, visit:")
print("https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability/agent-core/agents")
