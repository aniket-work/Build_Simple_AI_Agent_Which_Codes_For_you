import streamlit as st


def run_assistant(message, user_proxy, assistant):
    chat_history = []

    user_proxy.initiate_chat(
        assistant,
        message=message,
        callback=lambda x: chat_history.append(x)
    )

    return chat_history


def run_code_block(code, user_proxy):
    exitcode, output, error = user_proxy.run_code(code)
    if output:
        st.write("Output:")
        st.text(output)

        if output.strip().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            st.image(output.strip())
    if error:
        st.error(f"Error: {error}")