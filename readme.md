<br>��������ĿĿǰ�������¹��ܣ�
<br>��Ŀ��ַ��https://github.com/zhangyancheng/selenium-git.git

<br>�Զ���ִ��
<br>1������ҳ���д�Զ�����������
<br>2����Զ�����ܣ��Թ���ģ����з�װ
<br>3�����ݲ���������д�����ű�����֤��λ��������ȷ
<br>4��ʹ��PageObjectģʽ����д���Խű���ʵ��ҳ���������λ���������������ݵķ��룬��ߴ���ά���ԣ���ҳ��Ϊ��λ��
<br>5��ͨ��Jenkins+tomcat+git��svn��������ƽ̨��ʵ�ֽű���ά������������
<br>6��������沢�����ʼ�

<br>ʹ��˵��:
<br>1�� ��config.ini��������Ŀ·����project_path
<br>2�� pictures  �����ϴ���ͼƬ
<br>3�� data/testadta  ���ò������ݣ���excel��text��xml
<br>4�� public/base.py  ��webdriver�����˵ڶ��εļ򵥷�װ��ʹ�ø��ӷ��㣨����ģ�飩
<br>5�� public/datainfo.py  ���Զ�excel��������ݶ�ȡ�������������
<br>6�� public/function.py  ��ͼ�����ķ�װ
<br>7�� public/log.py  ���д�ӡ��־�Ĺ��ܣ���ӡ�ڿ���̨���ļ��У���־������report/log/Ŀ¼��
<br>8�� public/myunit.py  �����ĳ�ʼ���ͽ��������ķ���
<br>9�� public/readconfig.py  ��ȡ�����ļ���.ini�ļ���
<br>10��public/sendmail.py  ���з��ʼ��Ĺ���
<br>11��report  �鿴������ͼ����־�����Ա���
<br>12��test_case/page_obj  ʹ��pageobject��дpageҳ�棬�ڲ��������������
<br>13��testcaseĿ¼  ��д�������������Է�ģ���д������Ӧ��Ŀ¼
<br>14��ִ��run_ai_test.py  �Ϳ���ִ�����еĲ�������

<br>���Բο���ʦ��pyse,github��ַ:https://github.com/defnngj/pyse
<br>��ʦ�Ĳ���԰��ַ��https://github.com/defnngj/pyse

<br>����base�ļ�
<br>import base
<br>1�������������
<br>�����ȸ������
<br>dr = PySelenium.PySelenium('chrom')
<br>����Զ�����������ʹ��gridʩ�зֲ�ʽִ��
<br>dr = PySelenium.PySelenium(RChrome','127.0.0.1:8080')
<br>2���ڵ�ַ��������ַ��
<br>dr.open('http://www.baidu.com')
<br>3���������
<br>dr.max_window()
<br>4������������Ĵ��ڵĴ�С
<br>dr.set_window(800,500)
<br>5��������ı��������ֱ������ֵ(����˵�������ļ��ϴ�ʱ���ϴ��ļ���·�����������ͻᱨ��)��
<br>dr.type('id->su','Сʯͷtester')
<br>6��������ı�������ݣ�Ȼ��������ֵ���õúࣩܶ��
<br>dr.clear_type('name->su','��ʦ')
<br>7��ֱ�ӵ��Ԫ��
<br>dr.click('css->#kw')
<br>8���Ҽ����Ԫ�أ�
<br>dr.right_click('id->kw')
<br>9��������ƶ���һ��Ԫ����
<br>dr.move_to_element('clas->btn1.btn-green.btn-search')
<br>10��˫��Ԫ��
<br>dr.double_click("id->kw")
<br>11����һ��Ԫ����ק������һ��Ԫ����
<br>dr.drag_and_drop('id->kw1','id->kw2')
<br>12���������ӵ�text�����(<a href="http://www.baidu.com">�ٶ�</a>)
<br>dr.click_text('�ٶ�')
<br>13���رմ��ڣ�driver
<br>dr.quit()
<br>14��ִ��js�ű�
<br>dr.js('script')
<br>15����ȡԪ�ص�����
<br>dr.get_attribute("id->su","href")
<br>16����ȡԪ�ص��ı���Ϣtext
<br>dr.get_text('id->su')
<br>17�����ص�ǰҳ���title
<br>dr.get_title()
<br>18�����ص�ǰҳ���url
<br>dr.get_url()
<br>20������frame
<br>dr.switch_to_frame('id->kw')
<br>21���˳�frame
<br>dr.switch_to_frame_out()
<br>22���ж�Ԫ���Ƿ����
<br>dr.element_exist('id->kw')
<br>23����ͼ
<br>dr.take_screenshot('file_path')
<br>24���������µ�table
<br>dr.into_new_window()
<br>25���������ݲ��һس�
<br>dr.type_and_enter('id->kw')
<br>26��ʹ��js�����ĳ��Ԫ��
<br>dr.js_click('id->kw')
<br>27������ԭ����webdriver�����и��Ի�����
<br>dr.origin_driver()