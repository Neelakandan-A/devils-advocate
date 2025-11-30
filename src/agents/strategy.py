from .base import Agent

class StrategyAgent(Agent):
    def __init__(self):
        instructions = """
        You are the Strategy & Action Agent.
        Based on the facts, legal research, and risk assessment, formulate a concrete plan.
        
        Create a step-by-step Action Plan:
        1. Immediate actions (e.g., "Send demand letter").
        2. Deadlines.
        3. Negotiation talking points.
        4. Evidence gathering checklist.
        5. Escalation path (when to hire a lawyer).
        
        Be specific and actionable.
        """
        super().__init__(name="StrategyAgent", instructions=instructions)
