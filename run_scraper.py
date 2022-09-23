import scraper
import pandas as pd
import datetime as dt

websites = pd.read_csv('websites.csv', encoding='iso-8859-1')

websites['time'] = dt.datetime.now()

websites['result'] = websites['URL'].apply(scraper.get_labels)

websites.set_index('Name')

web_t = websites.T

out_df = pd.DataFrame([])

for column in web_t.columns:
    web_t[column].loc['result'] = [string for string in web_t[column].loc['result'] if len(string)<50]
    out_df = pd.concat((out_df, web_t[column].explode(ignore_index=True)), axis=1)

out_df.to_csv('output.csv', header=False, index=False)
out_df.to_excel('output.xlsx', header=False, index=False)

