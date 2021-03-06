import numpy as np
import requests
from PIL import Image
from bs4 import BeautifulSoup
from wordcloud import WordCloud,STOPWORDS

url_root = 'http://top.baidu.com'




def get_url(source):
    soup = BeautifulSoup(source,'html.parser')
    tag_div = soup.find_all('div',attrs={'class':'hblock'})

    urls = []
    for td in tag_div:
        tag_a =td.find_all('a')
        for ta in tag_a:
            href = ta.get('href').replace('.','')
            url_hot = url_root+href
            urls.append(url_hot)

    return urls

def find_keywords(source):
    keywords = []
    soup = BeautifulSoup(source, 'html.parser')

    tag_a = soup.find_all('a', attrs={'class': 'list-title'})
    for ta in tag_a:
        text = ta.get_text()
        keywords.append(text)

    return keywords


def draw_wordcloud():
    color_mask = np.array(Image.open("cat.png"))

    hot_text = []
    with open('hot.txt') as f:
        for i in f:
            hot_text.append(i.strip())

    cut_text = ' '.join(hot_text)

    stopwords = list(STOPWORDS)
    with open('stop.txt', encoding='utf-8') as f:
        for i in f:
            stopwords.append(i.strip())
    # stopwords=set(stopwords)
    cloud = WordCloud(max_words=1000, mask=color_mask, margin=10,
        random_state=10, font_path="msyh.ttc",
        background_color='white',
        stopwords=set(stopwords))
    wc = cloud.generate(cut_text)

    wc.to_file("snoopy.png")


def main():
    url_baidu = 'http://top.baidu.com/buzz?b=1&fr=topindex'

    response = requests.get(url_baidu).content.decode('gbk')

    urls = get_url(response)

    all_keywords = []
    for u in urls:
        resp = requests.get(u).content.decode('gbk')
        keywords = find_keywords(resp)
        all_keywords.extend(keywords)

    with open('hot.txt', 'w') as f:
        f.write('\n'.join(all_keywords))

    draw_wordcloud()


if __name__ == '__main__':
    main()