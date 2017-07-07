<br>风速链项目目前具有以下功能：
<br>项目地址：https://github.com/zhangyancheng/selenium-git.git

<br>自动化执行
<br>1、根据页面编写自动化测试用例
<br>2、搭建自动化框架，对公共模块进行封装
<br>3、根据测试用例编写单步脚本，保证定位和流程正确
<br>4、使用PageObject模式来编写测试脚本，实现页面操作、定位、用例、测试数据的分离，提高代码维护性（以页面为单位）
<br>5、通过Jenkins+tomcat+git或svn持续集成平台，实现脚本的维护、构建控制
<br>6、输出报告并发送邮件

<br>使用说明:
<br>1、 在config.ini中配置项目路径：project_path
<br>2、 pictures  放置上传的图片
<br>3、 data/testadta  放置测试数据，如excel、text、xml
<br>4、 public/base.py  对webdriver进行了第二次的简单封装，使用更加方便（公共模块）
<br>5、 public/datainfo.py  可以对excel表进行数据读取，完成数据驱动
<br>6、 public/function.py  截图方法的封装
<br>7、 public/log.py  具有打印日志的功能，打印在控制台和文件中，日志保存在report/log/目录下
<br>8、 public/myunit.py  用例的初始化和结束方法的分钟
<br>9、 public/readconfig.py  读取配置文件（.ini文件）
<br>10、public/sendmail.py  具有发邮件的功能
<br>11、report  查看用例截图、日志、测试报告
<br>12、test_case/page_obj  使用pageobject，写page页面，在测试用例里面调用
<br>13、testcase目录  编写测试用例，可以分模块编写，建相应的目录
<br>14、执行run_ai_test.py  就可以执行所有的测试用例

<br>可以参考虫师的pyse,github地址:https://github.com/defnngj/pyse
<br>虫师的博客园地址：https://github.com/defnngj/pyse

<br>导入base文件
<br>import base
<br>1、启动浏览器：
<br>启动谷歌浏览器
<br>dr = PySelenium.PySelenium('chrom')
<br>启动远程浏览器比如使用grid施行分布式执行
<br>dr = PySelenium.PySelenium(RChrome','127.0.0.1:8080')
<br>2、在地址栏输入网址：
<br>dr.open('http://www.baidu.com')
<br>3、窗口最大化
<br>dr.max_window()
<br>4、设置浏览器的窗口的大小
<br>dr.set_window(800,500)
<br>5、不清除文本框的内容直接输入值(比如说：进行文件上传时，上传文件的路径，如果清除就会报错)：
<br>dr.type('id->su','小石头tester')
<br>6、先清除文本框的内容，然后再输入值（用得很多）：
<br>dr.clear_type('name->su','虫师')
<br>7、直接点击元素
<br>dr.click('css->#kw')
<br>8、右键点击元素：
<br>dr.right_click('id->kw')
<br>9、将鼠标移动到一个元素上
<br>dr.move_to_element('clas->btn1.btn-green.btn-search')
<br>10、双击元素
<br>dr.double_click("id->kw")
<br>11、将一个元素拖拽到另外一个元素上
<br>dr.drag_and_drop('id->kw1','id->kw2')
<br>12、根据连接的text来点击(<a href="http://www.baidu.com">百度</a>)
<br>dr.click_text('百度')
<br>13、关闭窗口，driver
<br>dr.quit()
<br>14、执行js脚本
<br>dr.js('script')
<br>15、获取元素的属性
<br>dr.get_attribute("id->su","href")
<br>16、获取元素的文本信息text
<br>dr.get_text('id->su')
<br>17、返回当前页面的title
<br>dr.get_title()
<br>18、返回当前页面的url
<br>dr.get_url()
<br>20、进入frame
<br>dr.switch_to_frame('id->kw')
<br>21、退出frame
<br>dr.switch_to_frame_out()
<br>22、判断元素是否存在
<br>dr.element_exist('id->kw')
<br>23、截图
<br>dr.take_screenshot('file_path')
<br>24、进入最新的table
<br>dr.into_new_window()
<br>25、输入内容并且回车
<br>dr.type_and_enter('id->kw')
<br>26、使用js来点击某个元素
<br>dr.js_click('id->kw')
<br>27、返回原生的webdriver，进行个性化需求
<br>dr.origin_driver()