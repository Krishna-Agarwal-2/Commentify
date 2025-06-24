# 💬 CommentiFy — YouTube Comment Analyzer (LLM + Sentiment)

A quick tool to extract comments from any YouTube video and summarize them using an LLM (like ChatGPT or Mistral via Ollama), **with sentiment analysis**.

Built during a late-night coding spree with zero UI, zero testing, and just vibes.

---

## 🧠 What It Does

- 📥 Pulls comments from a YouTube video using the YouTube Data API  
- 🧹 Cleans and preprocesses the text (sort of)  
- 🧠 Summarizes them using an LLM (OpenAI / Claude / Ollama)  
- 😊 Classifies each comment as **Positive**, **Neutral**, or **Negative**  
- 📊 Outputs a sentiment breakdown and overall summary  

---

## 📦 Setup

1. Clone the repo

```bash
git clone https://github.com/yourusername/commentify.git
cd commentify
```

2. Install dependencies

```bash
pip install google-api-python-client openai
```

3. Add your API keys

Edit `config.py` or create a `.env` file:

```python
YOUTUBE_API_KEY = "your_youtube_key_here"
OPENAI_API_KEY = "your_openai_key_here"
```

---

## 🚀 Usage

Pass a YouTube video URL or ID:

```bash
python main.py --video https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Or just the video ID:

```bash
python main.py --video dQw4w9WgXcQ
```

It will:
- Fetch ~100 top comments  
- Run them through a basic sentiment classifier  
- Send them to the LLM for summarization  
- Print a summary + sentiment breakdown  

---

## 🧪 Sample Output

```text
=== Summary ===
Most users love the music and visuals. A few joke about the unexpected twist. Some comments express nostalgia and appreciation for the creator's editing style.

=== Sentiment Breakdown ===
👍 Positive: 72%
😐 Neutral: 20%
👎 Negative: 8%
```

---

## ⚠️ Caveats

- No retries, no error handling, no rate limiting  
- Sentiment is basic rule/LLM-based, not deep ML  
- Assumes all comments are in English  
- Built mainly as a playground project  

---

## 📌 TODO (If I Ever Touch This Again)

- [ ] Clean comment text better  
- [ ] Use local models like Mistral via Ollama  
- [ ] Add topic clustering or keyword extraction  
- [ ] Build a simple Streamlit UI  
- [ ] Add charts (matplotlib or Plotly)  

---

## 🙃 Author Notes

This project is 50% useful, 50% cursed. I just wanted to stop doomscrolling and do something with all that YouTube comment noise.

---

## 🧠 License

MIT — because I don't want to be responsible if this becomes Skynet.
