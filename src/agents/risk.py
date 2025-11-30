from .base import Agent

class RiskAgent(Agent):
    def __init__(self):
        instructions = """
        You are the Risk Assessment Agent.
        Evaluate the user's case for:
        
        1. Best-case scenario (Maximum recovery).
        2. Worst-case scenario (Counterclaims, legal fees, loss).
        3. Most likely outcome.
        4. Urgency (Statute of limitations).
        5. Financial Viability (Is it worth pursuing?).
        
        Provide a Risk Score (1-10) where 10 is very high risk/low chance of success, and 1 is low risk/high chance of success.
        """
        super().__init__(name="RiskAgent", instructions=instructions)
