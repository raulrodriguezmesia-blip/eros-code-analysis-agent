import os
os.environ["AZURE_IDENTITY_DISABLE_IMDS"] = "1"

import json
from azure.ai.agentserver.responses import ResponsesAgentServerHost, TextResponse, ResponseContext
import inspect

# Create server
server = ResponsesAgentServerHost()

@server.response_handler
def analyze_code(request, context, cancellation_signal):
    return TextResponse(context=context, request=request, text='{"test": "ok"}')

# Check signature
sig = inspect.signature(server._create_fn)
print(f"Handler signature: {sig}")

# Test TextResponse
class MockRequest:
    pass

class MockContext:
    response_id = "test-id"

result = TextResponse(context=MockContext(), request=MockRequest(), text='{"test": "ok"}')
print(f"TextResponse result: {result}")