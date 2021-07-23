## 腾讯云号码保护

目前`腾讯云号码保护`为客户提供`回拨`、`中间号`等功能，腾讯云号码保护 python DEMO支持以下操作：

### 回拨

回拨支持操作：

- 回拨请求
- 回拨取消
- 拉取回拨话单


> `Note` 回拨回调请自行填写url，post接收json数据

### 中间号

中间号支持操作：

- 获取中间号
- 解绑中间号
- 拉取中间号话单


> `Note` 中间号回调请自行填写url，post接收json数据



## 开发

### 准备

在开始应用之前，需要准备如下信息:

- [x] 获取AppID和id

该数据是对接后腾讯云线下分配的，请自行保存好数据。

- [x] 白名单ip地址

准备需要进行调试的服务器ip，需要进行加入白名单配置后才可以调用测试使用。


## 安装
基于Python 3.7.0版本，要求Python 3.0及以上版本。

请自行下载安装Python 3.x，并完成环境配置。

打开命令行窗口，执行pip install requests命令。

执行pip list查看安装结果。

### 手动

1. 手动下载或clone最新版本demo代码
2. 直接调用app.py文件中对应try案例。
3. 请求格式：python app.py

## 用法
- **准备必要参数**
```python
host = 'https://test.pstn.avc.qcloud.com' #请求域名
appId ="66050"   #腾讯统一分配标识
id = "test"  #url后缀标识
```

- **获取中间号**
```python
try:
    src = "008612345678901" 
    dst = "008612345678902" 
    requestId = "1234567890qwrttyty" 
    record = "0" 
    cityId = ""
    bizId="test122"
#    accreditList=""
#    assignVirtualNum="008617080214571"  注意该字段如要带，必须填明细
    maxAssignTime = "300" 
    statusFlag = "16191" 
    statusUrl = 'http://statusUrl/callback' 
    hangupUrl = 'http://hangupUrl/callback' 
    recordUrl = 'http://recordUrl/callback'   
    npp_req.npp_getVirtualNum(host,appId,id,requestId,src,dst,'','',record,maxAssignTime,cityId,bizId,statusFlag,statusUrl,hangupUrl,recordUrl) #发送请求
except urllib.error.HTTPError as e:
        print(e.code)
        print('响应参数:'+e.read().decode('utf-8')) #打印错误信息
except urllib.error.URLError as e:
        print(e.reason)
```
> `Note`


- **解绑中间号**
```python
try:
    bindId="50e0ebf1-2bd4-4291-866f-98692d9d75ca"
    requestId="1234567890qwrttyty"
    bizId="test122"
    npp_req.npp_delVirtualNum(host,appId,id,requestId,bindId,bizId) #发送请求
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:'+e.read().decode('utf-8')) #打印错误信息
except urllib.error.URLError as e:
    print(e.reason)
```
> `Note` 

- **拉取中间号话单**
```python
try:
#    callId=""
    src=""
    startTimeStamp="1625382495"
    endTimeStamp="1625474549"
    compress="0"
    npp_req.npp_get400Cdr(host,appId,id,'',src,startTimeStamp,endTimeStamp,compress)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:'+e.read().decode('utf-8')) #打印错误信息
except urllib.error.URLError as e:
    print(e.reason)
```
> `Note`

- **回拨请求**
```python
try:
    requestId="123456"
    src="008612345678911"
    dst="008612345678912"
    srcDisplayNum="01067440253"
    dstDisplayNum=""
    record="1"
    maxAllowTime="30"
    bizId=""
    statusFlag="16191"
    statusUrl = 'http://statusUrl/callback' 
    hangupUrl = 'http://hangupUrl/callback' 
    recordUrl = 'http://recordUrl/callback'
    orderId=""
    #以下接口需配合按键才能完成，如不需要，请注释掉，转接录音可线下配置    
    readPrompt="您拨打的电话转接中"
    interruptPrompt="请按1"
    key="1"
    operate="1"
    repeatTimes="2"
    promptGender="1"
    keyPressUrl=""
    callback_req.callback(host,appId,id,requestId,src,dst,srcDisplayNum,dstDisplayNum,record,maxAllowTime,bizId,statusFlag,statusUrl,hangupUrl,recordUrl,orderId,readPrompt,interruptPrompt,key,promptGender,repeatTimes,operate,keyPressUrl)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:'+e.read().decode('utf-8')) #打印错误信息
except urllib.error.URLError as e:
    print(e.reason)
```
> `Note`

- **回拨取消**
```python
try:
    callId="12-210706-1eeb837c8c22222222222222d2"
    cancelFlag="0"
    callback_req.callCancel(host,appId,id,callId,cancelFlag)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:'+e.read().decode('utf-8')) #打印错误信息
except urllib.error.URLError as e:
    print(e.reason) 
```
> `Note`

- **拉取回拨话单**
```python
try:
#   callId=""
    src=""
    startTimeStamp="1625534014"
    endTimeStamp="1625537618"
    compress="0"
    callback_req.getCdr(host,appId,id,'',src,startTimeStamp,endTimeStamp,compress)
except urllib.error.HTTPError as e:
    print(e.code)
    print('响应参数:'+e.read().decode('utf-8')) #打印错误信息
except urllib.error.URLError as e:
    print(e.reason) 
```
> `Note`