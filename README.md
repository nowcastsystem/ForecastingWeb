# How to run the Timeseries UI backend
use conda to create a new env with python >= 3.6 and activate

pip install https://github.com/yutiansut/tornado_http2/archive/master.zip
pip install tornado==5.1.1

cd ForecastingQA
python setup.py install --force

cd TimeseriesForcastingBackend
python setup.py install --force

pip install xgboost

sudo mongod #before this step, make sure you have mongoDB installed

quantaxis_webserver



# QUANTAXIS_WEBSERVER
quantaxis_webserver


QUANTAXIS的持久化及后端解决方案

```
给了一个demo:  地址  www.yutiansut.com:8010
当前服务器部署版本: 1.3.4

```

## install
```
pip install https://github.com/yutiansut/tornado_http2/archive/master.zip
pip install tornado==5.1.1
pip install quantaxis_webserver
```

## 运行

```
命令行输入：

quantaxis_webserver

```

## API


api参见: [backend_api](./backendapi.md)

## CHANGELOG
- 1.0 版本  基于原有quantaxisd的功能做移植

- 1.1 

    - 增加http2支持
    - [] 增加tls, ssl支持

    - 一个完备的websocket通讯/交易机制
    
- 1.3.3 
    - 增加windows服务(QUANTAXIS_Webservice)
    - 对应qadesktop 0.0.7 版本

- 1.3.4
    - 改用websocket+ json 的模式进行cs通信
    - 对应qadesktop 0.0.8 版本
    
- 1.3.5
    - 增加 USERHandler模型, 对应1.2.8+ 的quantaxis QA_USER

- 1.3.6
    - 部分bug修复/ 对QAUSER的进一步适配

- 1.3.7
    - 随着QAARP模块的完善和修改, QAWEBSERVER需要完整实现QAARP的功能
    - 支持双登陆模式(model: wechat/password)
    - TODO: 交易监控
