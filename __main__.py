import tkinter as tk
from tkinter import ttk, messagebox
from client import Translator, LANGUAGES

# Initialize the main window
root = tk.Tk()
root.title("Google Translate Clone")
root.geometry("850x450")
root.configure(bg='white')

# Colors and fonts to mimic Google's interface
primary_color = "#4285F4"  # Google's blue
button_color = "#34A853"  # Google's green button color
background_color = "white"
text_font = ("Arial", 12)
header_font = ("Arial", 14, "bold")

# Initialize the Google Translate API translator
translator = Translator()

# Language options (from googletrans LANGUAGES)
languages = {name.capitalize(): lang for lang, name in LANGUAGES.items()}

# Frame for layout
top_frame = tk.Frame(root, bg=background_color, pady=10)
top_frame.pack(side=tk.TOP, fill=tk.X)

# Language selection
source_lang_label = tk.Label(top_frame, text="From:", bg=background_color, font=header_font, fg=primary_color)
source_lang_label.pack(side=tk.LEFT, padx=10)

source_lang = ttk.Combobox(top_frame, values=list(languages.keys()), font=text_font, state="readonly")
source_lang.set("English")
source_lang.pack(side=tk.LEFT, padx=5)

target_lang_label = tk.Label(top_frame, text="To:", bg=background_color, font=header_font, fg=primary_color)
target_lang_label.pack(side=tk.LEFT, padx=20)

target_lang = ttk.Combobox(top_frame, values=list(languages.keys()), font=text_font, state="readonly")
target_lang.set("Spanish")
target_lang.pack(side=tk.LEFT, padx=5)

# Adding border and shadow-like effect to the input and output fields
def apply_widget_style(widget):
    widget.config(bd=2, relief="solid", highlightbackground="#e0e0e0", highlightthickness=1)

# Input text field
input_text = tk.Text(root, height=8, width=70, font=text_font, wrap="word")
apply_widget_style(input_text)
input_text.pack(pady=10)

# Output text field (with disabled state initially)
output_text = tk.Text(root, height=8, width=70, font=text_font, wrap="word", state=tk.DISABLED)
apply_widget_style(output_text)
output_text.pack(pady=10)

# Translate button with hover effect
def on_enter(e):
    translate_button['background'] = "#2c8a3e"

def on_leave(e):
    translate_button['background'] = button_color

# Translate button functionality
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text to translate.")
        return

    # Get selected languages
    source_language = languages.get(source_lang.get())
    target_language = languages.get(target_lang.get())

    try:
        # Perform the translation using googletrans
        translated_text = translator.translate(text, src=source_language, dest=target_language).text
        
        # Display the translation
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Clear Button functionality
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

# Translate and Clear buttons with styling
button_frame = tk.Frame(root, bg=background_color)
button_frame.pack(pady=15)

translate_button = tk.Button(button_frame, text="Translate", bg=button_color, fg="white", font=("Arial", 14), command=translate_text)
translate_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", bg=primary_color, fg="white", font=("Arial", 14), command=clear_text)
clear_button.pack(side=tk.LEFT, padx=10)

# Adding hover effects to the Translate button
translate_button.bind("<Enter>", on_enter)
translate_button.bind("<Leave>", on_leave)

# Run the application
root.mainloop()
