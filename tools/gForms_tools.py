from mcp_server import mcp
from utils.gForms_interaction.read_gForm import get_form_responses
from typing import Dict, Any

@mcp.tool()


def get_form_responses_tool() -> Dict[str, Any]:
    return get_form_responses()