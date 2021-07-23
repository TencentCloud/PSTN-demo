# -*- coding: utf-8 -*-
import time
import json
import urllib.request

'''
回拨呼叫请求
'''


def callback(host, appId, id, requestId, src, dst, srcDisplayNum, dstDisplayNum, record, maxAllowTime, bizId,
             statusFlag, statusUrl, hangupUrl, recordUrl, orderId, readPrompt, interruptPrompt, key, promptGender,
             repeatTimes, operate, keyPressUrl):
    # 请求Body,可按需删除选填参数
    jsonData = json.dumps({
        "appId": appId,
        "requestId": requestId,
        "src": src,
        "dst": dst,
        "srcDisplayNum": srcDisplayNum,
        "dstDisplayNum": dstDisplayNum,
        "record": record,
        "maxAllowTime": maxAllowTime,
        "bizId": bizId,
        "statusFlag": statusFlag,
        "statusUrl": statusUrl,
        "hangupUrl": hangupUrl,
        "recordUrl": recordUrl,
        "orderId": orderId,
        "preCallerHandle": {
            "readPrompt": readPrompt,
            "interruptPrompt": interruptPrompt,
            "keyList": [{
                "key": key,
                "operate": operate
            }],
            "repeatTimes": repeatTimes,
            "keyPressUrl": keyPressUrl,
            "promptGender": promptGender
        }
    }).encode('ascii')
    # 真实请求url
    realUrl = host + '/201511v3/callBack?id=' + id
    call_req(realUrl, jsonData)


'''
回拨呼叫取消
'''


def callCancel(host, appId, id, callId, cancelFlag):
    # 请求Body,可按需删除选填参数
    jsonData = json.dumps({
        "appId": appId,
        "callId": callId,
        "cancelFlag": cancelFlag
    }).encode('ascii')
    # 真实请求url
    realUrl = host + '/201511v3/callCancel?id=' + id
    call_req(realUrl, jsonData)


'''
回拨拉取话单
'''


def getCdr(host, appId, id, callId, src, startTimeStamp, endTimeStamp, compress):
    # 请求Body,可按需删除选填参数
    jsonData = json.dumps({
        "appId": appId,
        "src": src,
        #        "callId":callId,
        "startTimeStamp": startTimeStamp,
        "endTimeStamp": endTimeStamp,
        "compress": compress
    }).encode('ascii')
    # 真实请求url
    realUrl = host + '/201511v3/getCdr?id=' + id
    call_req(realUrl, jsonData)


def call_req(realUrl, jsonData):
    print('请求地址：' + realUrl)
    print('请求参数：' + jsonData.decode('utf-8'))
    # 请求方法为POST
    req = urllib.request.Request(url=realUrl, data=jsonData, method='POST')
    # 请求Headers参数
    req.add_header('Content-Type', 'application/json;charset=UTF-8')
    # 加入请求时间
    localtime = time.asctime(time.localtime(time.time()))
    # 转换年月日时分秒
    format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 打开本地文件
    fo = open('calllback_data.txt', 'a', encoding='utf-8')
    # 发送请求
    r = urllib.request.urlopen(req).read().decode('utf-8')
    print("++++++++++++++++++++响应参数+++++++++++++++++++")
    print(r)  # 打印响应结果
    print("数据已保存到calllback_data.txt，请注意查看信息")
    # 绑定请求参数记录到本地文件,方便定位问题
    fo.write("请求时间：" + format_time + '请求地址：' + realUrl + '\n' + '请求参数：' + jsonData.decode('utf-8') + '\n')
    fo.write('响应结果：' + str(r) + '\n')
    # 关闭文件
    fo.close()
