import spacy
import en_core_web_sm

input_sentence = ""
natural_language = spacy.load("en_core_web_sm") #English

while input_sentence != "quit":
    # Pass the question string directly into the nlp object
    input_sentence = input()
    doc = natural_language(input_sentence)

    # 1. Extract Named Entities (What real-world targets are mentioned?)
    print("Entities found:")
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")

    # 2. Analyze the grammatical structure (What is the action and subject?)
    print("\nGrammatical Breakdown:")
    for token in doc:
        print(f" Word: {token.text:10} | Role: {token.dep_:10} | Part of Speech: {token.pos_}")



