from datetime import datetime, timezone, timedelta

import matplotlib.pyplot as plt
import requests

URL = 'https://api.alternative.me/fng/?limit=30'


def fetch(url):
    res = requests.get(url)
    res = res.json()
    return res


def run():
    global URL
    r = fetch(URL)
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
    if status == 'Extreme Greed':
        status = 'Extreme Greed: 売り'
    elif status == 'Extreme fear':
        status = 'Extreme fear: 買い'
        print(msg=f'{status} 恐怖指数: {values[-1]}')


if __name__ == '__main__':
    run()
