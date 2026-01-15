import requests
from config import API_KEY

class NewsFeed:
    """Об'єкт, що отримує новини через API."""
    
    def __init__(self, interest, language='en'):
        self.interest = interest
        self.language = language
        self.api_key = API_KEY
        self.url = f"https://newsapi.org/v2/everything?q={self.interest}&language={self.language}&apiKey={self.api_key}"

    def get_news(self):
        try:
            response = requests.get(self.url)
            
            if response.status_code != 200:
                return f"Помилка API: Статус {response.status_code}. Перевірте ключ або з'єднання."

            content_dict = response.json()

            if "articles" not in content_dict:
                return "Помилка: Невірний формат відповіді від сервера новин."

            articles = content_dict["articles"]

            if not articles:
                return f"На жаль, за темою '{self.interest}' свіжих новин за останню добу не знайдено."

            email_body = ""
            for article in articles[:5]: 
                email_body += f"<p><a href='{article['url']}'>{article['title']}</a></p><br>"
            
            return email_body
            
        except Exception as e:
            return f"Сталася помилка при отриманні новин: {e}"