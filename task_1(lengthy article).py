from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
def summary_gen(text,num_sentences=3):
  stop_words= set(stopwords.words('english')+ list(punctuation))
  words=word_tokenize(text.lower())
  freq={}
  for word in words:
    if word not in stop_words:
      freq[word]=freq.get(word,0)+1
  sentences=sent_tokenize(text)
  sentences_scores={}
  for sent in sentences:
    for word in word_tokenize(sent.lower()):
      if word in freq:
        sentences_scores[sent]=sentences_scores.get(sent,0)+freq[word]
  top_sentences=sorted(sentences_scores,key=sentences_scores.get, reverse=True)[:num_sentences]
  return ' '.join(top_sentences)
article="""Artificial Intelligence (AI) has emerged as a transformative force in various sectors, and education is no exception. Over the last decade, the integration of AI into educational systems has grown rapidly. From personalized learning tools to automated grading systems, AI is reshaping the way students learn and teachers instruct.

One of the most significant contributions of AI in education is personalized learning. Traditional education often follows a one-size-fits-all approach, where each student is expected to keep pace with the curriculum regardless of their individual capabilities. AI algorithms can analyze students' learning patterns, strengths, and weaknesses to provide customized educational content. This not only helps students learn at their own pace but also enhances their understanding and retention of knowledge.

Moreover, AI-powered tools like chatbots and virtual teaching assistants are helping to bridge the communication gap between students and educators. These tools are available 24/7 and can answer students’ questions instantly, provide additional learning resources, or guide them through difficult concepts. This continuous support outside the classroom makes learning more accessible and engaging.

Assessment is another area where AI is making a difference. Automated grading systems can evaluate multiple-choice questions and even essay-type answers to some extent. This reduces the administrative burden on teachers, allowing them more time to focus on instructional strategies and student interaction. Furthermore, AI can detect patterns in students’ performance and predict those who are at risk of falling behind, enabling timely intervention.

In developing countries, where educational resources are limited, AI has the potential to democratize learning. With internet connectivity and mobile devices becoming more widespread, students in remote areas can access high-quality educational content and virtual classes. This helps bridge the educational divide and opens up opportunities for lifelong learning.

However, the integration of AI in education is not without challenges. Data privacy, algorithmic bias, and the lack of human touch in automated systems are some of the concerns that need to be addressed. Additionally, teachers must be adequately trained to use AI tools effectively and ethically in the classroom.

In conclusion, while AI brings a plethora of opportunities to the education sector, its implementation should be carefully planned. A balanced approach that combines technological innovation with human values will ensure that AI becomes a tool for inclusive and effective education rather than a replacement for traditional teaching methods."""
print(summary_gen(article))