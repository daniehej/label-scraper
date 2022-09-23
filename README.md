# label-scraper
Implementation of label scraper from the paper: 

I Kadek Aditya Cahaya Putra, Dana Sulistiyo Kusumo, Anisa Herdiani, lndra Lukman Sardi and Shinta Yulia Puspitasari: An Automatic Website Menu Comparison among Indonesia’s University Websites for Designing Labeling System of an Indonesia University Website, Journal of Computer Science, 2019.

[Link to paper on researchgate.net](https://www.researchgate.net/publication/332630549_An_Automatic_Website_Menu_Comparison_among_Indonesia%27s_University_Websites_for_Designing_Labeling_System_of_an_Indonesia_University_Website)

Labels are obtained using Xpath descriptors which according to the paper should catch the majority of actionable labels on websites for the purpose of comparisons. As in the paper, the used Xpath descriptors are as follows
```
//div//a//text()
//div//option//text()
```
If this does not catch the wanted actionable labels, it is advisable to experiment with different Xpath descriptors as examined in the paper.

## Dependencies
```
requests
lxml
pandas
```

## Usage
Command line usage
```
python scraper.py --webpages https://aalborg.dk https://randers.dk
```

For the purpose of processing a list of URLs and obtaining the output labels as CSV and XLSX spreadsheet, organise the input URLs in a CSV file as in the example `websites.csv` and run
```
python run_scraper.py
```
