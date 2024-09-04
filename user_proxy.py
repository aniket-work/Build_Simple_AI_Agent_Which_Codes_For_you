import autogen
import io
import sys
from constants import MAX_CONSECUTIVE_AUTO_REPLY, CODE_EXECUTION_TIMEOUT


class StreamlitUserProxy(autogen.UserProxyAgent):
    def __init__(self, name):
        super().__init__(
            name=name,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=MAX_CONSECUTIVE_AUTO_REPLY,
            is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
            code_execution_config={
                "work_dir": "temp",
                "use_docker": False,
                "timeout": CODE_EXECUTION_TIMEOUT,
            },
        )

    def get_human_input(self, prompt):
        return None  # No human input in this case

    def run_code(self, code, **kwargs):
        result = io.StringIO()
        error = io.StringIO()
        sys.stdout = result
        sys.stderr = error

        try:
            exec(code)
            output = result.getvalue()
            error_msg = error.getvalue()
            exitcode = 0
        except Exception as e:
            output = ""
            error_msg = str(e)
            exitcode = 1
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

        return exitcode, output, error_msg