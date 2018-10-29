import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window

Window.size = (400,130)

from kivy.uix.boxlayout import BoxLayout

import requests, random

s = ['강', '경', '고', '김', '남', '노', '도', '문', '민', '박', '방', '변', '서', '석', '설', '성', '송', '신', '여', '오', '왕', '유', '이', '장', '전', '정']
f1 = ['서', '선', '성', '슬', '신', '아', '안', '영', '예', '오', '오', '원', '윤','은', '지', '진', '채', '초', '혜', '효']
f2 = ['교', '리', '린', '림', '서', '선', '설', '세', '솔', '수', '슬', '연', '영','예', '오', '우', '윤', '율', '은', '인', '재', '정', '주', '지', '진', '채', '하', '혜', '후', '희']

def randomNames(req_num, mine):
    names = []
    for i in range(req_num):
        while 1:
            new = (
                s[random.randint(0, len(s)-1)] + 
                f1[random.randint(0, len(f1)-1)] +
                f2[random.randint(0, len(f2)-1)]
            )
            if new[0] == mine[0]: continue # 같은 성은 좀 그렇잖아
            if new not in names: 
                names.append(new)
                break
    return names

def sendThis(question_id, user, crush):
    url = 'https://kr.lovemeter.me/save-quiz-response'
    r = requests.post(url, data={'userFullName': user, 'crushFullName': crush, 'encUserQuizId': question_id})
    print('[+]', user, '->', crush)
    return True

def send(question_id, user, crush, req_num):
    for i in range(req_num):
        sendThis(question_id, user, crush)

def sendRandom(question_id, user, req_num):
    names = randomNames(req_num, user)
    for crush in names:
        sendThis(question_id, user, crush)

class LblTxt(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)

class LblNum(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)

class MyApp(App):

    def build(self):
        self.root = Builder.load_file('form.kv')
        return self.root

if __name__ == '__main__':
    MyApp().run()
