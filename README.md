Magic Folder — Local AI File Sorter

Automatically sort and rename your files based on their content using local AI.  
Just drop a file into a folder — the AI will read it, understand what it’s about, and organize it for you. All 100% offline.
This project is built to run entirely offline. Your documents are never sent to the cloud.

![image](https://github.com/user-attachments/assets/99345ff0-0373-43b1-89f1-6fd9c11d85c7)

Setup
1. Clone the repo

```bash
git clone https://github.com/josh5210/magic-folder-public.git
cd magic-folder
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
```

3. Install dependencies
```bash
pip install torch transformers watchdog python-docx PyMuPDF
```

4. Configure Directory Structure in monitoring.py

5. Run the script
```bash
python monitoring.py
```


License: MIT
