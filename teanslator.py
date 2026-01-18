# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("translation", model="VAGOsolutions/SauerkrautLM-Translator-LFM2.5-1.2B")
result = pipe("Hello, my name is John.")
print(result)
# [{'translation_text': 'Hallo, mein Name ist John.'}]
result = pipe("The weather is nice today.")
print(result)