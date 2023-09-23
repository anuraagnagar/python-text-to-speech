import pyttsx3


class TextToSpeechMp3:

    engine: pyttsx3.Engine

    def __init__(self, voice, rate, volume):
        self.engine = pyttsx3.init()
        if not voice:
            self.get_available_voices()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

    def text_to_speech(self, text, save_file=False, file_name="output.mp3"):

        self.engine.say(text)
        print("I'm speaking...")

        if save_file:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()

    def show_available_voices(self):
        voices = [self.engine.getProperty("voices")]
        
        for voice in voices[0]:
            print(f"{voice.name}")
        
    def get_available_voices(self):
        voice = "com.apple.speech.synthesis.voice.daniel"
        self.engine.setProperty("voice", voice)
    
    def run(self):
        text = input("Provide text to convert speech >> ")
        self.show_available_voices()
        self.text_to_speech(text, save=True, file_name="output.mp3")


if __name__ == "__main__":
    tts = TextToSpeechMp3(voice, 200, 1.0)
    tts.run()