def hitung_kata(teks):
    words = teks.split()
    words = [word for word in words if word.lower() != "the"]
    return len(words)