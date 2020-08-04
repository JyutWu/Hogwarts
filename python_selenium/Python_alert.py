"""
弹框处理机制
在页面操作中有时会遇到JavaScript所生成的alert、confirm以及prompt弹框，可以使用
switch_to.alert()方法定位到。然后使用text/accept/dismiss/send_keys等方法进行操作。
分辨alert、window、div模态框:
1.alert，浏览器弹出框，一般是用来确认某些操作、输入简单的text或用户名、密码等，根据浏览器的不同，弹出框的样式也不一样，不过都是很简单的一个小框。在firebug中是无法获取到该框的元素的，也就是说alert是不属于网页DOM树的。如下图所示：

2.window，浏览器窗口，点击一个链接之后可能会打开一个新的浏览器窗口，跟之前的窗口是平行关系（alert跟窗口是父子关系，或者叫从属关系，alert必须依托于某一个窗口），有自己的地址栏、最大化、最小化按钮等。这个很容易分辨。

3.div伪装对话框，是通过网页元素伪装成对话框，这种对话框一般比较花哨，内容比较多，而且跟浏览器一看就不是一套，在网页中用firebug能够获取到其的元素


操作alert常用的方法：
1.switch_to.alert()：获取当前页面上的警告框。
2.text：返回alert/confirm/prompt中的文字信息。
3.accept()：接受现有警告框。
4.dismiss()：解散现有警告框。
5.send-keys(keysToSend)：发送文本至警告框。keysToSend:将文本发送至警告框。


"""
from time import sleep

from selenium.webdriver import ActionChains

from python_selenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)

        print(self.driver.switch_to_alert().text)
        self.driver.switch_to_alert().accept()
        sleep(3)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)

