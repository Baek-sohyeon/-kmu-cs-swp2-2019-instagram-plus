import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://kapi.kakao.com/v1/vision/multitag/generate'
MYAPP_KEY = '9c4f2cf226ede514870bd212fc61ef80'

def generate_tag(image_url):
    hashtag = ''
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = {'image_url': image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        result = resp.json()['result']
        if len(result['label_kr']) > 0:
            if type(result['label_kr'][0]) != str:
                result['label_kr'] = map(lambda x: str(x.encode("utf-8")), result['label_kr'])
            hashtag += ("#일상 #데일리 #맞팔선팔환영 #맞팔 #소통 \n#선팔하면맞팔 #좋아요반사 #좋아요테러 \n#맞팔해요 #선팔해요 #팔로우늘리기 #좋반테러 \n#좋반댓 #첫줄반사 #likeforlikes #instalike \n#selfie #instamood #daily \n#followforfollowback #{}".format(' #'.join(result['label_kr'])))
            return hashtag
        else:
            hashtag += ("이미지로부터 태그를 생성하지 못했습니다.")
            return hashtag

    except Exception as e:
        print(str(e))
        sys.exit(0)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Classify Tags')
#     parser.add_argument('image_url', type=str, nargs='?',
#         default="https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/10.jpg",
#         help='image url to classify')
#
#     args = parser.parse_args()
#
#     generate_tag(args.image_url)

