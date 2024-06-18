import pandas as pd

df = pd.read_csv('AG_news_dataset/test.csv')
new = df.get(['Description'])
new.to_csv('test_descriptions.csv')
