from src import config, load_findex_data, load_search_data, load_news_articles, process_findex_data, process_trends_data, process_news_articles

def run_pipeline():

    print(f"\n----------Data Ingestion----------\n")
    
    print("Fetching World Bank FINDEX data...\n")
    load_findex_data.get_csv_from_url(config.WB_GLOBAL_FINDEX_URL)

    print("\n\nFetching Google Trends data...\n")
    load_search_data.get_search_data(config.PYTRENDS_KEYWORDS, config.SEARCH_TERM_DIR)
    
    print("\n\nFetching NewsAPI news articles...\n")
    load_news_articles.get_articles(config.NEWSAPI_URL, config.QUERY_KEYWORDS, config.ARTICLES_DIR)

    print(f"\n----------Data Ingestion complete----------\n")
    
    
    print(f"\n\n----------Data Processing----------\n")
    
    print("Processing World Bank Findex data...\n")
    process_findex_data.process_csv(config.FINDEX_RAW_CSV_PATH, config.FINDEX_PROCESSED_CSV_PATH)
    
    print("Processing search trends data...\n")
    process_trends_data.process_csv(config.TRENDS_RAW_CSV_PATHS, config.TRENDS_PROCESSED_CSV_DIR)
    
    print("Processing news articles...\n")
    process_news_articles.process_json(config.ARTICLES_RAW_CSV_PATH, config.ARTICLES_PROCESSED_CSV_PATH)
    
    print(f"\n\n----------Data Processing complete----------\n")

if __name__ == "__main__":
    run_pipeline()