# Import Spacy
import spacy
from sys import argv

MODEL_USED = "models/daphne_entities_12"

# Returns 
def ner(text, model=MODEL_USED):
    nlp = spacy.load(model)
    doc = nlp(text)


if __name__ == "__main__":
    # Run test.py "model_path" "text_to_evaluate- in the termina"
    model = argv[1]
    text = argv[2]
    print("\nModel: {}\nText: {}\n".format(model, text))
    nlp = spacy.load(model)
    doc = nlp(text)

    # Find named entities, phrases and concepts
    for index, entity in enumerate(doc.ents):
        print("{}: '{}' corresponds to {}".format(index + 1, entity.text, entity.label_))
    print(doc)