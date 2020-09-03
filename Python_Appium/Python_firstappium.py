from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platformVersion": "6.0",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".common.MainActivity",
    "noReset": True,  # 保留上次操作痕迹（比如登录状态）
    "dontStopAppOnReset": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
# els1 = driver.find_elements_by_id("com.xueqiu.android:id/home_search")
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath("/ hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / "
                                   "android.widget.LinearLayout / android.widget.FrameLayout / android.view.ViewGroup "
                                   "/ android.widget.FrameLayout / android.widget.LinearLayout / "
                                   "android.widget.RelativeLayout / android.widget.FrameLayout / "
                                   "android.widget.LinearLayout / androidx.recyclerview.widget.RecyclerView "
                                   "/android.widget.RelativeLayout[1]")
el3.click()

driver.back()  # 当你从一个父页面跳转到子页面进行操作，操作完之后没有“返回”之类的按钮或链接，重新进入父页面又很麻烦，back()可以帮你
