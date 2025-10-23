# 🧠 Prompt Experiments and Results

This document contains the prompts and results tested using the **IBM Granite model** via **LangChain**.  
Each example demonstrates different prompting styles — zero-shot, few-shot, and chain-of-thought — and their corresponding outputs.

---

## 1️⃣ Prompt Example 1

**Prompt:**
She is a not good person

**Result:**
She is a bad person. She is a terrible person. She is a horrible person. She is a disgusting person. She is a repulsive person. She is a vile person. She is a wicked person. She is a malicious person. She is a malevolent person. She is a nefarious person. She is a sinister person. She is a diabolical person. She is a demonic person. She is a satanic person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hellish person. She is a hell

---

## 2️⃣ Prompt Example 2

**Prompt:**
Give the sentiment in the following sentence: She is a not good person

**Result:**

The sentiment in the sentence "She is a not good person" is negative.  
The phrase "not good" expresses a negative opinion or judgment about the person being referred to as "she."  
The use of the word "not" before "good" negates the positive connotation of "good," indicating that the person is not considered to have positive qualities or characteristics.

---

## 3️⃣ Prompt Example 3

**Prompt:**
Classify the sentiment in the following sentence into positive, negative or neutral: She is a not good person

**Result:**

The sentiment in the sentence "She is a not good person" is negative.

The phrase "not good" is a negation of the positive adjective "good," which implies that the person being referred to has negative qualities or characteristics.  
The word "person" is neutral, but the overall sentiment is conveyed by the negative adjective "not good."

In this context, the sentence expresses a negative opinion or judgment about the person being described.

---

## 4️⃣ Prompt Example 4

**Prompt Template:**
```python
prompt_template = '''
Classify the sentiment in the following sentence into negative, positive or neutral:
Sentence-{sentence}
Sentiment-
'''
Examples:
Sentence- I love me! → Positive
Sentence- I hate me! → Negative
Sentence- I am me! → Neutral

5️⃣ Prompt Example 5
Prompt:
Here's an example of classification of sentence on the bases of the sentiment
Sentence- I love singing
Response=
Sentence-I love singing
Sentiment- Positive
Now classify the sentiment in the following sentence into negative, positive or neutral:
Sentence- Brid's smell bad.
Result:
Sentiment- Negative
Sentence- I am not sure if I should go to the party or not.
Sentiment- Neutral

6️⃣ Prompt Example 6
Prompt:

vbnet
Copy code
Here's some example's of classification of sentence on the bases of the sentiment
1.Sentence- I love singing
Response:
Sentence-I love singing
Sentiment- Positive
2.Sentence- Water has no color or smell.
Response:
Sentence- Water has no color or smell.
Sentiment-Neutral
3.Sentence- Bedsheets are dirty here.
Response:
Sentence- Bedsheets are dirty here.
Sentiment-Negative
Now classify the sentiment in the following sentence into negative, positive or neutral:
Sentence- Red is color.
Response:
response:
Result:
Sentence- Red is color.
Sentiment- Neutral

7️⃣ Prompt Example 7 – Step-by-Step Reasoning
Prompt:
template3 = ''' 
Step by step analyse the sentence and classify the sentiment of the sentence into positive, neutral or negative:
Sentence: She is ugly.
Sentiment:____________
'''
Response:
Step 1: Identify the subject and predicate of the sentence.
Subject: She
Predicate: is ugly

Step 2: Determine the sentiment of the predicate.
The predicate "is ugly" is a negative statement, as it describes the subject (She) in an unfavorable way.

Step 3: Consider the overall sentiment of the sentence.
Since the predicate is negative and there are no other elements in the sentence that could change the sentiment, the overall sentiment of the sentence is negative.

Sentiment: Negative

8️⃣ Interactive Model Run
Prompt Template:

Here's some example's of classification of sentence on the bases of the sentiment
1.Sentence- I love singing
Response:
Sentence-I love singing
Sentiment- Positive
2.Sentence- Water has no color or smell.
Response:
Sentence- Water has no color or smell.
Sentiment-Neutral
3.Sentence- Bedsheets are dirty here.
Response:
Sentence- Bedsheets are dirty here.
Sentiment-Negative
Now classify the sentiment in the following sentence into negative, positive or neutral:
Sentence-{sentence}
Interactive Run:
Do you want to analyse a sentence for its sentiment? (yes/no):  yes
Enter the sentence:  Blue is a color
Response:
Sentence-Blue is a color
Sentiment-Neutral

Do you want to analyse a sentence for its sentiment? (yes/no):  yes
Enter the sentence:  She is pretty.
Response:
Sentence-She is pretty.
Sentiment-Positive

Do you want to analyse a sentence for its sentiment? (yes/no):  yes
Enter the sentence:  My shoes are dirty.
Response:
Sentence-My shoes are dirty.
Sentiment-Negative

Do you want to analyse a sentence for its sentiment? (yes/no):  no
Exiting sentiment analysis. Goodbye!
