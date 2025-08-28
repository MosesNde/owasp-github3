         from openai import OpenAI
         import os
 
        # Initialize OpenAI client with OpenRouter API for Deepseek R1
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPENROUTER_API_KEY"))
        self.model_name = "deepseek/deepseek-r1:free"  # Use Deepseek R1 model
         
        # Define function to query models through OpenRouter
         def query_model(system_msgs, user_msgs):
             if self.system_message_handling == "combined":
                 # Combine system and user messages into a single user message
         self.query_model = query_model
 
         self.action_set = HighLevelActionSet(
            subsets=["chat", "bid", "infeas"],
            strict=False,
            multiaction=False,
            demo_mode=demo_mode,
         )
 
         self.action_history = []
 
 class DemoAgentArgs(AbstractAgentArgs):
 
     agent_name: str = "DemoAgent"  # Agent name for the SDK to recognize
    model_name: str = "deepseek/deepseek-r1:free"  # Default model, can be changed at runtime
     chat_mode: bool = False        # Whether to enable chat mode
     demo_mode: str = "off"         # Visual effects mode (off, minimal, full)
     use_html: bool = False         # Whether to include HTML in observations
 
 
 # Example creating and using the DemoAgent
def run_demo_agent(model_name="deepseek/deepseek-r1:free", task_name="webclones.omnizon-1", headless=False, leaderboard=False, run_id=None):
     logger.info(f"Starting DemoAgent test with model: {model_name} on task: {task_name}")
     
     # Create the agent arguments with the specified parameters