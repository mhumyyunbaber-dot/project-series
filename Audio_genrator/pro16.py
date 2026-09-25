from gtts import gTTS
# text=("Hello i am Humayun student of Artificial Intelligence and Machine learning and i am learning python programming Language")
# text=("ہیلو میں ہمایوں ہوں، مصنوعی ذہانت اور مشین لرننگ کا طالب علم ہوں اور میں پائتھن پروگرامنگ زبان سیکھ رہا ہوں۔")
text=("benchode main chiz to tu ne pouchi nahi  ")
tts=gTTS(text=text,lang="ur")
tts.save("hello.mp3")
print("Audio file is genrated and saved as hello.mp3")