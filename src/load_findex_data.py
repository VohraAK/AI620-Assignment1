from . import config
import wget

def get_csv_from_url(url: str):
    '''This fucntion uses wget to download the report from the provided URL'''
    _ = wget.download(url, out=config.WB_GLOBAL_FINDEX_DIR)
    

if __name__ == "__main__":
    get_csv_from_url(config.WB_GLOBAL_FINDEX_URL)
