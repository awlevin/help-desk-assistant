# 🎧 Help Desk Assistant

[![Vellum](https://img.shields.io/badge/Built%20with-Vellum-blue)](https://www.vellum.ai)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent help desk assistant workflow built with Vellum that provides automated customer support responses. This AI-powered agent can handle common support queries, provide helpful information, and assist users with their questions in a conversational manner.

## 🚀 What This Workflow Does

The Help Desk Assistant is designed to:
- Respond to customer support inquiries in real-time
- Provide accurate and helpful information
- Handle multiple types of support requests
- Maintain a professional and friendly tone
- Scale customer support operations efficiently

## 📁 Key Files Breakdown

### `workflow.py`
The main workflow orchestration file that defines the execution flow of the help desk assistant. This file contains the core logic that coordinates between different nodes and manages the conversation flow.

### `nodes/`
Contains individual node implementations that make up the workflow:
- **`prompt.py`**: Defines the AI prompt node that generates responses to customer queries
- **`chat_message.py`**: Handles incoming chat messages and triggers the workflow

### `inputs.py`
Defines the input schema for the workflow, specifying what data the help desk assistant expects to receive (e.g., user messages, context, metadata).

### `sandbox.py`
A local testing environment that allows you to run and test the workflow on your machine before deploying it to production.

## 💻 How to Run Locally

1. **Clone this repository**
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

   Replace `your_api_key_here` with your actual Vellum API key, which you can find in your [Vellum account settings](https://app.vellum.ai/api-keys).

## 🌐 Try It Online

Want to see the Help Desk Assistant in action without setting anything up? Try the public preview:

**[Launch Interactive Demo →](https://app.vellum.ai/public/workflow-sandboxes/help-desk-assistant)**

## 🔧 Fork and Customize in Vellum

You can fork this workflow and customize it in the Vellum UI:

1. **Open in Vellum**: Visit the [Vellum Workflows](https://app.vellum.ai/workflows) page
2. **Import this workflow**: Use the workflow deployment name `help-desk-assistant`
3. **Customize**: Modify prompts, add new nodes, adjust the conversation flow
4. **Test**: Use the built-in sandbox to test your changes
5. **Deploy**: Push your customized version to production

### Customization Ideas
- Add knowledge base integration for company-specific information
- Implement ticket creation for complex issues
- Add sentiment analysis to prioritize urgent requests
- Integrate with CRM systems
- Add multi-language support
- Implement escalation logic for human handoff

## 📚 Learn More

- [Vellum Documentation](https://docs.vellum.ai)
- [Vellum Workflows Guide](https://docs.vellum.ai/workflows)
- [API Reference](https://docs.vellum.ai/api-reference)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share your customizations

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ using [Vellum](https://www.vellum.ai)** - The AI product development platform for building production-ready AI applications.