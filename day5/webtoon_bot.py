# -*- coding:utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import requests
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

@app.route('/<day>')
def daum_toon(day):
    # daily_toon_data = {} # 선언
    url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/'+day
    data = request_json_data_from_url(url)
    # daily_toon_data[day] = parse_daum_webtoon_data(data)
    # return daily_toon_data
    return {day: parse_daum_webtoon_data(data)}
    # return {day: data}


def request_json_data_from_url(url):
    response = requests.get(url)
    data = response.json()  # 응답으로 온 내용을 JSON형식으로 바꿔줌.
    return data


def parse_daum_webtoon_data(data):
    # print(data)
    toons = []
    for toon in data["data"]:
        # 제목의 key는 'title'
        title = toon["title"]

        # 웹툰 닉네임으로 상세 url
        nickname = toon["nickname"]

        # 설명의 key는 'introduction'
        desc = toon["introduction"]

        # 작가랑 장르
        # 정통방법!
        # 장르의 위치는 'cartoon' 안에 'genre' 라는 리스트 안에 'name'이라는 key
        genres = []  # 장르의 데이터를 하나씩 넣자!
        for genre in toon["cartoon"]["genres"]:
            genres.append(genre["name"])
        # print(genres)

        # 작가 이름의 위치는 'cartoon' 안에 'artists'라는 리스트 안에 'name'이라는 key
        artists = []
        for artist in toon["cartoon"]["artists"]:
            artists.append(artist["name"])

        # 썸네일 이미지
        img_url = toon["pcThumbnailImage"]["url"]
        url = 'http://webtoon.daum.net/data/pc/webtoon/view/' + nickname
        tmp = {
            title: {
                "nickname": nickname,
                "url": url,
                "desc": desc,
                "genres": genres,
                "writer": artists,
                "img_url": img_url
            }
        }

        # 정보들 넣기
        toons.append(tmp)
        # print(toons)
    return toons

@app.route('/webtoon/<nickname>')
def webtoon_info(nickname):
    # url = 'http://webtoon.daum.net/webtoon/view/'+nickname
    url = 'http://webtoon.daum.net/data/pc/webtoon/view/'+nickname
    # return requests.get(url).json()
    data = request_json_data_from_url(url)
    # print(data)
    return data

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))

def results():
    req = request.get_json(force=True)
    print(req)
    print("----------------------------------")
    queryText = req.get('queryResult').get('outputContexts')
    # output = queryText[0].get('parameters')
    output = queryText[1].get('parameters')
    day = output.get('day_of_week')
    genres = output.get('dgenre')
    # print(site)
    print(day)
    print(genres)

    print("#### CRAWLNG ####")
    # webtoon_url = 'http://webtoon.daum.net/data/pc/webtoon/view/'
    webtoon_url = 'http://webtoon.daum.net/webtoon/view/'
    data = daum_toon(day)
    webtoons = data[day]
    # print(webtoons)
    webtoon_list = []
    title_list = []
    nickname_list = []
    img_list = []
    for webtoon in webtoons:
        webtoon_title = list(webtoon.keys())
        for value in webtoon.values():
            # print(value)
            for l in value["genres"]:
                if genres in l:
                    tmp = {
                        "title": webtoon_title,
                        # "genres_list": value["genres"]
                    }
                    # print(value['nickname'])
                    title_list.append(webtoon_title)
                    nickname_list.append(value['nickname'])
                    img_list.append(value['img_url'])
                    webtoon_list.append(tmp)
    # print(webtoon_list)
    web1 = nickname_list[0]
    # print(web1[0])
    # print(img_list[0])
    response = {
        "fulfillmentText": "This is a text response",
        'fulfillmentMessages': [{
            "text": {
                "text": [
                    webtoon_url + nickname_list[0]+"\n\n"+
                    webtoon_url + nickname_list[1]
                ]
            }
            # "quickReplies": {
            #     "title": "웹툰 목록",
            #     "quickReplies": [
            #         nickname_list[0], nickname_list[1], nickname_list[2]
            #     ]
            # }
            # "card": {
            #     "title": "title",
            #     "subtitle": "subtitle",
            #     "imageUri": "sss",
            #     "buttons": [
            #         {
            #             "text": "button text",
            #             "postback": webtoon_url+nickname_list[0]
            #         }
            #     ]
            # }
        }],
            #
        # 'fulfillmentMessages': [{
        #     "quickReplies": {
        #         "title": "웹툰 목록",
        #         "quickReplies": [
        #             title_list[0], title_list[1], title_list[2]
        #         ]
        #     }
        # }],
        'data': {
            'day': day,
            'genres': genres
        }
    }
    return response

if __name__ == '__main__':
    app.run(debug=True)