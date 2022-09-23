"""
Script to scrape labels from websites by Xpath.

Sample usage:

python scraper.py --webpages https://aalborg.dk https://randers.dk

"""
from os import write
from lxml import html
import requests
import csv
import argparse

parser = argparse.ArgumentParser(description='Get labels from webpages.')
parser.add_argument('--webpages', metavar='N', type=str, nargs='+',
                    help='urls to scrape')
args = parser.parse_args()


def get_labels(url, write_csv=True):
    """
    Get the labels from a given url
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.text)

    labels = []

    # ==========================================
    # Get labels according to Xpath
    # ==========================================
    for label in tree.xpath('//div//a//text()'):
        if label != None:
            labels.append(label.strip())
        #print(label)

    for label in tree.xpath('//div//option//text()'):
        if label != None:
            labels.append(label.strip())
        #print(label)

    labels = list(dict.fromkeys(labels)) # Remove duplicates by turning into dict and back to list
    labels = list(filter(None, labels)) # Remove empty strings

    labels.sort()

    print(labels)
    print(f"{len(labels)} labels found in {url}")

    # ==========================================
    # Write file
    # ==========================================
    if write_csv:
        url_filename = "".join(x for x in url if x.isalnum())
        with open(f'labels_{url_filename}.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for item in labels:
                filewriter.writerow([item])

    return labels


if __name__ == "__main__":

    # Get webpages from command line options
    webpages = args.webpages

    # If there were no webpages in the command line, use these instead.
    if webpages == None:
        # If you run this file in your editor, simply add the urls here.
        webpages = [
            'https://www.aalborg.dk/',

            ]

    for webpage in webpages:
        get_labels(webpage)

