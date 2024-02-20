import pandas as pd
from elasticsearch import Elasticsearch, helpers

data_files = {
    "airtraffic": "Air Traffic.csv",
    "airlinedelays": "Airline Delays.csv",
    "crimedata": "Crime Data.csv",
    "diamondsdata": "Diamonds Data.csv"
}

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

for index, file in data_files.items():
    df = pd.read_csv(file)
    data = df.to_dict('records')
    helpers.bulk(es, data, index=index, doc_type="_doc", raise_on_error=False)
