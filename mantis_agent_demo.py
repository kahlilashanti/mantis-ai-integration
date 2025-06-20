from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from mantis_tools import (
    load_experience,
    go_to_scene,
    update_scene,
    get_current_scene
)

llm = ChatOpenAI(model="gpt-4", temperature=0)

tools = [
    load_experience,
    go_to_scene,
    update_scene,
    get_current_scene
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example prompt
result = agent.run(
    "Load the Cubs experience from https://mantisxr.com/cubs, go to the suite scene, and change the logo to https://adidas.com/logo.png."
)

print("\n\nAgent Result:\n", result)
