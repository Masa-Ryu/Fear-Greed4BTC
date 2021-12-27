from datetime import datetime, timezone, timedelta

import matplotlib.pyplot as plt
import requests


class Fear2Greed:
    def __init__(self):
        self.url = 'https://api.alternative.me/fng/?limit=30'

    @staticmethod
    def fetch(url):
        res = requests.get(url)
        res = res.json()
        return res

    def run(self):
        r = self.fetch(self.url)
        data = r['data']
        date, values, status = [], [], None
        for _ in reversed(data):
            date.append(
                datetime.fromtimestamp(
                    int(_['timestamp']),
                    timezone(timedelta(hours=+9), 'JST')
                    ).strftime('%m/%d')
                )
            values.append(int(_['value']))
            status = _['value_classification']
        plt.plot(date, values, marker='.', markersize=20)
        plt.xticks(rotation=90, fontsize=6)
        plt.ylabel('Fear  & Greed')
        plt.title('Fear & Greed')
        plt.savefig('fear_greed.jpg', dpi=300)
        return status, values
