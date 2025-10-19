# Send-reversed-messages

This simple Python program reads multi-line text input from the user and prints each line reversed, while preserving the original line order. 

---
## 🤣 Usefulness
I sometimes write reversed messages to friends just to tease them. This tool makes the prank much easier. 
Usually, my friends reply with a reversed message too, and I can use this tool to convert their replies back.


## 🔧 Features

- Reads multi-line input from `stdin`
- Reverses characters in each line individually
- Maintains the original paragraph and line order
- Supports both interactive and piped input


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


## 🧠 Example

**Input file**
```
Hi Friend,

I hope you’re enjoying the beautiful autumn colors!
I’ve been learning Python and developing some fun little tools—one of them actually wrote this email for me!
How do you like it?
Hopefully I’ll have more progress to share soon. I’d love to see you sometime later this year.

Best,
SpaceCharging
```

**Command**
```bash
$ python reverse_lines.py < lines.txt
```

**Output**
```
,dneirF iH

!sroloc nmutua lufituaeb eht gniyojne er’uoy epoh I
!em rof liame siht etorw yllautca meht fo eno—sloot elttil nuf emos gnipoleved dna nohtyP gninrael neeb ev’I
?ti ekil uoy od woH
.raey siht retal emitemos uoy ees ot evol d’I .noos erahs ot ssergorp erom evah ll’I yllufepoH

,tseB
gnigrahCecapS
```

---

## 🪪 License

This project is released under the [MIT License](LICENSE).
