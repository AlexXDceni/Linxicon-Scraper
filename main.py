from scraper import get_words
from ai_chat import get_hint

if __name__ == "__main__":
    words = get_words()
    if words:
        get_hint(words)

        

