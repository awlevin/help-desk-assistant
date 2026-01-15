# 🎧 Help Desk Assistant

[![Vellum](https://img.shields.io/badge/Built%20with-Vellum-blue)](https://www.vellum.ai)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)

An intelligent help desk assistant workflow built with Vellum that provides automated customer support and ticket management capabilities.

## 🌟 Overview

This workflow implements a conversational help desk assistant that can handle customer inquiries, provide support information, and assist with common help desk tasks. The assistant is designed to streamline customer support operations and provide quick, accurate responses to user questions.

## 📁 Project Structure

```
help-desk-assistant/
├── nodes/
│   └── prompt.py          # Core prompt node for the assistant's responses
├── display/
│   ├── workflow.py        # Workflow visualization and display logic
│   └── nodes/
│       └── prompt.py      # Display configuration for prompt nodes
├── triggers/
│   └── chat_message.py    # Chat message trigger configuration
└── README.md
```

### Key Files

- **`nodes/prompt.py`**: Contains the main prompt logic that powers the help desk assistant's conversational capabilities. This defines how the assistant processes and responds to user queries.

- **`display/workflow.py`**: Defines the visual representation and flow of the workflow in the Vellum UI, showing how different nodes connect and interact.

- **`display/nodes/prompt.py`**: Configuration for how prompt nodes are displayed in the workflow editor.

- **`triggers/chat_message.py`**: Defines the chat message trigger that initiates the workflow when users send messages to the assistant.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Vellum API key ([get one here](https://app.vellum.ai/))

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

3. Run the workflow:
```bash
VELLUM_API_KEY=your_api_key_here python -m nodes.sandbox
```

Replace `your_api_key_here` with your actual Vellum API key.

## 🔗 Try It Online

Experience the help desk assistant in action with the public preview:

**[Launch Public Preview](https://app.vellum.ai/public/workflow-sandboxes/help-desk-assistant)**

## 🛠️ Customize in Vellum

Want to modify this workflow for your specific needs?

1. **Fork the workflow**: Visit the [Vellum app](https://app.vellum.ai) and import this workflow
2. **Edit nodes**: Customize prompts, add new nodes, or modify the conversation flow
3. **Test changes**: Use the built-in sandbox to test your modifications
4. **Deploy**: Deploy your customized version with one click

### Customization Ideas

- Adjust the assistant's tone and personality in the prompt nodes
- Add integration nodes to connect with your ticketing system
- Implement custom logic for routing complex queries
- Add knowledge base integration for domain-specific support
- Configure escalation paths for issues requiring human intervention

## 📚 Learn More

- [Vellum Documentation](https://docs.vellum.ai/)
- [Workflow Development Guide](https://docs.vellum.ai/workflows)
- [API Reference](https://docs.vellum.ai/api-reference)

## 🤝 Contributing

This workflow was generated from Vellum. To contribute improvements:

1. Make changes in the Vellum UI
2. Test thoroughly using the sandbox
3. Export and update this repository
4. Share your enhancements with the community

## 📄 License

This workflow is provided as-is for use with the Vellum platform.

---

**Built with ❤️ using [Vellum](https://www.vellum.ai)**