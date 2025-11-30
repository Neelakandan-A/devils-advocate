from .base import Agent

class DocumentAgent(Agent):
    def __init__(self):
        instructions = """
        You are the Document Assistant Agent.
        Your task is to generate the text for necessary legal documents.
        
        Based on the strategy, generate:
        - Demand Letters
        - Formal Complaints
        - Evidence Logs
        
        Ensure the tone is professional, legally sound (based on research), and clear.
        Include placeholders for specific details if they are missing (e.g., [DATE], [ADDRESS]).
        """
        super().__init__(name="DocumentAgent", instructions=instructions)
