# 🎧 Help Desk Assistant

[![Vellum Workflow](https://img.shields.io/badge/Vellum-Workflow-blueviolet)](https://www.vellum.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent help desk assistant workflow built with Vellum that provides automated customer support responses. This AI-powered agent can handle common support queries, provide helpful information, and assist users with their questions in a conversational manner.

## 🌟 Features

- **Conversational AI**: Natural language understanding for customer support queries
- **Automated Responses**: Intelligent prompt-based response generation
- **Chat Interface**: Built-in chat message trigger for seamless conversations
- **Customizable**: Easy to modify and extend for your specific use case

## 📁 Repository Structure

```
help-desk-assistant/
├── nodes/
│   └── prompt.py          # Core prompt node logic for generating responses
├── display/
│   ├── workflow.py        # Workflow visualization and structure
│   └── nodes/
│       └── prompt.py      # Display configuration for prompt nodes
├── triggers/
│   └── chat_message.py    # Chat message trigger configuration
└── README.md              # This file
```

### Key Files Breakdown

- **`nodes/prompt.py`**: Contains the main prompt node implementation that processes user queries and generates appropriate help desk responses using AI.

- **`display/workflow.py`**: Defines the workflow structure and how different nodes connect together. This is the blueprint of your help desk assistant.

- **`display/nodes/prompt.py`**: Configuration for how prompt nodes are displayed and configured in the Vellum UI.

- **`triggers/chat_message.py`**: Defines the chat message trigger that initiates the workflow when a user sends a message.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Vellum API key ([get one here](https://app.vellum.ai))

### Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/awlevin/help-desk-assistant.git
   cd help-desk-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install vellum-ai
   ```

3. **Set your Vellum API key and run**
   ```bash
   VELLUM_API_KEY=your_api_key_here python -m nodes.sandbox
   ```

   Replace `your_api_key_here` with your actual Vellum API key.

## 🎮 Try It Out

Want to see the workflow in action before running it locally? Try the public preview:

**[Launch Public Preview →](https://app.vellum.ai/public/workflow-sandboxes/help-desk-assistant)**

## 🔧 Customization

### Modifying the Prompt

To customize the help desk assistant's behavior, edit the prompt configuration in `nodes/prompt.py`. You can:

- Adjust the system prompt to change the assistant's personality
- Modify response templates
- Add custom logic for specific query types

### Extending the Workflow

You can extend this workflow by:

1. Adding new nodes for specialized support categories
2. Integrating with external APIs (ticketing systems, knowledge bases)
3. Adding conditional logic for routing different types of queries
4. Implementing escalation paths for complex issues

## 🎨 Fork and Build in Vellum UI

Want to customize this workflow visually? You can fork it directly in Vellum:

1. Visit [Vellum](https://app.vellum.ai)
2. Navigate to Workflows
3. Import this workflow using the deployment name: `help-desk-assistant`
4. Use the visual editor to modify nodes, add new functionality, and test changes
5. Deploy your customized version

## 📚 Learn More

- [Vellum Documentation](https://docs.vellum.ai)
- [Workflow Development Guide](https://docs.vellum.ai/workflows)
- [API Reference](https://docs.vellum.ai/api-reference)

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💬 Support

Need help? 

- Check out the [Vellum Community](https://community.vellum.ai)
- Review the [documentation](https://docs.vellum.ai)
- Open an issue in this repository

---

Built with ❤️ using [Vellum](https://www.vellum.ai)