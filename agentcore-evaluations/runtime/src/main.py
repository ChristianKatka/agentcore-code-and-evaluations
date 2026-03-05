from strands import Agent, tool
from strands_tools import calculator
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Initialize the AgentCore Runtime app
app = BedrockAgentCoreApp()

# Custom tool 
@tool
def weather():
    """ Get weather """ 
    return "sunny"


# Initialize the Bedrock model
model_id = "amazon.nova-pro-v1:0"
model = BedrockModel(
    model_id=model_id,
)

# Create the agent with tools and system prompt
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather."
)


# Define the entrypoint for AgentCore Runtime
@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    print("User input:", user_input)
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()
