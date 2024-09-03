import streamlit as st
from assistant import create_assistant
from user_proxy import StreamlitUserProxy
from utils import run_assistant, run_code_block

def main():
    st.set_page_config(page_title="AI Coding Assistant", layout="wide")
    st.title("AI Coding Assistant")

    assistant = create_assistant()
    user_proxy = StreamlitUserProxy("user_proxy")

    user_input = st.text_area("Enter your coding task or question:", height=100)

    if st.button("Get Assistance"):
        if user_input:
            chat_history = run_assistant(user_input, user_proxy, assistant)

            for msg in chat_history:
                role = msg['role']
                content = msg['content']

                if role == "human":
                    st.write("You:")
                    st.write(content)
                elif role == "assistant":
                    st.write("AI Assistant:")
                    st.write(content)

                    code_blocks = content.split("```")
                    for i in range(1, len(code_blocks), 2):
                        code = code_blocks[i].strip()
                        language = code.split("\n")[0]
                        code = "\n".join(code.split("\n")[1:])

                        st.code(code, language=language)

                        if st.button(f"Run Code Block {i // 2 + 1}"):
                            run_code_block(code, user_proxy)
        else:
            st.warning("Please enter a coding task or question.")

if __name__ == "__main__":
    main()