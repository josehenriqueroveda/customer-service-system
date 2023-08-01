import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class ChartGenerator:
    def generate_nps_chart(self, nps, detractors, promoters, passives):
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
        ax.set_xlim(0, 100)
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
