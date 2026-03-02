from bedrock_agentcore_starter_toolkit import Evaluation
from boto3.session import Session
import sys

# Initialize boto session
boto_session = Session()
region = boto_session.region_name

# Initialize Evaluation client
eval_client = Evaluation(region=region)

# Get agent_id from command line or prompt
if len(sys.argv) > 1:
    agent_id = sys.argv[1]
else:
    agent_id = input("Enter your Agent ID: ")

config_name = input("Enter a name for this evaluation config (default: strands_agent_online_eval): ") or "strands_agent_online_eval"
sampling_rate = input("Enter sampling rate percentage (default: 100): ") or "100"

print(f"\nCreating online evaluation configuration for Agent: {agent_id}")
print(f"Config Name: {config_name}")
print(f"Sampling Rate: {sampling_rate}%")
print("-" * 50)

# Create online evaluation configuration
response = eval_client.create_online_config(
    agent_id=agent_id,
    config_name=config_name,
    sampling_rate=int(sampling_rate),
    evaluator_list=[
        "Builtin.GoalSuccessRate",
        "Builtin.Correctness",
        "Builtin.ToolParameterAccuracy",
        "Builtin.ToolSelectionAccuracy"
    ],
    config_description="Online evaluation for Strands agent with built-in metrics",
    auto_create_execution_role=True
)

print("\n✓ Online evaluation configuration created!")
print(f"Configuration ID: {response['onlineEvaluationConfigId']}")
print("\nYou can now invoke your agent and the evaluation will run automatically.")
print("View results in the AgentCore Observability console:")
print("https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability/agent-core/agents")

# Save config ID for later use
with open("eval_config_id.txt", "w") as f:
    f.write(response['onlineEvaluationConfigId'])
print("\nConfiguration ID saved to: eval_config_id.txt")
