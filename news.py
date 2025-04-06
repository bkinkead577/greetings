# A[i key:  772a07cebc1a42fc95bade964dfb39a3
import requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles..."""

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "772a07cebc1a42fc95bade964dfb39a3"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
            # print(article['title'], article['url'])

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        # x = content['articles'][2]['title']
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url
# TODO: Add new class
# TODO: add another class



#pprint(content)

if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa', from_date='2025-04-01', to_date='2025-04-10', language='en')
    print(news_feed.get())
