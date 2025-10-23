#!/usr/bin/env python
# coding: utf-8

import warnings
warnings.filterwarnings("ignore")

from langchain_ibm.llms import WatsonxLLM
from langchain_core.prompts import PromptTemplate


# MODEL CREATION

model_id = "ibm/granite-4-h-small"
project_id = "YOUR_PROJECT_ID"  # required for IBM Cloud usage
url = "YOUR_URL"

params = {
    "max_new_tokens": 200,
    "min_new_tokens": 10,
    "temperature": 0.2,
    "top-p": 0.2,
    "top-k": 1
}

sentiment_model = WatsonxLLM(
    model_id=model_id,
    project_id=project_id,
    url=url,
    params=params
)
# PROMPT TEMPLATE (LangChain)

template = """
Classify the sentiment in the following sentence into Negative, Positive, or Neutral:
Sentence: {sentence}
Sentiment:
"""
prompt = PromptTemplate.from_template(template)


# MODEL INVOCATION EXAMPLES

print(sentiment_model.invoke('She is a not good person'))  # quick trial

# Zero-shot variations
print(sentiment_model.invoke('Give the sentiment in the following sentence: She is a not good person'))
print(sentiment_model.invoke('Classify the sentiment in the following sentence into positive, negative or neutral: She is a not good person'))

# Template usage
print(sentiment_model.invoke(prompt.format(sentence='I love me!')))
print(sentiment_model.invoke(prompt.format(sentence="I don't like fruits.")))

# Batch examples
sentences = [
    'Blue is a good color',
    'Blacks are used in funerals',
    'Lily is my birth flower',
    'Open the door please'
]

for sentence in sentences:
    print(f'Sentence: {sentence}')
    print('Sentiment:', sentiment_model.invoke(prompt.format(sentence=sentence)))
    print()

# One-shot prompting
template1 = """
Here's an example of classification based on sentiment:
Sentence: I love singing
Sentiment: Positive

Now classify the sentiment in the following sentence:
Sentence: Birds smell bad.
Sentiment:
"""
print(sentiment_model.invoke(template1))

# Few-shot prompting
template2 = """
Here are some examples of sentiment classification:
1) Sentence: I love singing
   Sentiment: Positive
2) Sentence: Water has no color or smell.
   Sentiment: Neutral
3) Sentence: Bedsheets are dirty here.
   Sentiment: Negative

Now classify this sentence:
Sentence: Red is color.
Sentiment:
"""
print(sentiment_model.invoke(template2))

# Chain-of-thought prompting
template3 = """
Step by step, analyze and classify the sentiment:
Sentence: She is ugly.
Sentiment:
"""
print(sentiment_model.invoke(template3))


# INTERACTIVE MODE

while True:
    answer = input('Do you want to analyse a sentence for its sentiment? (yes/no): ')
    if answer.strip().lower() in ['yes', 'y', 'yup', 'ya']:
        sentence = input('Enter the sentence: ')
        print(sentiment_model.invoke(prompt.format(sentence=sentence)))
    else:
        print("Exiting sentiment analysis. Goodbye!")
        break
