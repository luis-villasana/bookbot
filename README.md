# 📖 BookBot

A command-line Python tool that reads a text file of a book, analyzes it, and prints a report containing the word count and character frequency.

---

## 🚀 Features

- 📚 Reads the full text from a `.txt` file
- 🔢 Counts total number of words
- 🔤 Calculates how many times each letter appears (case-insensitive)
- 📊 Outputs a sorted frequency table (most used → least used)
- 🧪 Simple and easy-to-read code, perfect for learning Python fundamentals

---

## 🛠️ Usage

### 📦 Installation

Clone the repository:
```bash
git clone https://github.com/your-username/bookbot.git
cd bookbot
```

Run BookBot on a `.txt` file:
```bash
python3 main.py books/frankenstein.txt
```

Expected output:
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 74813 total words
--------- Character Count -------
e: 42563
t: 31697
a: 25541
...
============= END ===============
```

---

## 🧠 How It Works

BookBot is split into two files:

### `main.py`
- Handles file input, orchestrates the analysis, and prints the final report.

### `stats.py`
- `get_num_words(text)`: Returns number of words in the text.
- `get_character_count(text)`: Builds a dictionary of character frequencies (case-insensitive).
- `get_sorted_list(dict)`: Filters to letters only, sorts character frequency from highest to lowest.

---

## 🧪 Example Book Files

You can test it using classic books from [Project Gutenberg](https://www.gutenberg.org/):
- `frankenstein.txt`
- `alice_in_wonderland.txt`
- `moby_dick.txt`

Make sure to save them in a `books/` directory (or modify the path when running the command).

---

## 📂 Project Structure

```
bookbot/
├── books/
│   └── frankenstein.txt
├── main.py
├── stats.py
└── README.md
```

---

## 💡 Learning Goals

✅ File I/O  
✅ Command-line arguments  
✅ Dictionary manipulation  
✅ List sorting with custom keys  
✅ Code modularity and separation of concerns  

---

## 🤝 Contributing

BookBot is part of a learning journey — contributions, suggestions, and improvements are welcome!

Feel free to fork the repo, create a new branch, and open a pull request.

---

## 🧠 Author

Built by Luis Villasana (https://github.com/luis-villasana) while learning backend development at [Boot.dev](https://boot.dev).

---