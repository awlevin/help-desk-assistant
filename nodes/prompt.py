from vellum import (
    ChatMessagePromptBlock,
    PlainTextPromptBlock,
    PromptParameters,
    PromptSettings,
    RichTextPromptBlock,
    VariablePromptBlock,
)
from vellum.workflows.nodes.displayable import InlinePromptNode
from vellum.workflows.types.core import MergeBehavior

from ..state import State


class Prompt(InlinePromptNode[State]):
    ml_model = "claude-sonnet-4-5-20250929"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[RichTextPromptBlock(blocks=[PlainTextPromptBlock(text="""Answer this in 2 lines only """)])],
        ),
        VariablePromptBlock(input_variable="chat_history"),
    ]
    prompt_inputs = {
        "chat_history": State.chat_history,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=0,
        max_tokens=64000,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,
        logit_bias=None,
        custom_parameters={
            "expanded_1m_context": False,
        },
    )
    settings = PromptSettings(stream_enabled=True)

    class Trigger(InlinePromptNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES