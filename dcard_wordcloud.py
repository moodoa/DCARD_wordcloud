import json
import requests

from datetime import datetime
from wordcloud import WordCloud
from matplotlib import colors

def get_forum_trending_word(forum, start_date, end_date, unwanted_list):
    time_expire = False
    all_topics = []
    newest_id = "999999999999"
    while time_expire == False:
        content = requests.get(f"https://www.dcard.tw/_api/forums/{forum}/posts?popular=false&limit=100&before={newest_id}").text
        articles_info = json.loads(content)
        newest_id = str(articles_info[-1]["id"])
        for article in articles_info:
            if datetime.strptime(article["createdAt"].split("T")[0], "%Y-%m-%d") < datetime.strptime(start_date, "%Y/%m/%d"):
                time_expire = True
                break
            if datetime.strptime(article["createdAt"].split("T")[0], "%Y-%m-%d") <= datetime.strptime(end_date, "%Y/%m/%d"):
                print(article["createdAt"])
                for topic in article["topics"]:
                    if topic not in unwanted_list:
                        all_topics.append(topic)

    return all_topics

def draw_cloud(all_topics):
    color_list=["#eb4034", '#edac34','#8de332', "#32e3c3", "#e332e0"]
    colormap=colors.ListedColormap(color_list)
    text = " ".join(all_topics)
    cloud = WordCloud(width=1200, height=800, font_path="SourceHanSansTW-Regular.otf", colormap=colormap).generate(text)
    cloud.to_file('wordcloud.png')
    return "Job Done"

if __name__=="__main__":
    draw_cloud(get_forum_trending_word("trending", "2020/10/1", "2020/10/30", ["時事", "討論", "新聞"]))