import pyttsx
import winsound

class userWarning:

    def turnAlarmOn(self):
        duration = 2000  # millisecond
        freq = 550  # Hz
        winsound.Beep(freq, duration) #MavoiceEngineing Alarm Sound



    def say(self,risvoiceEngineLevel):              #Warn the user by telling What to do
        voiceEngine = pyttsx.init()
        newVoiceRate = 125
        voiceEngine.setProperty('rate', newVoiceRate)
        newVolume=1.3
        voiceEngine.setProperty('volume', newVolume)

        if risvoiceEngineLevel is 0:
            voiceEngine.say("Very Low disease spreading rate is detected during past hours Please take necessary actions before further spreading ")
            voiceEngine.runAndWait()
        elif risvoiceEngineLevel is 1:
            voiceEngine.say("Low disease spreading rate is detected during past hours Please take necessary actions ")
            voiceEngine.runAndWait()
        elif risvoiceEngineLevel is 2:
            voiceEngine.say("High disease spreading rate is detected during past hours Please immediately take necessary actions  ")
            voiceEngine.runAndWait()
        elif risvoiceEngineLevel is 3:
            voiceEngine.say("Very High disease spreading rate is detected during past hours Please immediately take necessary actions ")
            voiceEngine.runAndWait()





