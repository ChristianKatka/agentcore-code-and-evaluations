from bedrock_agentcore_starter_toolkit import Evaluation
from boto3.session import Session
import sys


region = "us-east-1"
agent_id = "strands_claude_getting_started-p5llts4z2q"
session_id = "123456789"

eval_client = Evaluation(region=region)


print(f"Running on-demand evaluation for Agent: {agent_id}")
print(f"Session: {session_id}")
print("-" * 50)

# Run evaluation with built-in metrics
print("\n1. Evaluating Goal Success Rate...")
goal_success_results = eval_client.run(
    agent_id=agent_id,
    session_id=session_id,
    evaluators=["Builtin.GoalSuccessRate"]
)

for result in goal_success_results.results:
    print(f"\nGoal Success: {result.label} ({result.value})")
    print(f"Explanation: {result.explanation}")

# Run evaluation for Correctness
print("\n2. Evaluating Correctness...")
correctness_results = eval_client.run(
    agent_id=agent_id,
    session_id=session_id,
    evaluators=["Builtin.Correctness"]
)

for result in correctness_results.results:
    print(f"\nCorrectness: {result.label} ({result.value})")
    print(f"Explanation: {result.explanation}")

# Run evaluation for Tool Selection and Parameter Accuracy
print("\n3. Evaluating Tool Selection and Parameter Accuracy...")
tool_results = eval_client.run(
    agent_id=agent_id,
    session_id=session_id,
    evaluators=["Builtin.ToolParameterAccuracy", "Builtin.ToolSelectionAccuracy"]
)

for result in tool_results.results:
    print(f"\nMetric: {result.evaluator_name}")
    print(f"Value: {result.label} ({result.value})")
    print(f"Explanation: {result.explanation}")

# Save results to file
print("\n4. Saving evaluation results to file...")
save_results = eval_client.run(
    agent_id=agent_id,
    session_id=session_id,
    evaluators=[
        "Builtin.GoalSuccessRate",
        "Builtin.Correctness",
        "Builtin.ToolParameterAccuracy",
        "Builtin.ToolSelectionAccuracy"
    ],
    output="eval_results/on_demand_results.json"
)

print("\n✓ On-demand evaluation complete!")
print("Results saved to: eval_results/on_demand_results.json")
