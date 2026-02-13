# load_findex_data.py
WB_GLOBAL_FINDEX_URL = "https://data360files.worldbank.org/data360-data/data/WB_FINDEX/WB_FINDEX.csv"
WB_GLOBAL_FINDEX_DIR = "data/raw"


# load_news_articles.py
NEWSAPI_URL = "https://newsapi.org/v2/everything"
QUERY_KEYWORDS ='(Pakistan AND ("digital payment" OR "mobile wallet" OR fintech OR "financial inclusion" OR "cashless economy")) OR JazzCash OR EasyPaisa OR Raast OR SadaPay OR NayaPay OR "State Bank of Pakistan" OR "branchless banking" OR "QR payment"'
ARTICLES_language = 'en'
ARTICLES_DIR = "data/raw"

 
# load_search_data.py
PYTRENDS_KEYWORDS = {
    'primary_wallets': ['JazzCash', 'EasyPaisa', 'SadaPay', 'NayaPay', 'Raast'],
    'payment_features': ['mobile wallet', 'QR code payment', 'digital wallet', 'cashless payment', 'online payment'],
    'use_cases': ['bill payment app', 'mobile topup', 'money transfer', 'online shopping Pakistan'],
    'banking_terms': ['mobile banking', 'branchless banking', 'digital account', 'online banking Pakistan']
}
SEARCH_TERM_DIR = "data/raw"


# process_findex_data.py
FINDEX_RAW_CSV_PATH = "data/raw/WB_FINDEX.csv"
FINDEX_PROCESSED_CSV_PATH = "data/processed/pakistan_digital_payments_findex.csv"
FINDEX_COLS_TO_RETAIN = ["TIME_PERIOD", "INDICATOR_LABEL", "OBS_VALUE", "REF_AREA_LABEL", "SEX_LABEL", "AGE_LABEL", "URBANISATION_LABEL", "COMP_BREAKDOWN_1_LABEL", "COMP_BREAKDOWN_2_LABEL", "COMP_BREAKDOWN_3_LABEL"]
FINDEX_KEY_INDICATORS = ["Made or received a digital payment", "Made a digital merchant payment", "Received digital payments", "Mobile money account", "Digitally enabled account", "Used mobile phone or card to pay for in-store purchase", "Used a mobile phone or the internet to pay bills", "Used a mobile phone or the internet to buy something online", "Received wages: through a mobile phone", "Made a utility payment: using a mobile phone"]


# process_trends_data.py
TRENDS_RAW_CSV_PATHS = {
    'primary_wallets': 'data/raw/PK_digital_payments_trends_primary_wallets.csv',
    'payment_features': 'data/raw/PK_digital_payments_trends_payment_features.csv',
    'use_cases': 'data/raw/PK_digital_payments_trends_use_cases.csv',
    'banking_terms': 'data/raw/PK_digital_payments_trends_banking_terms.csv'
}
TRENDS_PROCESSED_CSV_DIR = "data/processed"


# process_news_articles.py
ARTICLES_RAW_CSV_PATH = "data/raw/pakistan_digital_payments_articles.json"
ARTICLES_PROCESSED_CSV_PATH = "data/processed/pakistan_digital_payments_processed_articles.json"

