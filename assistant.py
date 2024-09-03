import autogen
from constants import ASSISTANT_NAME, ASSISTANT_SYSTEM_MESSAGE
import json


def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)


def create_assistant():
    config = load_config()

    assistant = autogen.AssistantAgent(
        name=ASSISTANT_NAME,
        llm_config={"config_list": config['llm_config'], "seed": config['seed']},
        system_message=ASSISTANT_SYSTEM_MESSAGE
    )

    return assistant