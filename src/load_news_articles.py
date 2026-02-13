from . import config
import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

def get_articles(api_url: str, query_keywords: str, save_dir: str):
    '''This function requests NewsAPI for news articles related to the argument keywords'''
    response = requests.get(f"{api_url}?q={query_keywords}&apiKey={NEWSAPI_KEY}")
    
    res_body = response.json()
    
    os.makedirs(save_dir, exist_ok=True)
    
    # output is an array of objects (news articles)
    # print(news_articles)
    with open(f"{save_dir}/pakistan_digital_payments_articles.json", "w") as file:
        json.dump(res_body, file)
    

if __name__ == "__main__":
    get_articles(config.NEWSAPI_URL, config.QUERY_KEYWORDS, config.ARTICLES_DIR)
