# AI Podcast Generator

This script generates an AI-powered podcast based on a give text.
It transforms a conversation between two AI personalities into a fully synthesized audio file. You can customize the speakers, language, and voices for your podcast.

  
## Requirements
Before running the script, make sure you have the following installed/configured:

- Python 3.8 or higher
- [Hugging Face account](https://huggingface.co/) to generate the conversational dialogues
- [EdgeTTS](https://pypi.org/project/edge-tts/) to generate the Text to speech
- [Pydub](https://pypi.org/project/pydub/) to make the final output mp3

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
Customization

#### Change Speakers and Language
You can customize the speakers and their voices by modifying the following variables in the script:

```spe
aker1 = "Ava"  # Change to your preferred speaker name
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


### Notes
Make sure you are logged into Hugging Face and have the proper credentials for API access.
If you encounter any issues with model overload, wait and try again later.
