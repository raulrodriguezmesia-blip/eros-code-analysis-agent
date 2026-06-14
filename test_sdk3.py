import os
import json
from typing import Any
import sys
import traceback

from azure.ai.agentserver.responses import ResponsesAgentServerHost, TextResponse, ResponseEventStream

# Test con output_item_message (generator)
def handler(request, context, cancellation_signal):
    print(f"Handler called", file=sys.stderr)
    try:
        stream = ResponseEventStream(response_id=context.response_id)
        yield stream.emit_created()
        yield stream.emit_in_progress()
        yield from stream.output_item_message(text='{"phase": "test"}')
        yield stream.emit_completed()
    except Exception as e:
        print(f"ERROR in handler: {e}", file=sys.stderr)
        traceback.print_exc()
        raise

# Mock context
class Mock:
    response_id = "test-id"

for event in handler(None, Mock(), None):
    print(f"Event: {event}")