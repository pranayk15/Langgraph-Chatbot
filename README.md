# 🧠 AI Chatbot using LangGraph, Streamlit, SQLite and LangSmith

This project is a fully functional AI chatbot built using **LangGraph**, **LangChain**, **Streamlit**, and **SQLite**, with **LangSmith** for observability.  
It behaves like a mini-ChatGPT, supports persistent chat history, uses multiple tools to enhance responses, and provides a clean UI for seamless interaction.

---

## ✅ Key Features

### 1. Conversational AI (LangGraph)
- Multi-turn conversational agent built using LangGraph’s state machine architecture  
- Smooth, contextual responses similar to ChatGPT  
- Handles tool calls intelligently based on user queries  

### 2. Persistent Chat Memory (SQLite)
- All chats are stored in a local SQLite database  
- Refreshing the Streamlit page does NOT erase history  
- Clean and reliable message logging  

### 3. Built-in Tools for Smarter Responses
The chatbot comes with three powerful tools:

#### 🔎 DuckDuckGo Search Tool  
Fetches fresh real-time information from the web.

#### 🧮 Calculator Tool  
Solves math expressions accurately and instantly.

#### 📈 Stock Price Tool (Alpha Vantage)  
Retrieves real-time stock values using Alpha Vantage API.

### 4. LangSmith Integration
- Complete observability of the agent workflow  
- View traces, prompts, tool calls, timings, and errors  
- Essential for debugging and improving the agent  

### 5. Modern Streamlit UI
- ChatGPT-like interface  
- Scrollable conversation panel  
- Auto-loaded chat history  
- Responsive and clean presentation  

---

## 🛠 Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| AI Orchestration | LangGraph + LangChain |
| Database | SQLite |
| Observability | LangSmith |
| External Tools | DuckDuckGo Search, Alpha Vantage API |
| LLM Provider | OpenAI / Groq / Google etc. |

---


---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # macOS / Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add environment variables
Create a .env file:
```bash
OPENAI_API_KEY=your_key
LANGSMITH_API_KEY=your_key
ALPHAVANTAGE_API_KEY=your_key
```

### 5. Run the Streamlit app
```bash
streamlit run app.py
```

### 🔧 How It Works Internally
# 🧩 LangGraph Workflow

-Each user message goes into the LangGraph state
-The agent decides whether to use a tool
-Tool results feed back into the model
-Final response is generated and shown in UI

# 🗂 SQLite Message Storage

-Every interaction is inserted into a conversations table
-On app launch, chat history is loaded from the database
-Works seamlessly even after refresh or restart

# 📊 LangSmith Observability

-All agent runs, traces, and tool calls visible in dashboard
-Helps debug slow steps, errors, and reasoning issues

### 🔮 Future Improvements

-Multi-chat session management
-File upload and file-processing tools
-User authentication
-Voice input and TTS responses
-Vector DB long-term memory

### 🤝 Contributing

-Contributions are welcome.
-Feel free to open issues or submit pull requests to improve the chatbot.

### 📜 License

This project is licensed under the MIT License.
