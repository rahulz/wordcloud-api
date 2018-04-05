from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def wordcloud(data, title=None):
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud=WordCloud(
        background_color='white',
        stopwords=STOPWORDS,
        max_words=200,
        max_font_size=40,
        scale=3,
    ).generate(str(data)))
    return plt
