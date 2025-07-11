COMPANY: CODTECH IT SOLUTIONS
NAME: NITIN JOHRI
INTERN ID: CT06DG1491
DOMAIN: ARTIFICIAL INTELLIGENCE
DURATION: 6 WEEKS
MENTOR: NEELA SANTOSH
I have created a text summarization code where it summarize lengthy or big texts into one page text or small paragraph.I have listed key steps to make one of those and output below so someone can understand how summarization works in this code of mine.
1) Text Preprocessing:
  The input text is converted to lowercase.It's tokenized into words using word_tokenize, and sentences using sent_tokenize.
2) Stopwords and Punctuation Removal:
  Words like "the", "is", "and", and punctuation marks are considered non-informative and removed using NLTK's stopwords list and    Python's punctuation.
3) Word Frequency Calculation:
  The remaining (informative) words are counted to get their frequency in the text.This frequency acts as a proxy for importance: more frequent words are deemed more important.
4) Sentence Scoring:
  Each sentence is scored based on the sum of the frequencies of its non-stopword words.Essentially, sentences with more "important" words score higher.
5) Summary Selection:
  The sentences are ranked by score, and the top n sentences (default 3) are selected as the summary.
 outputs: 
 From personalized learning tools to automated grading systems, AI is reshaping the way students learn and teachers instruct. AI   algorithms can analyze students' learning patterns, strengths, and weaknesses to provide customized educational content. A balanced approach that combines technological innovation with human values will ensure that AI becomes a tool for inclusive and effective education rather than a replacement for traditional teaching methods.
