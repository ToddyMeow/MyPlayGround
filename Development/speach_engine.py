#import essential packages
import pyttsx3
import datetime

#initialize AI voice engine
speach_engine = pyttsx3.init()
voice_opts = speach_engine.getProperty('voices')
voice_spead = 200
speach_engine.setProperty('rate', voice_spead)
speach_engine.setProperty('voice', voice_opts[1].id)


class assistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voice_choice = self.engine.getProperty('voices')

        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', self.voice_choice[2].id)

    def speak(self,text):
        """Read out text

        Args:
            text (String): Target text 
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def report_time():
        time = datetime.datetime.now().strftime("%I:%M")
        return "Current time is "+time 
