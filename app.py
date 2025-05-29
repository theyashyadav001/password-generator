# app.py
import random
import string
import gradio as gr

def generate_password(length, uppercase, lowercase, digits, special_chars):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        return "⚠️ Select at least one option."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

iface = gr.Interface(
    fn=generate_password,
    inputs=[
        gr.Slider(6, 50, value=12, label="Password Length"),
        gr.Checkbox(label="Include Uppercase"),
        gr.Checkbox(label="Include Lowercase"),
        gr.Checkbox(label="Include Digits"),
        gr.Checkbox(label="Include Special Characters"),
    ],
    outputs="text",
    title="🔐 Password Generator",
    description="Generate strong passwords with options for letters, numbers, and symbols."
)

iface.launch()
>
