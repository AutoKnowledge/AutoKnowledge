from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000/')
text = "Obama's mother is Hillary"

output = nlp.annotate(text, properties={
    # 'annotators': 'tokenize,ssplit,pos,lemma,depparse,natlog,ner,coref,openie,kbp',
    'annotators': 'openie',
    'outputFormat': 'json'
})
print(output)
