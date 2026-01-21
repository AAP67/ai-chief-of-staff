import streamlit as st
import os
from anthropic import Anthropic
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import custom modules
from system_prompt import CHIEF_OF_STAFF_PROMPT
from utils.file_processor import process_uploaded_file

# Page configuration
st.set_page_config(
    page_title="AI Chief of Staff",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Anthropic client
@st.cache_resource
def get_anthropic_client():
    # Try to get API key from Streamlit secrets (for deployment)
    # Falls back to environment variable (for local development)
    api_key = None
    
    # Try Streamlit secrets first (for deployment)
    try:
        api_key = st.secrets.get("ANTHROPIC_API_KEY")
    except (FileNotFoundError, KeyError):
        pass
    
    # Fall back to environment variable
    if not api_key:
        api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        st.error("⚠️ ANTHROPIC_API_KEY not found. Please set it in your environment variables or Streamlit secrets.")
        st.info("""
        **For local development:** Create a `.env` file with `ANTHROPIC_API_KEY=your_key`
        
        **For Streamlit Cloud:** Add your API key in Settings → Secrets
        """)
        st.stop()
    
    return Anthropic(api_key=api_key)

client = get_anthropic_client()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files_content" not in st.session_state:
    st.session_state.uploaded_files_content = []

# Sidebar
with st.sidebar:
    st.title("🎯 AI Chief of Staff")
    st.markdown("---")
    
    st.subheader("Analysis Mode")
    analysis_mode = st.selectbox(
        "Choose analysis depth:",
        ["Quick Take", "Deep Dive", "Scenario Analysis"]
    )
    
    st.markdown("---")
    st.subheader("📎 Upload Documents")
    st.caption("Upload pitch decks, financials, market research")
    
    uploaded_files = st.file_uploader(
        "Drop files here",
        accept_multiple_files=True,
        type=['pdf', 'pptx', 'xlsx', 'csv', 'txt', 'md']
    )
    
    if uploaded_files:
        for file in uploaded_files:
            if file.name not in [f['name'] for f in st.session_state.uploaded_files_content]:
                with st.spinner(f"Processing {file.name}..."):
                    content = process_uploaded_file(file)
                    st.session_state.uploaded_files_content.append({
                        'name': file.name,
                        'content': content
                    })
                st.success(f"✓ {file.name} processed")
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.uploaded_files_content = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Built for Series A/B founders")
    st.caption("Direct strategic analysis, no BS")

# Main chat interface
st.title("💼 Your AI Chief of Staff & BizOps Lead")

# Show example prompts if no conversation yet
if len(st.session_state.messages) == 0:
    st.markdown("""
    ### What I can help you with:
    
    **Strategic Decisions:**
    - "Should we enter the enterprise market or focus on SMB?"
    - "Evaluate this partnership opportunity with [Company X]"
    - "Help me think through our pricing strategy"
    
    **Deal Analysis:**
    - "Here's a pitch deck - should we invest/acquire?"
    - "Analyze this competitor and our positioning"
    - "Review our financial model and projections"
    
    **Board/Investor Prep:**
    - "Help me frame our pivot for the board"
    - "Create talking points for our Series B pitch"
    - "Stress-test our growth assumptions"
    
    **Just upload files and ask me anything.**
    """)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything - strategic decisions, deal analysis, planning..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare context with uploaded files
    context = ""
    if st.session_state.uploaded_files_content:
        context = "\n\n**UPLOADED DOCUMENTS:**\n\n"
        for file_data in st.session_state.uploaded_files_content:
            context += f"\n### {file_data['name']}\n{file_data['content']}\n"
    
    # Add analysis mode instruction
    mode_instruction = {
        "Quick Take": "\n\nProvide a quick, direct take (3-5 key points) on this.",
        "Deep Dive": "\n\nProvide a comprehensive analysis with valuation, competitive landscape, risks, and clear recommendation.",
        "Scenario Analysis": "\n\nProvide Bull/Base/Bear scenarios with key assumptions and probability-weighted outcomes."
    }
    
    full_prompt = prompt + mode_instruction[analysis_mode]
    if context:
        full_prompt = context + "\n\n" + full_prompt
    
    # Get Claude's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Thinking..."):
            try:
                # Call Claude API with streaming
                with client.messages.stream(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4096,
                    system=CHIEF_OF_STAFF_PROMPT,
                    messages=[
                        {"role": m["role"], "content": m["content"]} 
                        for m in st.session_state.messages[:-1]
                    ] + [{"role": "user", "content": full_prompt}]
                ) as stream:
                    for text in stream.text_stream:
                        full_response += text
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                full_response = f"I encountered an error: {str(e)}"
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Export functionality
if len(st.session_state.messages) > 0:
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    
    with col2:
        # Create markdown export
        export_text = f"# AI Chief of Staff Analysis\n\n"
        export_text += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        export_text += "---\n\n"
        
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                export_text += f"## Question:\n{msg['content']}\n\n"
            else:
                export_text += f"## Analysis:\n{msg['content']}\n\n"
            export_text += "---\n\n"
        
        st.download_button(
            label="📥 Export Analysis",
            data=export_text,
            file_name=f"chief_of_staff_analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
            mime="text/markdown",
            use_container_width=True
        )
