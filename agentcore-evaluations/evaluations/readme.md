## Evaluating Your Agent

AgentCore Evaluations provides two types of evaluation: on-demand and online.

### On-Demand Evaluation

Evaluate specific agent sessions after they've been executed. This is useful for investigating specific interactions or validating fixes.

```bash
python eval_on_demand.py
```

You'll be prompted for:

- Agent ID (from deploy.py output)
- Session ID (from your agent invocations)

The script will evaluate:

- Goal Success Rate (session-level)
- Correctness (trace-level)
- Tool Selection Accuracy (span-level)
- Tool Parameter Accuracy (span-level)

Results are saved to `eval_results/on_demand_results.json`

### Online Evaluation

Set up continuous monitoring of your agent in production. This automatically evaluates agent interactions based on sampling rate.

#### Setup Online Evaluation

```bash
python eval_online_setup.py
```

You'll be prompted for:

- Agent ID
- Configuration name
- Sampling rate (percentage of sessions to evaluate)

This creates an online evaluation configuration that continuously monitors your agent.

#### Check Online Evaluation Status

```bash
python eval_online_check.py
```

View detailed results in the [AgentCore Observability Console](https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability/agent-core/agents)

### Evaluation Metrics

Built-in metrics available:

- **Builtin.GoalSuccessRate** - Did the agent achieve the user's goal?
- **Builtin.Correctness** - Is the response factually correct?
- **Builtin.ToolSelectionAccuracy** - Did the agent select the right tools?
- **Builtin.ToolParameterAccuracy** - Did the agent use correct parameters?

## Cleanup

When you're done, delete the AgentCore Runtime and ECR repository to avoid charges.

```bash
python cleanup.py
```

## Files Overview

### Agent Deployment

- **main.py** - Your Strands agent with AgentCore Runtime integration
- **deploy.py** - Configures and launches the agent to AgentCore Runtime
- **check_status.py** - Monitors deployment status
- **invoke_agent.py** - Invokes the agent using the starter toolkit
- **invoke_with_boto3.py** - Invokes the agent using boto3 directly
- **cleanup.py** - Deletes the AgentCore Runtime and ECR repository

### Agent Evaluation

- **eval_on_demand.py** - Run on-demand evaluation on specific sessions
- **eval_online_setup.py** - Create online evaluation configuration for continuous monitoring
- **eval_online_check.py** - Check online evaluation configuration status

## What Happens Behind the Scenes

When you use `BedrockAgentCoreApp`, it automatically:

- Creates an HTTP server listening on port 8080
- Implements the `/invocations` endpoint for processing requests
- Implements the `/ping` endpoint for health checks
- Handles proper content types and response formats
- Manages error handling according to AWS standards

The starter toolkit handles:

- Auto-generating a Dockerfile based on your code
- Building the Docker container
- Creating and pushing to ECR
- Deploying to AgentCore Runtime
