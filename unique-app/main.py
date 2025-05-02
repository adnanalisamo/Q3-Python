import tkinter as tk
from tkinter import messagebox
import requests
import random
import pyperclip

class QuoteFetcher:
    def __init__(self, use_api=True):
        self.use_api = use_api
        self.local_quotes = [
            "Believe you can and you're halfway there.",
            "Dream big and dare to fail.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "The harder you work for something, the greater you'll feel when you achieve it.",
            "Push yourself, because no one else is going to do it for you."
        ]

    def fetch_quote(self):
        if self.use_api:
            try:
                response = requests.get("https://zenquotes.io/api/random")
                data = response.json()
                quote = f"{data[0]['q']} - {data[0]['a']}"
                return quote
            except Exception as e:
                print("API error, loading from local quotes.")
                return random.choice(self.local_quotes)
        else:
            return random.choice(self.local_quotes)


class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Motivational Quote")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")

        self.fetcher = QuoteFetcher(use_api=True)

        self.quote_label = tk.Label(root, text="Click the button to get your quote!", wraplength=500, justify="center", font=("Helvetica", 14), bg="#f0f8ff")
        self.quote_label.pack(pady=50)

        self.get_quote_button = tk.Button(root, text="Get New Quote", command=self.display_quote, bg="#4caf50", fg="white", padx=10, pady=5)
        self.get_quote_button.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy Quote", command=self.copy_quote, bg="#2196f3", fg="white", padx=10, pady=5)
        self.copy_button.pack(pady=10)

    def display_quote(self):
        quote = self.fetcher.fetch_quote()
        self.quote_label.config(text=quote)

    def copy_quote(self):
        current_quote = self.quote_label.cget("text")
        if current_quote:
            pyperclip.copy(current_quote)
            messagebox.showinfo("Copied", "Quote copied to clipboard!")

def main():
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
