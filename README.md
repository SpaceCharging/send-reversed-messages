# Send-reversed-messages

This simple Python program reads multi-line text input from the user and prints each line reversed, while preserving the original line order. 

---

## 🔧 Features

- Reads multi-line input from `stdin`
- Reverses characters in each line individually
- Maintains the original paragraph and line order
- Supports both interactive and piped input
- No external dependencies

---

## 🚀 Usage

### Interactive mode
```bash
$ python reverse_lines.py
Enter your text, press Ctrl+D when done:
Hello world
Python is fun!
<Ctrl+D>
```

**Output**
```
dlrow olleH
!nuf si nohtyP
```

### From a file
```bash
$ python reverse_lines.py < input.txt
```

### From a pipeline
```bash
$ cat input.txt | python reverse_lines.py
```

---

## 🧩 Implementation Overview

| Function | Description |
|-----------|--------------|
| `intake()` | Reads text from standard input (`sys.stdin.read()`). |
| `rev(txt)` | Reverses a string using `reversed()` and `''.join()`. |
| `rev_paragraph(read_in)` | Splits input into lines, reverses each, and prints the result. |
| `main()` | Entry point — coordinates input and output. |

---

## 📂 Project Structure

```
reverse_lines.py
README.md
```

---

## ⚙️ Requirements

- Python 3.6 or later
- Works cross-platform (Linux, macOS, Windows)

---

## 🧠 Example

**Input file**
```
First line
Second line
Third line
```

**Command**
```bash
$ python reverse_lines.py < lines.txt
```

**Output**
```
enil tsriF
enil dnoceS
enil drihT
```

---

## 🪪 License

This project is released under the [MIT License](LICENSE).
