import gtts

 synthesize(text, lang, filename):
    tts = gtts.gTTS(text=text,lang=lang)
    tts.save(filename)