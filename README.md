# 🎧 Help Desk Assistant

[![Vellum Workflow](https://img.shields.io/badge/Vellum-Workflow-blueviolet)](https://www.vellum.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent help desk assistant workflow built with Vellum that provides automated customer support responses.

## 🌟 Overview

This workflow implements a help desk assistant that can handle customer inquiries, provide support responses, and streamline customer service operations. It leverages AI to understand customer questions and generate helpful, contextual responses.

## 📁 Project Structure

```
help-desk-assistant/
├── nodes/
│   ├── nodes/
│   │   └── prompt.py          # Core prompt node for generating responses
│   ├── display/
│   │   ├── workflow.py        # Workflow orchestration and display logic
│   │   └── nodes/
│   │       └── prompt.py      # Display configuration for prompt node
│   └── triggers/
│       └── chat_message.py    # Chat message trigger handler
```

### Key Files

- **`nodes/nodes/prompt.py`**: Contains the main prompt logic that processes customer inquiries and generates appropriate responses
- **`nodes/display/workflow.py`**: Defines the workflow structure, node connections, and overall execution flow
- **`nodes/triggers/chat_message.py`**: Handles incoming chat messages that trigger the workflow
- **`nodes/display/nodes/prompt.py`**: Configuration for how the prompt node is displayed in the Vellum UI

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Vellum API key ([get one here](https://app.vellum.ai))

### Running Locally

1. Clone this repository:
```bash
git clone https://github.com/awlevin/help-desk-assistant.git
cd help-desk-assistant
```

2. Install dependencies:
```bash
pip install vellum-ai
```

3. Run the workflow sandbox:
```bash
VELLUM_API_KEY=your_api_key_here python -m nodes.sandbox
```

Replace `your_api_key_here` with your actual Vellum API key.

## 🔗 Try It Online

Experience the workflow in action with our public preview:

**[Launch Help Desk Assistant →](https://app.vellum.ai/public/workflow-sandboxes/help-desk-assistant)**

## 🛠️ Customize in Vellum

Want to modify this workflow for your specific use case?

1. **Fork the workflow**: Visit the [Vellum app](https://app.vellum.ai) and import this workflow
2. **Customize nodes**: Adjust prompts, add new nodes, or modify the logic flow
3. **Test changes**: Use the built-in sandbox to test your modifications
4. **Deploy**: Deploy your customized version with one click

### Building in Vellum UI

1. Log in to [Vellum](https://app.vellum.ai)
2. Navigate to Workflows
3. Click "Import Workflow" and select this repository
4. Use the visual editor to:
   - Modify prompt templates
   - Add conditional logic
   - Integrate with external APIs
   - Configure response formatting
   - Add knowledge bases or document search

## 💡 Use Cases

- **Customer Support**: Automate responses to common customer inquiries
- **Technical Support**: Provide troubleshooting guidance and solutions
- **FAQ Automation**: Answer frequently asked questions instantly
- **Ticket Triage**: Categorize and route support tickets efficiently
- **24/7 Availability**: Offer round-the-clock support without human intervention

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [Vellum Documentation](https://docs.vellum.ai)
- [Vellum API Reference](https://docs.vellum.ai/api-reference)
- [Community Discord](https://discord.gg/vellum)

---

Built with ❤️ using [Vellum](https://www.vellum.ai)