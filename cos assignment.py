import tkinter as tk
from tkinter import messagebox, ttk
import time

# Sample dictionaries for different languages
dictionaries = {
    #SULEIMAN BWALA
    "Hausa": {
        "gida": "house",
        "mota": "car",
        "ruwa": "water",
        "abinci": "food",
        "suna": "name",
        "lafiya": "health",
        "kudi": "money",
        "yara": "children",
        "baba": "father",
        "mama": "mother",
        "doki": "horse",
        "gari": "town",
        "baki": "mouth",
        "hanya": "road",
        "kasa": "land",
        "gaskiya": "truth",
        "zuciya": "heart",
        "sako": "message",
        "fata": "skin",
        "hankali": "wisdom"
    },
    #PHILLIP POPOOLA
    "Spanish": {
        "hola": "hello",
        "gracias": "thank you",
        "adiós": "goodbye",
        "sí": "yes",
        "no": "no",
        "por favor": "please",
        "lo siento": "sorry",
        "bien": "good",
        "mal": "bad",
        "amigo": "friend",
        "casa": "house",
        "agua": "water",
        "comida": "food",
        "libro": "book",
        "escuela": "school",
        "profesor": "teacher",
        "estudiante": "student",
        "trabajo": "work",
        "familia": "family",
        "ayuda": "help"
    },
    #FRANK ELUMA
    "French": {
        "bonjour": "hello",
            "merci": "thank you",
            "au revoir": "goodbye",
            "oui": "yes",
            "non": "no",
            "s'il vous plaît": "please",
            "excusez-moi": "excuse me/sorry",
            "bien": "good",
            "mal": "bad",
            "ami": "friend",
            "maison": "house",
            "eau": "water",
            "nourriture": "food",
            "livre": "book",
            "école": "school",
            "professeur": "teacher",
            "étudiant": "student",
            "travail": "work",
            "famille": "family",
            "aide": "help"
    },
    #LOIC ISAAC
    "German": {
        "hallo": "hello",
        "danke": "thank you",
        "auf wiedersehen": "goodbye",
        "ja": "yes",
        "nein": "no",
        "bitte": "please",
        "entschuldigung": "excuse me/sorry",
        "gut": "good",
        "schlecht": "bad",
        "freund": "friend",
        "haus": "house",
        "wasser": "water",
        "essen": "food",
        "buch": "book",
        "schule": "school",
        "lehrer": "teacher",
        "schüler": "student",
        "arbeit": "work",
        "familie": "family",
        "hilfe": "help"
    },
    #NANA DAVID
    "Swahili": {
        "habari": "hello/news",
        "asante": "thank you",
        "kwaheri": "goodbye",
        "ndiyo": "yes",
        "hapana": "no",
        "tafadhali": "please",
        "pole": "sorry",
        "nzuri": "good",
        "mbaya": "bad",
        "rafiki": "friend",
        "nyumba": "house",
        "maji": "water",
        "chakula": "food",
        "kitabu": "book",
        "shule": "school",
        "mwalimu": "teacher",
        "mwanafunzi": "student",
        "kazi": "work",
        "familia": "family",
        "msaada": "help"
    }
}

def search_word():
    word = entry.get().strip().lower()
    selected_language = language_var.get()
    dictionary = dictionaries[selected_language]
    
    # Simulate loading effect
    loading_label.config(text="oya wait fes...")
    root.update()
    time.sleep(1)  # Simulate a delay for loading

    meaning = dictionary.get(word)
    loading_label.config(text="")
    
    if meaning:
        messagebox.showinfo("Meaning", f"The meaning of '{word}' in {selected_language} is: {meaning}")
    else:
        messagebox.showwarning("Not Found", f"'{word}' not found in the {selected_language} dictionary.")

# Create the main window
root = tk.Tk()
root.title("Multi-Language Dictionary")
root.geometry("1000x1500")
root.configure(bg='grey')

# Create a label for language selection
language_var = tk.StringVar(value="Hausa")
language_label = tk.Label(root, text="Select Language:", bg='black', fg='white')
language_label.pack(pady=10)

# Create a dropdown for language selection
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=list(dictionaries.keys()))
language_dropdown.pack(pady=10)

# Create a label for word entry
label = tk.Label(root, text="Enter word:", bg='black', fg='white')
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a loading label
loading_label = tk.Label(root, text="", bg='black', fg='white')
loading_label.pack(pady=10)

# Create a search button
search_button = tk.Button(root, text="Search", command=search_word, bg='gray', fg='white')
search_button.pack(pady=20)

# Run the application
root.mainloop()
#"Por favor": "Please",
