import logging
from google.adk.agents.llm_agent import Agent

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def logging_tool(param: str) -> dict:
    """Інструмент з логуванням подій"""
    logger.info(f"Виклик інструменту logging_tool з параметром: {param}")
    return {"result": "success", "processed_param": param}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='logging_agent',
    description="Агент з логуванням.",
    instruction="Використовуй інструмент logging_tool та логуй всі дії.",
    tools=[logging_tool],
)