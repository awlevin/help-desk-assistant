from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.prompt import Prompt


class PromptDisplay(BaseInlinePromptNodeDisplay[Prompt]):
    node_id = UUID("41b98b2a-2078-480e-8d90-35ba061c2a2e")
    output_id = UUID("21b2c9e9-17c6-4dc2-99bd-024423caa04e")
    array_output_id = UUID("0f8be032-200c-4eb1-b69a-cc6dd2bf3600")
    target_handle_id = UUID("acc733b5-4d01-4a6a-aa29-2f609c2febcf")
    node_input_ids_by_name = {"prompt_inputs.chat_history": UUID("a36e6ee1-88da-4f0b-bb88-bbe7e61d1df2")}
    attribute_ids_by_name = {"ml_model": UUID("ae92ff5d-5792-4588-b3b3-97e31c22a174")}
    output_display = {
        Prompt.Outputs.text: NodeOutputDisplay(id=UUID("21b2c9e9-17c6-4dc2-99bd-024423caa04e"), name="text"),
        Prompt.Outputs.results: NodeOutputDisplay(id=UUID("0f8be032-200c-4eb1-b69a-cc6dd2bf3600"), name="results"),
        Prompt.Outputs.json: NodeOutputDisplay(id=UUID("439ae650-7ed6-4e9b-b93a-38a6a3a68f19"), name="json"),
    }
    port_displays = {Prompt.Ports.default: PortDisplayOverrides(id=UUID("852c3d39-dda3-4462-b6bc-f4f110de70bd"))}
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=460, y=275.8125),
        z_index=3,
        width=370,
        height=92,
        icon="vellum:icon:text-size",
        color="navy",
    )