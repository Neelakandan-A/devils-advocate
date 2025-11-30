from .base import Orchestrator
from .intake import IntakeAgent
from .devils_advocate import DevilsAdvocateAgent
from .research import ResearchAgent
from .risk import RiskAgent
from .strategy import StrategyAgent
from .document import DocumentAgent
import logging

logger = logging.getLogger(__name__)

class DevilsAdvocateOrchestrator(Orchestrator):
    def __init__(self):
        super().__init__()
        self.intake = IntakeAgent()
        self.devils_advocate = DevilsAdvocateAgent()
        self.research = ResearchAgent()
        self.risk = RiskAgent()
        self.strategy = StrategyAgent()
        self.document = DocumentAgent()
        
        self.register_agent(self.intake)
        self.register_agent(self.devils_advocate)
        self.register_agent(self.research)
        self.register_agent(self.risk)
        self.register_agent(self.strategy)
        self.register_agent(self.document)

    def process(self, user_input: str, progress_callback=None) -> str:
        # Helper to report progress
        def report(msg):
            if progress_callback:
                progress_callback(msg)
            else:
                print(msg)

        report("Phase 1: Intake & Classification...")
        intake_summary = self.intake.run(user_input)
        
        report("Phase 2: Devil's Advocate Challenge (Looping)...")
        challenge_result = self.devils_advocate.run(intake_summary)
        
        report("Phase 3: Running Parallel Research & Risk Assessment...")
        # In a real async environment, these would run in parallel
        research_result = self.research.run(intake_summary)
        risk_result = self.risk.run(intake_summary)
        
        context = {
            "intake": intake_summary,
            "challenges": challenge_result,
            "research": research_result,
            "risk": risk_result
        }
        
        report("Phase 4: Formulating Strategy...")
        strategy_plan = self.strategy.run("Develop a strategy based on the context.", context=context)
        
        report("Phase 5: Generating Legal Documents...")
        documents = self.document.run("Generate necessary documents based on the strategy.", context={"strategy": strategy_plan})
        
        report("Finalizing Report...")
        
        final_report = f"""
        # Devil's Advocate Case Report
        
        ## Case Summary
        {intake_summary}
        
        ## Critical Analysis (Devil's Advocate)
        {challenge_result}
        
        ## Legal Framework
        {research_result}
        
        ## Risk Assessment
        {risk_result}
        
        ## Strategic Plan
        {strategy_plan}
        
        ## Generated Documents
        {documents}
        """
        
        return final_report
