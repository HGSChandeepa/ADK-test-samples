import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search


# Function to fet the current time
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


# Function to find the factorial of a number
def factorial(n: int) -> int:
    """
    Calculate the factorial of a number
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search],
    # tools=[factorial , get_current_time],  # <--- Works
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
