"""extract bibtex from website
fixme: not match the whole word.
example: Give Gan, return Gang, Gan,
"""
import re
import requests
from bs4 import BeautifulSoup
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="https://openaccess.thecvf.com/CVPR2021?day=all")
    parser.add_argument("--keywords", nargs='+', help='case-insensitive')
    parser.add_argument("--dst_file", type=str, default="output.bib")
    args = parser.parse_args()
    return args

def main(args):
    """main function"""
    r = requests.get(args.url)
    demo = r.text

    soup = BeautifulSoup(demo, 'html.parser')
    paper_list = []
    # words = ['adversarial']
    cnt = 0
    for word in args.keywords:
        for i, k in enumerate(soup.find_all('div', class_='bibref')):
            text = k.get_text()
            match_flag = re.search(rf"\b{word}\b", text, re.IGNORECASE)
            if i in paper_list:
                continue
            if match_flag is not None:
                cnt += 1
                with open(args.dst_file, 'a') as f:
                    f.write(f'{text}\n')
                paper_list.append(i)
    print("{:d} bibs have been saved!".format(cnt))

if __name__ == '__main__':
    args = get_args()
    main(args)
