# 🧠 AI Doc Bot – Medical Chatbot with Voice & Vision Capabilities

**AI Doc Bot** is a multimodal medical chatbot designed to assist in basic health consultations.  
It can **see**, **listen**, and **speak** — combining **vision**, **voice**, and **language understanding** through advanced AI models.

---

## 🚀 Features

- 🩺 **Multimodal AI** – Understands text, images (like medical scans), and voice inputs.
- 🗣️ **Voice Interaction** – Patients can talk naturally; the bot listens and responds in voice.
- 👁️ **Vision Capabilities** – Uses vision models to analyze medical images.
- 💬 **Interactive UI** – Built with **Gradio** for a seamless chat interface.
- ⚙️ **Modular Architecture** – Clear separation between AI, voice, and UI components.

---

## 🧩 Project Architecture

### **Phase 1 – Brain of the Doctor**
- Configure **GROQ API** for AI inference.
- Preprocess medical images for vision model input.
- Integrate **Multimodal LLM** (e.g., LLaMA 3 Vision).

### **Phase 2 – Voice of the Patient**
- Use **FFmpeg** and **PortAudio** for audio recording.
- Implement **Speech-to-Text (STT)** with **OpenAI Whisper**.

### **Phase 3 – Voice of the Doctor**
- Use **Text-to-Speech (TTS)** engines like **gTTS** and **ElevenLabs**.
- Convert text replies from the AI into spoken responses.

### **Phase 4 – User Interface**
- Create an easy-to-use **VoiceBot UI** using **Gradio**.

---

## 🧰 Tools & Technologies

| Category | Technology |
|-----------|-------------|
| **AI Inference** | GROQ |
| **Vision Model** | LLaMA 3 Vision (Meta) |
| **Speech-to-Text** | OpenAI Whisper |
| **Text-to-Speech** | gTTS, ElevenLabs |
| **UI Framework** | Gradio |
| **Language** | Python |
| **IDE** | VS Code |

---

## 🧱 System Workflow

```
Patient Voice/Image
        ↓
 [STT – Whisper]
        ↓
 [Multimodal LLM – LLaMA 3 Vision via GROQ]
        ↓
 [TTS – gTTS / ElevenLabs]
        ↓
Doctor’s Voice Response
```

---

## 💡 Future Enhancements

- Integrate **paid LLMs** for advanced reasoning.
- **Fine-tune vision models** using real medical datasets.
- Add **multilingual support** for wider reach.
- Include **medical report summarization** and **diagnostic support**.

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashwin007-ai/AI_Doc_Bot-voice_vision.git
   cd AI_Doc_Bot-voice_vision
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # (Linux/macOS)
   venv\Scripts\activate       # (Windows)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API keys**
   ```bash
   export GROQ_API_KEY=your_key_here
   ```

5. **Run the application**
   ```bash
   python gradio_app.py
   ```

Open the local Gradio link displayed in your terminal to interact with the AI Doc Bot.

---

## 🧪 Example Use Case

1. Speak or upload an image describing your symptoms.  
2. The AI processes your input using **Whisper + LLaMA 3 Vision**.  
3. The AI Doctor responds with a **voice reply** generated using **gTTS / ElevenLabs**.

---

## 👨‍💻 Project Info

- **Project Name:** AI Doc Bot  
- **Created By:** P Ashwin Kumar  
- **Core Technologies:** Python, Whisper, LLaMA 3 Vision, GROQ, Gradio, ElevenLabs  

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it for learning or research purposes.

---

> 💬 *“AI Doc Bot – Bringing human-like intelligence to healthcare through voice and vision.”*
