# 💬 CommentiFy — YouTube Comment Summarizer (LLM-Powered)

A quick tool to extract comments from any YouTube video and summarize them using an LLM (like ChatGPT or Mistral via Ollama).

Built during a late-night coding spree with zero UI, zero testing, and just vibes.

---

## 🧠 What It Does

- Pulls comments from a YouTube video using the YouTube Data API
- Cleans them (sort of)
- Sends them to a language model (e.g., OpenAI, Claude, Ollama)
- Returns a summary of what people are saying in the comment section

---

## 📦 Setup

1. Clone the repo

```bash
git clone https://github.com/yourusername/commentify.git
cd commentify
```

Install dependencies

```bash
pip install google-api-python-client openai
```

Add your API keys

Edit config.py or .env file with:

```python
YOUTUBE_API_KEY = "your_youtube_key_here"
OPENAI_API_KEY = "your_openai_key_here"
```

🚀 Usage

```bash
python main.py --video https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Or pass just the video ID:

```bash
python main.py --video dQw4w9WgXcQ
```

It'll:

Fetch ~100 top comments

Smash them into a single prompt

Ask the LLM: "Summarize what people are saying in this video's comment section."

🧪 Sample Output
"Most viewers loved the nostalgic vibe. A few joked about being rickrolled again. Some praised the editing and the audio quality."

⚠️ Caveats
No retries, no error handling, no rate limiting

No sentiment breakdown yet (coming soon?)

Assumes all comments are in English

Built mainly as a playground project

📌 TODO (If I Ever Touch This Again)
 Clean comment text better

 Add support for sentiment charts

 Use local models like Mistral via Ollama

 Add topic clustering or frequent phrase detection

 Maybe build a Streamlit UI?

🙃 Author Notes
This project is 50% useful, 50% cursed. I just wanted to stop doomscrolling and do something with all that YouTube comment noise.

🧠 License
MIT — because I don't want to be responsible if this becomes Skynet.
