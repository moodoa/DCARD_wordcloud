# DCARD_wordcloud
製作指定期間內指定看版的 topic 文字雲

![alt text](https://i.imgur.com/dHD8QRF.png)

## dcard_wordcloud.py
* 以 `看板`、`開始時間`、`結束時間`、`排除字詞` 為參數爬取 DCARD 文章 Topics 並輸出文字雲。

## Requirements
python 3

## Usage
以爬取 `時事版` `2020/10/1 ~ 2020/10/30` 日的 topics ，並排除 `["時事", "討論", "新聞"]` 為例。

```
if __name__=="__main__":
    draw_cloud(get_forum_trending_word("trending", "2020/10/1", "2020/10/30", ["時事", "討論", "新聞"]))

輸出如首圖
```
## Installation
`pip install -r requriements.txt`

