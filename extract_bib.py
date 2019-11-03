"""extract bibtex from website
fixme: not match the whole word.
example: Give Gan, return Gang, Gan,
"""
import re
import requests
from bs4 import BeautifulSoup

def main(link, keywords):
    """main function"""
    print("Attention: Ignore Case!")
    r = requests.get(link)
    demo = r.text

    soup = BeautifulSoup(demo, 'html.parser')
    paper_list = []
    # words = ['adversarial']
    cnt = 0
    for word in keywords:
        for i, k in enumerate(soup.find_all('div', class_='bibref')):
            text = k.get_text()
            match_flag = re.search(word, text, re.IGNORECASE)
            if i in paper_list:
                continue
            if match_flag:
                cnt += 1
                with open("./ICCV2019.bib", 'a') as f:
                    f.write(text)
                paper_list.append(i)
    print("{:d} bibtex files have been created!".format(cnt))

if __name__ == '__main__':
    words = ['adversarial', 'defense', 'attack', 'GAN']
    url = "http://openaccess.thecvf.com/ICCV2019.py"
    main(url, words)
