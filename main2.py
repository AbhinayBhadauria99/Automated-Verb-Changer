import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

def get_past_tense(verb):
    lemmatizer = WordNetLemmatizer()
    base_form = lemmatizer.lemmatize(verb, 'v')
    past_tense = base_form + 'ed'
    return past_tense

def get_present_continuous(verb):
    present_continuous = verb + 'ing'
    return present_continuous

def main():
    verbs = ["jump", "play", "work", "kill", "stay"]

    print("Verb\t\tPast Tense\tPresent Continuous")
    print("------------------------------------------")

    for verb in verbs:
        past_tense = get_past_tense(verb)
        present_continuous = get_present_continuous(verb)

        print(f"{verb}\t\t{past_tense}\t\t{present_continuous}")

if __name__ == "__main__":
    main()
