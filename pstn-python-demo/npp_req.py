# -*- coding: utf-8 -*-
import json
import urllib.request
import time
'''
axb或xb绑定结构体
'''


def npp_getVirtualNum(host, appId, id, requestId, src, dst, accreditList, assignVirtualNum, record, maxAssignTime,
                      cityId, bizId, statusFlag, statusUrl, hangupUrl, recordUrl):
    # 请求Body,可按需删除选填参数
    jsonData = json.dumps({
        "appId": appId,
        "requestId": requestId,
        "src": src,
        "dst": dst,
        #        "accreditList":accreditList,
        #        "assignVirtualNum":assignVirtualNum,
        "record": record,
        "maxAssignTime": maxAssignTime,
        "cityId": cityId,
        "bizId": bizId,
        "statusFlag": statusFlag,
        "statusUrl": statusUrl,
        "hangupUrl": hangupUrl,
        "recordUrl": recordUrl
    }).encode('ascii')
    # 真实请求url
    realUrl = host + '/201511v3/getVirtualNum?id=' + id
    req(realUrl, jsonData)


'''
axb或xb解绑结构体
'''


def npp_delVirtualNum(host, appId, id, requestId, bindId, bizId):
    # 请求Body,可按需删除选填参数
    jsonData = json.dumps({
        "appId": appId,
        "requestId": requestId,
        "bindId": bindId,
        "bizId": bizId
    }).encode('ascii')
    # 真实请求url
    realUrl = host + '/201511v3/delVirtualNum?id=' + id
    req(realUrl, jsonData)


'''
axb或xb拉取话单结构体
'''


def npp_get400Cdr(host, appId, id, callId, src, startTimeStamp, endTimeStamp, compress):
    # 请求Body,可按需删除选填参数
    jsonData = json.dumps({
        "appId": appId,
        #        "callId":callId,
        "src": src,
        "startTimeStamp": startTimeStamp,
        "endTimeStamp": endTimeStamp,
        "compress": compress
    }).encode('ascii')
    # 真实请求url
    realUrl = host + '/201511v3/get400Cdr?id=' + id
    req(realUrl, jsonData)


def req(realUrl, jsonData):
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
    fo = open('npp_data.txt', 'a', encoding='utf-8')
    # 发送请求
    r = urllib.request.urlopen(req).read().decode('utf-8')
    print("++++++++++++++++++++响应参数+++++++++++++++++++")
    print(r)  # 打印响应结果
    print("数据已保存到npp_data.txt，请注意查看信息")
    # 绑定请求参数记录到本地文件,方便定位问题
    fo.write('请求时间:' + format_time + '请求地址：' + realUrl + '\n' + '请求参数：' + jsonData.decode('utf-8') + '\n')
    fo.write('响应结果：' + str(r) + '\n')
    # 关闭文件
    fo.close()
