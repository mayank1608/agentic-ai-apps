import pandas as pd
import matplotlib.pyplot as plt

class ChartTool:

    name = "chart_tool"

    def execute(self, rows):

        df = pd.DataFrame(rows)

        plt.figure(figsize=(8,5))

        plt.bar(
            df.iloc[:,0],
            df.iloc[:,1]
        )

        path = "salary_chart.png"

        plt.savefig(path)

        return path