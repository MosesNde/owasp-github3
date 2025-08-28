 from typing_extensions import Literal
 from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, root_validator
 from typing import Optional, Dict, Any, Union
 from dotenv import load_dotenv
 import traceback
 
 import uvicorn
 
# from cerebrum.llm.layer import LLMLayer as LLMConfig
# from cerebrum.memory.layer import MemoryLayer as MemoryConfig
# from cerebrum.storage.layer import StorageLayer as StorageConfig
# from cerebrum.tool.layer import ToolLayer as ToolManagerConfig

 load_dotenv()
 
 app = FastAPI()
 )
 
 # Store component configurations and instances
 active_components = {
     "llm": None,
     "storage": None,
     query_type: Literal["llm", "tool", "storage", "memory"]
     query_data: LLMQuery | ToolQuery | StorageQuery | MemoryQuery
 
    @root_validator(pre=True)
    def convert_query_data(cls, values: dict[str, Any]) -> dict[str, Any]:
        if 'query_type' not in values or 'query_data' not in values:
            return values
            
        query_type = values['query_type']
        query_data = values['query_data']
        
        type_mapping = {
            'llm': LLMQuery,
            'tool': ToolQuery,
            'storage': StorageQuery,
            'memory': MemoryQuery
        }
        
        if isinstance(query_data, type_mapping[query_type]):
            return values
            
        if isinstance(query_data, dict):
            values['query_data'] = type_mapping[query_type](**query_data)
            
        return values
 
 def initialize_llm_cores(config: dict) -> Any:
     """Initialize LLM core with configuration."""
         
         # Initialize new components
         active_components = initialize_components()
        # if not initialize_components():
        #     raise Exception("Failed to initialize components")
             
         print("✅ All components reinitialized successfully")
         
 async def refresh_configuration():
     """Refresh all component configurations"""
     try:
        print("Received refresh request")
         config.refresh()
        print("Configuration reloaded")
         restart_kernel()
        print("Kernel restarted")
         return {
             "status": "success", 
             "message": "Configuration refreshed and components reinitialized"
             config=config.agent_config
         )
         
        
         return {
             "status": "success",
             "execution_id": execution_id,
             "message": f"Agent {config.agent_id} submitted for execution"
         }
     except Exception as e:
         error_msg = str(e)
         stack_trace = traceback.format_exc()
         data = await request.json()
         logger.info(f"Received config update request: {data}")
         
         provider = data.get("provider")
         api_key = data.get("api_key")
         
         if not all([provider, api_key]):
             raise ValueError("Missing required fields: provider, api_key")
         
        # Update configuration
        config.config["api_keys"][provider] = api_key
         config.save_config()
         
         # Try to reinitialize LLM component