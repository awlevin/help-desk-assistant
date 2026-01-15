from uuid import UUID

from vellum_ee.workflows.display.base import (
    EdgeDisplay,
    EntrypointDisplay,
    StateValueDisplay,
    WorkflowDisplayData,
    WorkflowDisplayDataViewport,
    WorkflowMetaDisplay,
    WorkflowOutputDisplay,
)
from vellum_ee.workflows.display.workflows import BaseWorkflowDisplay

from ..nodes.prompt import Prompt
from ..state import State
from ..workflow import Workflow


class WorkflowDisplay(BaseWorkflowDisplay[Workflow]):
    workflow_display = WorkflowMetaDisplay(
        display_data=WorkflowDisplayData(
            viewport=WorkflowDisplayDataViewport(x=4.536631882411598, y=-68.71085625869529, zoom=1.008992009780227)
        )
    )
    state_value_displays = {
        State.chat_history: StateValueDisplay(
            id=UUID("0c1582e0-248d-4bec-871f-500bb64af47f"), name="chat_history", color="purple"
        ),
    }
    entrypoint_displays = {
        Prompt: EntrypointDisplay(
            id=UUID("3af460ea-5a6e-4599-a3d0-69ad4eea09ac"),
            edge_display=EdgeDisplay(id=UUID("877dae0c-0959-49f4-ae20-4b8355553c0b")),
        )
    }
    output_displays = {
        Workflow.Outputs.response: WorkflowOutputDisplay(
            id=UUID("9ceeb933-1d5e-49ea-9227-5600ef988175"), name="response"
        )
    }