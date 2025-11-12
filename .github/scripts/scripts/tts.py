from gtts import gTTS
tts = gTTS(open("out/script.txt").read(), lang='fa')
tts.save("out/voice.mp3")
print("✅ Voice generated")
