from vellum.workflows.references import LazyReference
from vellum.workflows.triggers import ChatMessageTrigger


class ChatMessage(ChatMessageTrigger):
    class Config(ChatMessageTrigger.Config):
        output = LazyReference("Workflow.Outputs.response")

    class Display(ChatMessageTrigger.Display):
        label = "Chat Message"
        x = 36.1384111708978
        y = 284.7770885934054
        z_index = 1
        icon = "vellum:icon:archive"