import requests
from bs4 import BeautifulSoup
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


@app.route('/order/info', methods=['GET', 'POST'])
def order_info():
    return make_response(jsonify(results()))


def open_url(url):
    response = requests.get(url)
    data = response.text
    result = BeautifulSoup(data, 'html.parser')

    return result


def address(day, classification):
    url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=" + day + "&order=" + classification + "&view=image"

    return url


def genre_classify(dic, genre, title):
    dictionary = dic.get(genre).append(title)

    return dictionary


def results():
    req = request.get_json(force=True)
    queryText = req.get('queryResult').get('outputContexts')
    param = queryText[0]['parameters']

    day = param['day']
    classify = param['classify']
    genre = param['genre']

    title_list = crawl(day, classify, genre)

    response = {
        'fulfillmentMessages': [{
            'text': {'text':
                     ["This is a response from webhook."]
                     }
        }]
    }

    return response


def crawl(day, classify, genre):
    soup = open_url(address(day, classify))
    tags = soup.find_all(class_="more")
    webtoon_view_detail_urls = []
    title_genres = {}
    title_list = []

    for tag in tags:
        webtoon_view_detail_urls.append("https://comic.naver.com" + tag.a.get('href'))

    for i in range(len(webtoon_view_detail_urls)):
        soup = open_url(webtoon_view_detail_urls[i])

        title_crawling = soup.find(class_="comicinfo").h2
        title_parse = str(title_crawling)[str(title_crawling).index('>') + 1:str(title_crawling).index('<span')]
        title = title_parse.lstrip()

        genre_crawling = soup.find(class_="genre").text
        genre_list = genre_crawling.split(', ')
        title_genres[title] = genre_list

    for title in title_genres:
        if genre in title_genres.get(title): title_list.append(title)

    return title_list


# def response(title_list):
#
#
#     response = {
#         'fulfillmentMessages': [{
#             'text': {'text':
#                      ["This is a response from webhook."]
#                      }
#         }]
#     }
#
#     return response


if __name__ == '__main__':
    app.run()