import streamlit as st

from src.model import get_agent


def reset_session():
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you?"}
    ]
    st.session_state.conversation = get_agent()


def sidebar():
    with st.sidebar:
        st.title(":tropical_drink: Chat with Mixtral")
        st.markdown(
            "Mixtral is a new large language model developed by Mistral AI, a French artificial intelligence company.")

    st.sidebar.button("Clear chat history", on_click=reset_session, use_container_width=True)