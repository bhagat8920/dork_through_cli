# dork_through_cli

---

````
# 🔎 Dork Search Automation

A Python tool to automate **Google Dorking** (or any custom search query) directly into your browser.  
This script reads queries (dorks) from a file and opens them in **Google, DuckDuckGo, Bing, or Yandex** search engines in batches.  

---

## ⚡ Features
- Read dorks from any `.txt` file (one query per line)
- Open results in **Google, DuckDuckGo, Bing, or Yandex**
- Batch mode → open multiple queries at once
- Interactive: Press **Enter** for next batch, **q** to quit
- Customizable batch size

---

## 📦 Requirements
- Python **3.7+**
- Any modern web browser (default system browser is used)

---

## 📂 Installation
Clone or download this repository, then navigate into the folder:

```bash
git clone https://github.com/yourusername/dork-search-automation.git
cd dork-search-automation
````

---

## 📝 Usage

### Basic Example

Run with a dork list:

```
python search_dorks.py -p /usr/share/wordlists/dorks.txt
```

### Choose Search Engine

* Google (default):

  ```
  python search_dorks.py -p dorks.txt -e google
  ```
* DuckDuckGo:

  ```
  python search_dorks.py -p dorks.txt -e duckduckgo
  ```
* Bing:

  ```
  python search_dorks.py -p dorks.txt -e bing
  ```
* Yandex:

  ```
  python search_dorks.py -p dorks.txt -e yandex
  ```

### Change Batch Size

Open **10 queries at a time**:

```
python search_dorks.py -p dorks.txt -b 10
```

---

## 📘 Example `dorks.txt`

```
site:.gov "login"
inurl:admin
"index of" passwords
site:.edu filetype:pdf
site:.org "contact us"
```

---

## 🎮 Interactive Controls

* **Enter** → open next batch of queries
* **q + Enter** → quit the program

---

## ⚠️ Disclaimer

This script is for **educational and research purposes only**.
Do not use it for unauthorized access, scraping, or any activity that violates search engine **Terms of Service**.
The author is not responsible for misuse.

```

---
