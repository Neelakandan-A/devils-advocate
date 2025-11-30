import os
import logging
from typing import List, Dict, Any, Optional, Callable
import google.generativeai as genai
from colorama import Fore, Style

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Agent:
    def __init__(self, name: str, model: str = "gemini-2.5-flash", instructions: str = "", tools: List[Any] = None):
        self.name = name
        self.model_name = model
        self.instructions = instructions
        self.tools = tools or []
        self.history = []
        
        # Initialize Gemini
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            logger.warning("GOOGLE_API_KEY not found. Running in MOCK mode.")
            self.model = None
        else:
            try:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel(model_name=self.model_name, tools=self.tools)
                self.chat = self.model.start_chat(history=[])
            except Exception as e:
                logger.warning(f"Failed to initialize Gemini model: {e}. Running in mock mode.")
                self.model = None

    def run(self, input_text: str, context: Dict[str, Any] = None) -> str:
        logger.info(f"Agent {self.name} received input: {input_text[:50]}...")
        print(f"{Fore.CYAN}[{self.name}]{Style.RESET_ALL} Processing...")
        
        full_prompt = f"{self.instructions}\n\nContext: {context}\n\nUser Input: {input_text}"
        
        if self.model:
            try:
                response = self.chat.send_message(full_prompt)
                output = response.text
            except Exception as e:
                logger.error(f"Error generating response: {e}")
                output = f"Error: {e}"
        else:
            # Mock response for testing without API key
            output = f"[MOCK] {self.name} processed: {input_text}"
            
        print(f"{Fore.GREEN}[{self.name}]{Style.RESET_ALL} Response: {output[:100]}...")
        return output

class LoopAgent(Agent):
    def __init__(self, name: str, model: str, instructions: str, tools: List[Any], validation_checker: Callable[[str], bool], max_loops: int = 3):
        super().__init__(name, model, instructions, tools)
        self.validation_checker = validation_checker
        self.max_loops = max_loops

    def run(self, input_text: str, context: Dict[str, Any] = None) -> str:
        loops = 0
        current_input = input_text
        final_response = ""
        
        while loops < self.max_loops:
            logger.info(f"LoopAgent {self.name} iteration {loops + 1}")
            response = super().run(current_input, context)
            final_response = response
            
            if self.validation_checker(response):
                logger.info(f"LoopAgent {self.name} validation passed.")
                break
            
            loops += 1
            current_input = f"Previous response was incomplete or needs refinement. Please address: {response}"
            
        return final_response

class Orchestrator:
    def __init__(self):
        self.agents = {}
        self.session_state = {}

    def register_agent(self, agent: Agent):
        self.agents[agent.name] = agent

    def process(self, user_input: str) -> str:
        raise NotImplementedError("Orchestrator process method must be implemented by subclass")
