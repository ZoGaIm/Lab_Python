from collections import Counter

def analyze_letter_frequencies(text):
    text = text.lower()
    
    letters_only = [ch for ch in text if ch.isalpha()]
    
    counter = Counter(letters_only)

    repeated = sorted([ch for ch, count in counter.items() if count >= 2])

    single = sorted([ch for ch, count in counter.items() if count == 1])

    print("а) Літери, які входять у текст не менше двох разів:", ', '.join(repeated) or "немає")
    print("б) Літери, які входять по одному разу:", ', '.join(single) or "немає")

text = input("Введіть текст (латинськими літерами): ")
analyze_letter_frequencies(text)
