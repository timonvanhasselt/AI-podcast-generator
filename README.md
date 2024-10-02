# AI Podcast Generator

This script generates an AI-powered podcast based on a given text.
It transforms a conversation between two AI personalities into a fully synthesized audio file. You can customize the speakers, language, and voices for your podcast.
Inspired by the audio overview option of Google's [NotebookLM](https://notebooklm.google.com) experiment, and inspired by [AnthusAI/Podcastic](https://github.com/AnthusAI/Podcastic) to make a script of it.

![Animated gif of the script in action](https://github.com/user-attachments/assets/46139154-0a4a-4491-89a4-5ea3984985a3)


  
## Requirements
Before running the script, make sure you have the following installed/configured:

- Python 3.8 or higher
- [Hugging Face account](https://huggingface.co/join) to generate the conversational dialogues; you can see the output in [HuggingChat](https://huggingface.co/chat/)
- [EdgeTTS](https://pypi.org/project/edge-tts/) to generate the Text to speech
- [Pydub](https://pypi.org/project/pydub/) to make the final output mp3
- [Flask](https://pypi.org/project/flask/) to run a webUI around the scriopt for easy creation of the podcast


## Installation

### macOS/Linux

1. **Clone the repository:**
   ```
   git clone https://github.com/timonvanhasselt/AI-podcast-generator.git
   cd ai-podcast-generator
   ```

2. **Create a virtual environment:**
```
python3 -m venv venv
source venv/bin/activate
```

3. **Install the required Python packages:**
`pip install -r requirements.txt`

### Windows
1. **Clone the repository:**
```git clone https://github.com/timonvanhasselt/AI-podcast-generator.git
cd ai-podcast-generator
```
2. **Create a virtual environment:**

```
python -m venv venv
venv\Scripts\activate
```

3. **Install the required Python packages:**

`pip install -r requirements.txt`

### Usage

Update the Hugging Face credentials in the script to your own email and password:
```
EMAIL = "your-email@domain.com"
PASSWD = "your-password"
```

**Prepare your input:** 
The script reads text input from a file named content.txt. 
Create a content.txt file in the project directory and input the text you want to be transformed into dialogue.

**Run the script:** 
Once everything is set up, you can run the script as follows:

**On macOS/Linux:**
`python3 podcast_script.py`

**On Windows:**
`python podcast_script.py`


### Output
The script will generate an SSML conversation between the speakers, convert it into speech, and combine the segments into a final MP3 file named final_output.mp3.

### Customization

**Change Speakers and Language**
You can customize the speakers and their voices by modifying the following variables in the script:

```
speaker1 = "Ava"  # Change to your preferred speaker name
speaker2 = "Andrew"  # Change to your preferred speaker name
lang = "English"  # Change to your preferred language
```

You can also map different voices using EdgeTTS by updating the voice_map dictionary:

```
voice_map = {
    "Ava": "en-US-AvaMultilingualNeural",  # Change to your desired voice from EdgeTTS
    "Andrew": "en-US-AndrewMultilingualNeural"
}
```

### WebUI
Run `app.py` first to open the Flask server for the webUI.
The webUI can be visited by browsing to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

The start button triggers the `podcast_script.py` script via the webUI.
The logs of the script are showed also, to give the user more info about what's happening. 
(Note: Generation of SSML and the Mp3 file takes about 2-3 minutes alltogether, depending on the text length).

The output mp3 will be loaded in the site after processing.


![Animated gif of the web UI in action](https://github.com/user-attachments/assets/1cc1213b-bb50-4967-9f94-634e935a6d29)


### Notes
Make sure you are logged into Hugging Face and have the proper credentials for API access.
If you encounter any issues with model overload, wait and try again later.
