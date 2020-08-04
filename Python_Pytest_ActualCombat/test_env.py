# 测试用例通过传入 fixture方法获取 测试数据/开发数据
#场景1：根据需求，通过执行不同的自定义参数去获取不同的数据，比如用测试环境或者开发环境的数据去执行测试用例，用一个方法去处理自定义参数执行后的结果，提供给后续的测试用例使用
def test_case(cmdoption):
    print('测试环境验证')
    env,datas = cmdoption
    print(f'环境：{env},环境信息：{datas}')
    ip = datas['env']['ip']
    port= datas['env']['port']
    url = 'http://'+ip+':'+port
    print(url)