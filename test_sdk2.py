import os
os.environ["AZURE_IDENTITY_DISABLE_IMDS"] = "1"
os.environ["OTEL_TRACES_EXPORTER"] = "none"

import json
import logging
logging.basicConfig(level=logging.DEBUG)

from azure.ai.agentserver.responses import ResponsesAgentServerHost, TextResponse

server = ResponsesAgentServerHost()

@server.response_handler
def analyze_code(request, context, cancellation_signal):
    try:
        code = "def test(): pass"
        return TextResponse(context=context, request=request, text=f'{{"code": "{code}"}}')
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    server.run()