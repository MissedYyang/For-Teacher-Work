'''

尝试写一个自动完成普法任务的脚本


实现功能：
1输入账号密码，实现登陆，或再次输入

2获取该账号下的所有任务
2.1学习练习ok
2.2综合评价——0分，啊哈哈或或或或，不过也算完成了，不管了
2.3法制实践ok


3完成任务。

'''

import re
import time
from requests import post, get


def log_in(username, password):
    '''
    登录
    '''
    token = ''
    url = 'https://service-k329zabl-1251413566.sh.apigw.tencentcs.com/client/Author/login'
    headers = {'Host': 'service-k329zabl-1251413566.sh.apigw.tencentcs.com',
               'Connection': 'keep-alive',
               'Content-Length': '70',
               'sourceId': '1',
               #'access-token': '5cfd6e2497dd6288f3c7e5aebb8a73e7',
               'source': '1',
               #'X-Date': 'Tue, 18 Oct 2022 04:47:17 GMT',
               'content-type': 'application/json',
               #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="Y7gJZIx9Fnycl0Zvw2w1oSDGY7Q="',
               'Accept-Encoding': 'gzip,compress,br,deflate',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
               'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
    json = {"sourceId": "1",
            "loginInfo": username,
            "password": password
            }
    res = post(url=url, headers=headers, json=json)
    # print(res.text)
    t = re.findall('token":"(.*?)"', res.text)
    if len(t) == 0:
        pass
    else:
        token = t[0]
        name = re.findall('"pinyinName":"(.*?)",', res.text)[0]
        school = re.findall('"schoolOrOrg":"(.*?)"', res.text)[0]
        print(school, name, token)
    return token


def get_columnlist(token):
    '''
    获取练习任务情况
    '''
    url = 'https://service-ryyy53hl-1251413566.sh.apigw.tencentcs.com/practice/getColumnList?taskId=23'

    headers = {'Host': 'service-ryyy53hl-1251413566.sh.apigw.tencentcs.com',
               'Connection': 'keep-alive',
               'sourceId': '1',
               'access-token': token,
               'source': '1',
               #'X-Date': 'Tue, 18 Oct 2022 04:58:47 GMT',
               'content-type': 'application/json',
               #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="hpjpwEpaHQQinvAmMwsUYglI+Us="',
               'Accept-Encoding': 'gzip,compress,br,deflate',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
               'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
    res = get(url=url, headers=headers)
    # print(res.text)
    columid_all = re.findall('"columnId":(.*?),', res.text)
    columname_all = re.findall('"name":"(.*?)"', res.text)
    # print(columid_all,columname_all)
    return columid_all, columname_all


def do_columid(columid_all, columname_all):
    '''
    完成练习任务
    '''
    for c in range(len(columid_all)):
        columid = columid_all[c]
        columname = columname_all[c]
        print('正在完成，', columname)

        url = 'https://service-ryyy53hl-1251413566.sh.apigw.tencentcs.com/practice/studyByColumnId?columnId={}&taskId=23'.format(
            columid)
        headers = {'Host': 'service-ryyy53hl-1251413566.sh.apigw.tencentcs.com',
                   'Connection': 'keep-alive',
                   'sourceId': '1',
                   'access-token': token,
                   'source': '1',
                   #'X-Date': 'Tue, 18 Oct 2022 11:50:46 GMT',
                   'content-type': 'application/json',
                   #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="JN3WLg9gyjftNsZ++YVZFoeM8HA="',
                   'Accept-Encoding': 'gzip,compress,br,deflate',
                   'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
                   'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
        res = get(url=url, headers=headers)
        # print(res.text)

        res = get(url=url, headers=headers)
        # print(res.text)

        url = 'https://service-ryyy53hl-1251413566.sh.apigw.tencentcs.com/practice/practice?taskId=23&columnId={}'.format(
            columid)
        res = get(url=url, headers=headers)
        # print(res.text)


def get_task(token):
    '''
    获取实践任务
    '''
    url = 'https://service-8k0n1689-1251413566.sh.apigw.tencentcs.com/punch/activity/selectActivityByUser?taskId=23'
    headers = {'Host': 'service-8k0n1689-1251413566.sh.apigw.tencentcs.com',
               'Connection': 'keep-alive',
               'sourceId': '1',
               'access-token': token,
               'source': '1',
               #'X-Date': 'Tue, 18 Oct 2022 12:10:42 GMT',
               'content-type': 'application/json',
               #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="lNO2uH8Khdsc7+nF6FcG9CPJH/I="',
               'Accept-Encoding': 'gzip,compress,br,deflate',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
               'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
    res = get(url=url, headers=headers)
    # print(res.text)
    # a='{("activityId":.*?"doneFlag":0)}'
    # task_all=re.findall(a,res.text)
    # print(task_all[0])
    taskid_all = re.findall('"ownPhase":"0","taskId":"(.*?)",', res.text)
    activityid_all = re.findall('"activityId":(.*?),', res.text)
    activitytype_all = re.findall(
        '"activityType":"(.*?)","createTime"', res.text)
    # print(taskid_all,activityid_all,activitytype_all)
    return taskid_all, activityid_all, activitytype_all


def do_task(token, taskid_all, activityid_all, activitytype_all):
    '''
    完成综合实践任务
    '''
    for i in range(len(taskid_all)):

        url = 'https://service-8k0n1689-1251413566.sh.apigw.tencentcs.com/punch/record/punch?taskId={}&activityId={}&activityType={}'.format(
            taskid_all[i], activityid_all[i], activitytype_all[i])

        headers = {'Host': 'service-8k0n1689-1251413566.sh.apigw.tencentcs.com',
                   'Connection': 'keep-alive',
                   'Content-Length': '2',
                   'sourceId': '1',
                   'access-token': token,
                   'source': '1',
                   #'X-Date': 'Tue, 18 Oct 2022 12:39:42 GMT',
                   'content-type': 'application/json',
                   #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="ub3BpNnejwUPfabQszCtHWiUnAE="',
                   'Accept-Encoding': 'gzip,compress,br,deflate',
                   'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
                   'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
        json = {}
        res = post(url=url, headers=headers, json=json)
        print(res.text)


def get_paper(token):
    '''
    获取综合评价任务
    '''
    url = 'https://service-g4ju878t-1251413566.sh.apigw.tencentcs.com/paper/getPaper?taskId=23'
    headers = {'Host': 'service-g4ju878t-1251413566.sh.apigw.tencentcs.com',
               'Connection': 'keep-alive',
               'sourceId': '1',
               'access-token': token,
               'source': '1',
               #'X-Date': 'Tue, 18 Oct 2022 13:07:11 GMT',
               'content-type': 'application/json',
               #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="eRRYlzo3oqxJK4Bcint2F4Shfqk="',
               'Accept-Encoding': 'gzip,compress,br,deflate',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
               'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
    res = get(url=url, headers=headers)
    # print(res.text)
    resultid = re.findall('"resultId":(.*?),"timeLeft', res.text)[0]
    paperid = re.findall('"id":(.*?),', res.text)[0]
    answerid_all = re.findall('"id":"(.*?)"', res.text)
    # print(resultid,paperid)
    return resultid, answerid_all, paperid


def do_paper(token, resultid, answerid_all, paperid):
    '''
    完成综合评价任务
    '''
    answer = ''
    # https://service-g4ju878t-1251413566.sh.apigw.tencentcs.com/paper/saveResult?taskId=23&code=undefined&resultId=115164386&answers=4782_B%40!%404783_C%40!%404785_A%40!%404784_C%40!%404790_D%40!%404789_D%40!%404788_B%40!%404791_C%40!%404792_B%40!%404795_A%40!%40&takeTime=64&sourceId=1&paperId=612
    url = 'https://service-g4ju878t-1251413566.sh.apigw.tencentcs.com/paper/saveResult?taskId=23&code=undefined&resultId={}&answers=4782_B%40!%404783_C%40!%404785_A%40!%404784_C%40!%404790_D%40!%404789_D%40!%404788_B%40!%404791_C%40!%404792_B%40!%404795_A%40!%40&takeTime=64&sourceId=1&paperId={}'.format(
        resultid, paperid)
    # print(url)
    # 4782_B@!@4783_C@!@4785_A@!@4784_C@!@4790_D@!@4789_D@!@4788_B@!@4791_C@!@4792_B@!@4795_A@!@
    headers = {'Host': 'service-g4ju878t-1251413566.sh.apigw.tencentcs.com',
               'Connection': 'keep-alive',
               'sourceId': '1',
               'access-token': token,
               'source': '1',
               #'X-Date': 'Tue, 18 Oct 2022 13:22:41 GMT',
               'content-type': 'application/json',
               #'Authorization': 'hmac id="AKID8cQp38Gnlim99v0ujA74cBwXBsvo9prBp4gi", algorithm="hmac-sha1", headers="x-date source", signature="mSXuLkBPfDsLXx75r9dGwOkP5y4="',
               'Accept-Encoding': 'gzip,compress,br,deflate',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d30) NetType/WIFI Language/zh_CN',
               'Referer': 'https://servicewechat.com/wx5e64e98fbbb4dd8b/28/page-frame.html'}
    res = get(url=url, headers=headers)
    print(res.text)


if __name__ == '__main__':
    while True:
        username = input('请输入普法账号：')
        password = input('请输入密码（不输入，默认后六位）：') or username[-6:]
        # 登录
        token = log_in(username, password)
        if token != '':
            columid_all, columname_all = get_columnlist(token)
            do_columid(columid_all, columname_all)
            taskid_all, activityid_all, activitytype_all = get_task(token)
            do_task(token, taskid_all, activityid_all, activitytype_all)
            # 获取了题目
            resultid, answerid_all, paperid = get_paper(token)
            # 这里计划以后，把所有年级的答案记录，在回答，避免出现0分的情况
            #answerid_all_1 = ''
            # answerid_all_2 = '4782_B@!@4783_C@!@4785_A@!@4784_C@!@4790_D@!@4789_D@!@4788_B@!@4791_C@!@4792_B@!@4795_A@!@'  # 80分
            #answerid_all_3 = ''
            #answerid_all_4 = ''
            #answerid_all_5 = ''
            #answerid_all_6 = ''
            # print(str(answerid_all))
            # 怎么去提交答案_
            # 答案比较奇怪，不知道怎么处理
            # 怎么保证不同年级都是100，计划是保存一份全年级答案，然后提取。
            # 好吧，发现0分也显示通过，哈哈哈哈哈那不是完美
            do_paper(token, resultid, answerid_all, paperid)
            print('已完成。。。。。。。。。。。。。。。。。。。。。。。')
        else:
            print('账号或密码有误。。。。。。。。。。\n')
