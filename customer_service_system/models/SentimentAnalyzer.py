import pandas as pd
from pysentimiento import create_analyzer


class SentimentAnalyzer:
    """
    SentimentAnalyzer class to analyze the sentiment of a given text

    ### Args:
    task (str): The task to perform. It can be "sentiment", "emotion", "hate_speech", "irony", "ner", "pos".
    lang (str): The language of the text. It can be "en", "es", "it", "pt".
    """

    def __init__(self, task: str, lang: str):
        self.analyzer = create_analyzer(task=task, lang=lang)

    def analyze(self, text: str) -> pd.DataFrame:
        return self.analyzer.predict(text)
