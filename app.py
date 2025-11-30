import streamlit as st
import os
from dotenv import load_dotenv
from src.agents.orchestrator import DevilsAdvocateOrchestrator
import time

# Page Config
st.set_page_config(
    page_title="Devil's Advocate AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for "Rich Aesthetics"
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
    }
    .stTextArea>div>div>textarea {
        background-color: #262730;
        color: white;
        border-radius: 10px;
    }
    h1 {
        color: #ff4b4b;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .report-container {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/3d-fluency/94/law.png", width=100)
    st.title("Devil's Advocate")
    st.markdown("### AI Legal Advisor")
    st.markdown("---")
    st.markdown("""
    **How it works:**
    1. 🗣️ **Intake**: We gather facts.
    2. 😈 **Challenge**: We test your case.
    3. 📚 **Research**: We find the law.
    4. ♟️ **Strategy**: We build a plan.
    """)
    st.markdown("---")
    
    api_key = st.text_input("Google API Key", type="password", help="Enter your Gemini API Key here if not in .env")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key

# Main Content
st.title("⚖️ Devil's Advocate")
st.subheader("Your AI Legal Team. Affordable. Accessible. Ruthless.")

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area(
        "Describe your legal situation:",
        height=200,
        placeholder="e.g., My landlord is withholding my $2000 security deposit claiming I damaged the carpet, but I have photos showing it was clean..."
    )

    if st.button("Analyze My Case"):
        if not user_input:
            st.warning("Please describe your situation first.")
        else:
            load_dotenv()
            
            # Progress Container
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Callback function to update UI
            def update_progress(msg):
                status_text.markdown(f"**🔄 {msg}**")
                # Simple logic to advance progress bar based on phases
                if "Phase 1" in msg: progress_bar.progress(10)
                elif "Phase 2" in msg: progress_bar.progress(30)
                elif "Phase 3" in msg: progress_bar.progress(50)
                elif "Phase 4" in msg: progress_bar.progress(70)
                elif "Phase 5" in msg: progress_bar.progress(90)
                elif "Finalizing" in msg: progress_bar.progress(100)
                time.sleep(0.5) # Visual delay for effect

            try:
                orchestrator = DevilsAdvocateOrchestrator()
                
                with st.spinner("The legal team is convening..."):
                    result = orchestrator.process(user_input, progress_callback=update_progress)
                
                st.success("Analysis Complete!")
                
                # Display Result
                st.markdown("### 📑 Case Report")
                st.markdown(f"""
                <div class="report-container">
                {result}
                </div>
                """, unsafe_allow_html=True)
                
                # Download Button
                st.download_button(
                    label="Download Report",
                    data=result,
                    file_name="legal_case_report.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

with col2:
    st.info("💡 **Tip**: Be specific about dates, amounts, and any written evidence you have.")
    st.markdown("### Active Agents")
    st.markdown("✅ **Intake Agent**")
    st.markdown("✅ **Devil's Advocate**")
    st.markdown("✅ **Research Agent**")
    st.markdown("✅ **Risk Agent**")
    st.markdown("✅ **Strategy Agent**")
    st.markdown("✅ **Document Agent**")

# Footer
st.markdown("---")
st.markdown("*Disclaimer: This is an AI prototype for educational purposes. Not professional legal advice.*")
