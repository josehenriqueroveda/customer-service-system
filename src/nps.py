import os
from dataclasses import dataclass

import openai
from openai.openai_object import OpenAIObject
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.environ["OPENAI_API_KEY"]


@dataclass
class Feedback:
    grade: int
    comment: str


class FeedbackAnalyzer:
    def calculate_nps(self, grades):
        detractors = sum(1 for grade in grades if grade < 7)
        promoters = sum(1 for grade in grades if grade > 8)
        return (promoters - detractors) / len(grades) * 100


class ChartGenerator:
    def generate_nps_chart(self, nps):
        NPS_ZONES = ["Critical", "Improvement", "Quality", "Excellence"]
        NPS_VALUES = [-100, 0, 50, 75, 100]
        NPS_COLORS = ["#FF595E", "#FFCA3A", "#8AC926", "#1982C4"]
        fig, ax = plt.subplots(figsize=(10, 2))
        for i, _ in enumerate(NPS_ZONES):
            ax.barh(
                [0],
                width=NPS_VALUES[i + 1] - NPS_VALUES[i],
                left=NPS_VALUES[i],
                color=NPS_COLORS[i],
            )

        ax.barh([0], width=1, left=nps, color="black")
        ax.set_yticks([])
        ax.set_xlim(-100, 100)
        ax.set_xticks(NPS_VALUES)

        plt.text(
            nps,
            0,
            f"{nps:.2f}",
            ha="center",
            va="center",
            color="white",
            bbox=dict(facecolor="black"),
        )

        patches = [
            mpatches.Patch(color=NPS_COLORS[i], label=NPS_ZONES[i])
            for i in range(len(NPS_ZONES))
        ]
        plt.legend(handles=patches, bbox_to_anchor=(1, 1))

        plt.title("NPS chart")
        plt.show()


def analyze_feelings(feedbacks):
    grades = [feedback.grade for feedback in feedbacks]
    comments_formatted = "\n".join(
        [f"- Grade {feedback.grade}: {feedback.comment}" for feedback in feedbacks]
    )
    prompt = f"""
            Summarize a general analysis on the following comments: 
            {comments_formatted} 
            And return a json object with the key "summary" and the value being the summary. 
        """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a model to analyze feelings from feedbacks.",
            },
            {"role": "user", "content": prompt},
        ],
    )
    if isinstance(response, OpenAIObject):
        summary = response.choices[0].message["content"]
        nps = FeedbackAnalyzer().calculate_nps(grades)
        ChartGenerator().generate_nps_chart(nps)
        return summary
    return None
