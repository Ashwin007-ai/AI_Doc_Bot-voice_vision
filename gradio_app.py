import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath, progress=gr.Progress()):
    
    if not audio_filepath:
        return "", "⚠️ Please record your voice describing your symptoms.", None
    
    progress(0.3, desc="Transcribing your voice...")
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    progress(0.6, desc="Analyzing medical information...")
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "I've heard your symptoms. However, I don't see any medical images to analyze. Please upload an image for a more complete assessment."

    progress(0.9, desc="Generating voice response...")
    output_audio_path = "final.mp3"
    text_to_speech_with_elevenlabs(
        input_text=doctor_response, 
        output_filepath=output_audio_path
    )

    progress(1.0, desc="Complete!")
    return speech_to_text_output, doctor_response, output_audio_path


def clear_all():
    return None, None, "", "", None


custom_css = """
#main-container {
    max-width: 1200px;
    margin: auto;
}

.header-section {
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
    margin-bottom: 30px;
    color: white;
}

.instruction-box {
    background-color: #f0f7ff;
    border-left: 4px solid #4a90e2;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.warning-box {
    background-color: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 20px;
}

footer {
    text-align: center;
    margin-top: 30px;
    padding: 20px;
    color: #666;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    
    with gr.Row(elem_id="main-container"):
        with gr.Column():
            gr.HTML("""
                <div class="header-section">
                    <h1>🏥 AI Medical Assistant</h1>
                    <p>Voice-Enabled Medical Image Analysis System</p>
                </div>
            """)
    
    with gr.Row(elem_id="main-container"):
        with gr.Column():
            gr.HTML("""
                <div class="instruction-box">
                    <h3>📋 How to Use:</h3>
                    <ol>
                        <li><strong>Record Your Symptoms:</strong> Click the microphone and describe what you're experiencing</li>
                        <li><strong>Upload Medical Image:</strong> Provide any relevant medical images (X-rays, scans, photos)</li>
                        <li><strong>Get Analysis:</strong> Receive AI-powered medical insights with voice response</li>
                    </ol>
                </div>
                <div class="warning-box">
                    <strong>⚠️ Disclaimer:</strong> This is an educational tool only. Always consult a licensed healthcare professional for medical advice.
                </div>
            """)
    
    with gr.Row(elem_id="main-container"):
        with gr.Column(scale=1):
            gr.Markdown("### 🎤 Step 1: Describe Your Symptoms")
            audio_input = gr.Audio(
                sources=["microphone"], 
                type="filepath",
                label="Voice Recording",
                format="wav"
            )
            
        with gr.Column(scale=1):
            gr.Markdown("### 📸 Step 2: Upload Medical Image")
            image_input = gr.Image(
                type="filepath",
                label="Medical Image (Optional)",
                height=300
            )
    
    with gr.Row(elem_id="main-container"):
        with gr.Column():
            analyze_btn = gr.Button("🔍 Analyze", variant="primary", size="lg")
            clear_btn = gr.Button("🗑️ Clear All", variant="secondary", size="lg")
    
    with gr.Row(elem_id="main-container"):
        with gr.Column():
            gr.Markdown("### 📝 Analysis Results")
            
            with gr.Accordion("Your Transcribed Message", open=True):
                transcription_output = gr.Textbox(
                    label="What you said",
                    placeholder="Your voice will be transcribed here...",
                    lines=3,
                    interactive=False
                )
            
            with gr.Accordion("Doctor's Assessment", open=True):
                doctor_response_output = gr.Textbox(
                    label="Medical Analysis",
                    placeholder="AI analysis will appear here...",
                    lines=5,
                    interactive=False
                )
            
            with gr.Accordion("Voice Response", open=True):
                audio_output = gr.Audio(
                    label="Listen to Doctor's Response",
                    autoplay=True
                )
    
    with gr.Row(elem_id="main-container"):
        with gr.Column():
            gr.HTML("""
                <footer>
                    <p>Powered by AI | Groq Whisper + Llama Vision + ElevenLabs TTS</p>
                    <p style="font-size: 12px; color: #999;">
                        This tool is for educational purposes only and should not replace professional medical advice.
                    </p>
                </footer>
            """)
    
    analyze_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[transcription_output, doctor_response_output, audio_output]
    )
    
    clear_btn.click(
        fn=clear_all,
        inputs=[],
        outputs=[audio_input, image_input, transcription_output, doctor_response_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch(debug=True, share=False)