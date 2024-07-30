import string

word_library = {
    1: ["a", "I", "A", "i", "d", "E", "f", "G", "h", "J", "k", "L", "m", "N", "o", "P", "q", "R", "s", "T", "u", "V", "w", "X", "y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "!", "@", "#", "$", "%", "^", "&", "*", "_a", "-", "_", "=", "+", ":3", ":')", "oi", "ami", "tumi", "o", "ooo", "oh", "omg", "ohoo", "ahha", "naa", "?", "??",
    "~", "`", "A", "B", "D", "F", "H", "K", "M", "O", "Q", "S", "U", "W", "Y", "e", "g", "i", "j", "l", "n", "p", "r", "t", "v", "x", "z", " a", "amii", "tumio", "ki", "keno"],
    2: ["an", "at", "by", "do", "go", "he", "if", "in", "is", "it", "me", "my", "no", "of", "on", "or", "to", "up", "us", "we"],
    3: ["and", "ant", "are", "art", "bat", "cat", "dog", "eat", "fan", "get", "hat", "ink", "job", "key", "log", "map", "not", "one", "pen", "run", "sat", "the", "van", "win", "yes"],
    4: ["able", "acid", "ball", "best", "book", "card", "dark", "each", "face", "give", "hand", "idea", "join", "keep", "lamp", "meet", "near", "open", "park", "quit", "rain", "same", "take", "unit", "very", "wave", "year"],
    5: ["apple", "beach", "brave", "clean", "dance", "eager", "fight", "grand", "heart", "house", "juice", "knife", "light", "magic", "never", "ocean", "piano", "quiet", "right", "smart", "table", "unity", "voice", "water", "yacht"],
    6: ["animal", "banana", "bright", "canvas", "driver", "engine", "flower", "garden", "health", "island", "journey", "kindred", "library", "market", "nation", "office", "person", "quiets", "radius", "school", "travel", "unique", "vision", "window", "yellow"],
    7: ["ability", "balance", "capture", "delight", "example", "freedom", "genuine", "history", "imagine", "justice", "kingdom", "liberty", "mystery", "network", "outsider", "picture", "quality", "resolve", "station", "theater", "unusual", "victory", "western", "youthful", "zealous"],
    8: ["absolute", "building", "champion", "decision", "elevator", "frontier", "generous", "harmony", "integrity", "kindness", "lifetime", "momentum", "national", "opposite", "potential", "question", "relevant", "strategy", "tomorrow", "umbrella", "valuable", "waterfall", "yesterday", "zodiacal"],
    9: ["adventure", "beautiful", "challenge", "dangerous", "effective", "fantastic", "grateful", "happiness", "immediate", "jealousy", "knowledge", "landscape", "marvelous", "nocturnal", "operation", "portfolio", "reception", "signature", "technical", "vacation", "wonderful", "youthful"],
    10: ["accomplish", "biological", "calculator", "deliberate", "excitement", "foundation", "graduation", "happiness", "innovation", "jubilantly", "kilometer", "leadership", "mysterious", "navigator", "operational", "production", "revelation", "systematic", "television", "underneath", "victorious", "wavelength"]
}

t = word_library[1]
math = round((51+50+52)/2)
word = t[math]
print(word)