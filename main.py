import os
import sys
from dotenv import load_dotenv
from src.agents.orchestrator import DevilsAdvocateOrchestrator
from colorama import init, Fore, Style

# Initialize colorama
init()

def main():
    load_dotenv()
    
    print(f"{Fore.RED}=================================================={Style.RESET_ALL}")
    print(f"{Fore.RED}   DEVIL'S ADVOCATE: AI Legal Advisor             {Style.RESET_ALL}")
    print(f"{Fore.RED}=================================================={Style.RESET_ALL}")
    print("Welcome. I am here to challenge your assumptions and help you navigate your legal issue.")
    print("Please describe your situation in detail.")
    
    # In a real app, we might take command line args or run a loop
    # For this demo, we'll take one initial input or use a preset scenario if empty
    
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        print("\n(Enter your case details below. Press Enter twice to submit.)")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        user_input = "\n".join(lines)
        
    if not user_input.strip():
        print("No input provided. Using default scenario: 'Sarah's landlord won't return her $2,000 security deposit.'")
        user_input = "My landlord won't return my $2,000 security deposit. I moved out 30 days ago and gave him my new address. He says the place was dirty, but I cleaned it."

    orchestrator = DevilsAdvocateOrchestrator()
    result = orchestrator.process(user_input)
    
    print(f"\n{Fore.YELLOW}================ FINAL REPORT ================{Style.RESET_ALL}")
    print(result)
    
    # Save report to file
    with open("case_report.md", "w") as f:
        f.write(result)
    print(f"\n{Fore.GREEN}Report saved to case_report.md{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
