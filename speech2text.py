# import speech_recognition as sr 
# from os import path
# from pydub import AudioSegment

# # convert mp3 file to wav
# # sound = AudioSegment.from_mp3("transcript.mp3")
# # sound.export("transcript.wav", format='wav')

# # transcribe audio file
# AUDIO_FILE = "transcript.wav"

# # use the audio file as the audio source
# r = sr.Recognizer()
# mic = sr.Microphone(device_index=0)

# with mic as source:
#     audio = r.listen(source)

# result = r.recognize_google(audio)
# print(result)

# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)

#     print("Transcription: " + r.recognize_google(audio))

# with open('my_result.txt', mode = 'w') as file:
#     file.write("Recognized text:")
#     file.write("\n")
#     file.write(result)

# print("Exporting process completed!")