# -*- coding: utf-8 -*-
import urllib.request
import npp_req
import callback_req

# 必填,请参考"开发准备"获取如下数据,替换为实际值
# 请求域名
host = 'https://test.pstn.avc.qcloud.com'
# 腾讯统一分配标识
appId = "66053"
# url后缀标识
id = "RQ"

'''
axb或xb绑定模式，各参数要求请参考"绑定接口文档"
* @param string requestId        session buffer，字符串最大长度不超过 42 字节，该 requestId 在后面回拨请求响应和回调中都会原样返回
* @param string src              主叫号码(号码前加 0086，如 008612345678911)，xb 模式下是不用填写该参数，axb 模式下是必选
* @param string dst              被叫号码(号码前加 0086，如 008612345678911)
* @param string assignVirtualNum  指定中间号，如果该中间号已被使用返回绑定失败，如果不带该字段由腾讯侧从号码池里自动分配
* param string  record           是否录音，0 表示不录音，1 表示录音。默认为不录音，注意如果需要录音回调，通话完成后需要等待一段时间，收到录音回调之后，再解绑中间号。
* param string  cityId           主被叫号码归属地，详见《腾讯-中间号-城市id.xlsx》
* param string  bizId            应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节,如果不带这个参数，请不要填
* param string  maxAssignTime    号码最大绑定时间，不填默认为 24 小时，最长绑定时间是168小时，单位秒
* param string  statusFlag       呼叫状态
* param string  statusUrl        请填写statusFlag并设置值，状态回调通知地址，正式环境可以配置默认推送地址
* param string  hangupUrl        话单回调通知地址，正式环境可以配置默认推送地址
* param string  recordUrl        录单 URL 回调通知地址，正式环境可以配置默认推送地址
* @return string              应答json字符串，详细内容参见腾讯云协议文档
'''

try:
    src = "008612345678901"
    dst = "008612345678902"
    requestId = "1234567890qwrttyty"
    record = "0"
    cityId = ""
    bizId = "test122"
    #    accreditList=""
    #    assignVirtualNum="008617080214571"
    maxAssignTime = "300"
    statusFlag = "16191"
    statusUrl = 'http://statusUrl/callback'
    hangupUrl = 'http://hangupUrl/callback'
    recordUrl = 'http://recordUrl/callback'
    npp_req.npp_getVirtualNum(host, appId, id, requestId, src, dst, '', '', record, maxAssignTime, cityId, bizId,
                              statusFlag, statusUrl, hangupUrl, recordUrl)  # 发送请求
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:' + e.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)

'''
axb或xb解绑模式，各参数要求请参考"解绑接口文档"
* @param string requestId        session buffer，字符串最大长度不超过 42 字节，该 requestId 在后面回拨请求响应和回调中都会原样返回
* @param string bizId            应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。
'''

try:
    bindId = "50e0ebf1-2bd4-4291-866f-98692d9d75ca"
    requestId = "1234567890qwrttyty"
    bizId = "test122"
    npp_req.npp_delVirtualNum(host, appId, id, requestId, bindId, bizId)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:' + e.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)

'''
拉取中间号话单，各参数要求请参考"接口文档"
* @param string callId        通话唯一标识 callId
* @param string src           查询主叫用户产生的呼叫话单，如填空表示拉取这个时间段所有话单，例"src"："" 注意src和callid不能共用发送
* @param string startTimeStamp 开始时间（时间戳格式）尽量填写近一天的
* @param string startTimeStamp 结束时间（时间戳格式）
* @param string compress       （0：不压缩 1：使用 zlib 压缩）默认不压缩
'''

try:
    #    callId=""
    src = ""
    startTimeStamp = "1625414895"
    endTimeStamp = "1625474549"
    compress = "0"
    npp_req.npp_get400Cdr(host, appId, id, '', src, startTimeStamp, endTimeStamp, compress)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:' + e.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)

'''
回拨外呼请求，各参数要求请参考"接口文档"
* @param string requestId        session buffer，字符串最大长度不超过 42 字节，该 requestId 在后面回拨请求响应和回调中都会原样返回
* @param string src              主叫号码(号码前加 0086，如 008613631686024)
* @param string dst              被叫号码(号码前加 0086，如 008613631686024)
* @param string srcDisplayNum    主叫显示系统分配的固话号码，如不填显示随机分配号码,案例01067440253
* @param string dstDisplayNum    被叫显示系统分配的固话号码，如不填显示随机分配号码，案例01067440253
* param string  record           是否录音，0 表示不录音，1 表示录音。默认为不录音
* param string  maxAllowTime     允许最大通话时间，不填默认为 30 分钟（单位：分钟)
* param string  bizId            应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节,如果不带这个参数，请不要填
* param string  statusFlag       呼叫状态
* param string  statusUrl        请填写statusFlag并设置值，状态回调通知地址，正式环境可以配置默认推送地址
* param string  hangupUrl        话单回调通知地址，正式环境可以配置默认推送地址
* param string  recordUrl        录单 URL 回调通知地址，正式环境可以配置默认推送地址
* param 结构体  preCallerHandle   结构体，主叫呼叫预处理操作，根据不同操作确认是不是呼通被叫等,需注意结构体是要配合按键支持播放使用，如果没有需求可以不用使用
* param string  readPrompt        呼叫主叫以后，给主叫用户的语音提示，播放该提示时用户所有按键无效
* param string  interruptPrompt   可中断提示，播放该提示时，用户可以按键
* param 结构体  keyList           对应按键操作,如果没有结构体里定义按键操作用户按键以后都从interruptPrompt 重新播放
* param string  repeatTimes       最多重复播放次数，超过该次数拆线
* param string  keyPressUrl       用户按键回调通知地址，如果为空不回调
* param string  promptGender      提示音男声女声：1 女声，2 男声。默认女声
* param string  key               用户按键（0-9、*、#、A-D)
* param string  operate           1: 呼通被叫 2：interruptPrompt 重播提示 3：拆线
* @return string              应答json字符串，详细内容参见腾讯云协议文档
'''

try:
    requestId = "123456"
    src = "008612345678911"
    dst = "008612345678912"
    srcDisplayNum = "01067440253"
    dstDisplayNum = ""
    record = "1"
    maxAllowTime = "30"
    bizId = ""
    statusFlag = "16191"
    statusUrl = 'http://statusUrl/callback'
    hangupUrl = 'http://hangupUrl/callback'
    recordUrl = 'http://recordUrl/callback'
    orderId = ""
    # 以下接口需配合按键才能完成，如不需要，请注释掉，转接录音可线下配置
    readPrompt = "您拨打的电话转接中"
    interruptPrompt = "请按1"
    key = "1"
    operate = "1"
    repeatTimes = "2"
    promptGender = "1"
    keyPressUrl = ""
    callback_req.callback(host, appId, id, requestId, src, dst, srcDisplayNum, dstDisplayNum, record, maxAllowTime,
                          bizId, statusFlag, statusUrl, hangupUrl, recordUrl, orderId, readPrompt, interruptPrompt, key,
                          promptGender, repeatTimes, operate, keyPressUrl)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:' + e.read().decode('utf-8'))  # 打印错误信息
except urllib.error.URLError as e:
    print(e.reason)

'''
回拨呼叫取消，各参数要求请参考"接口文档"
* @param string callId        回拨请求响应中返回的 callId
* @param string cancelFlag    0：不管通话状态直接拆线（默认) 1：主叫响铃以后状态不拆线 2：主叫接听以后状态不拆线 3：被叫响铃以后状态不拆线 4：被叫接听以后状态不拆线
'''

try:
    callId = "12-210706-12345678"
    cancelFlag = "0"
    callback_req.callCancel(host, appId, id, callId, cancelFlag)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:' + e.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)

'''
回拨拉取话单，各参数要求请参考"接口文档"
* @param string callId         回拨请求响应中返回的 callId，按 callId 查询该话单详细信息，填了该参数就不要填src
* @param string src            查询主叫用户产生的呼叫话单，如填空表示拉取这个时间段所有话单，例“src”：“”
* @param string startTimeStamp 开始时间（时间戳格式）
* @param string endTimeStamp   结束时间戳（时间戳格式）
* @param string compress       是否压缩（0：不压缩 1：使用 zlib 压缩）默认不压缩
'''

try:
    #   callId=""
    src = ""
    startTimeStamp = "1625534014"
    endTimeStamp = "1625537618"
    compress = "0"
    callback_req.getCdr(host, appId, id, '', src, startTimeStamp, endTimeStamp, compress)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:' + e.read().decode('utf-8'))  # 打印错误信息
except urllib.error.URLError as e:
    print(e.reason)
