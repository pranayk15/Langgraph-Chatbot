#🧠 AI Chatbot with LangGraph, Streamlit, SQLite and LangSmith

A fully functional ChatGPT-style conversational AI built using LangGraph, LangChain, Streamlit, SQLite, and LangSmith.
This chatbot can answer general queries, persist conversation history across sessions, and intelligently use integrated tools to perform real-world tasks.

🚀 Features
✅ 1. ChatGPT-like Conversational Agent

Built using LangGraph

Retains the full conversational context

Responds to all queries naturally and accurately

✅ 2. Persistent Chat History (SQLite Database)

Every user message + AI response is stored in SQLite

Even after refreshing the Streamlit page, the history is automatically reloaded

Clean, reliable long-term memory for conversation sessions

✅ 3. Tool-Augmented AI

The chatbot is enhanced with three powerful tools:

🔎 DuckDuckGo Search Tool

Searches the internet in real-time and fetches fresh information.

🧮 Calculator Tool

Evaluates mathematical expressions and solves calculations instantly.

📈 Stock Price Tool (Alpha Vantage)

Fetches real-time stock prices using the Alpha Vantage API.

✅ 4. LangSmith Integration

Complete observability for LangChain / LangGraph pipelines

Trace runs, debug agent reasoning, and monitor tool usage

Helps improve and scale the chatbot efficiently

✅ 5. Clean Streamlit UI

Simple and modern interface

Conversation UI similar to ChatGPT

Auto-scroll, message bubbles, and history view

🏗 Tech Stack
| Component     | Technology Used                                      |
| ------------- | ---------------------------------------------------- |
| Frontend / UI | **Streamlit**                                        |
| AI Framework  | **LangGraph + LangChain**                            |
| Database      | **SQLite**                                           |
| Observability | **LangSmith**                                        |
| Search Tool   | **DuckDuckGo Search**                                |
| Stock API     | **Alpha Vantage**                                    |
| LLM Backend   | Your preferred provider (OpenAI, Google, Groq, etc.) |

🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables

Create a .env file:

LANGSMITH_API_KEY=your_langsmith_key
OPENAI_API_KEY=your_model_key
ALPHAVANTAGE_API_KEY=your_alpha_vantage_key

5. Run the app
streamlit run app.py

🔗 How It Works
🧩 LangGraph Agent Flow

The agent follows this workflow:

Your message enters the LangGraph state machine

The chatbot checks if the query needs tools

If yes, it calls the appropriate tool (search, calculator, stocks)

The tool result is merged back into the AI reasoning

Final answer is generated

Conversation is saved to SQLite

UI updates with the new response

🗂 SQLite Memory

Every message is inserted into a conversations table.
When Streamlit reloads, the chat history is fetched from the database and rendered instantly.

📊 LangSmith Tracing

All agent steps, errors, tool usage and model responses appear in LangSmith dashboard for debugging and performance insights.

🖥️ UI Features

Chat interface with user + AI bubbles

Scrollable conversation window

Auto-reload of saved history

Clean sidebar for settings (optional)

Responsive and smooth experience

🔮 Possible Future Improvements

User authentication

Multi-chat sessions

Custom user-defined tools

File upload and processing

Voice input/output

Vector database for long-term memory

🤝 Contributing

Pull requests are welcome!
If you'd like to contribute, feel free to open an issue or submit a PR.

📜 License

This project is released under the MIT License.
