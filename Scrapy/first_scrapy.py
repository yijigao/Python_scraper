from scrapy.selector import Selector
from pprint import pprint

html = """
<html>
    <body>
        <class>
            <name>王尼玛</name>
            <sex>男</sex>
            <age>80</age>
            <favouite>开车</favouite>
        </class>
        <class>
            <name>陈一发</name>
            <sex>母</sex>
            <age>28</age>
            <favouite>开che</favouite>
        </class>
        <class>
            <name>狗贼叔叔</name>
            <sex>公</sex>
            <age>18</age>
            <favouite>土豪战</favouite>
        </class>
    </body>
</html>
"""

print("如果我们要采集第一个class的内容：")
first_class = Selector(text=html).xpath('/html/body/class[1]').extract()
# pprint(first_class)

pprint('如果我们要采集最后一个class的内容:')
last_class = Selector(text=html).xpath('/html/body/class[last()]').extract()
# pprint(last_class)

pprint('如果我们要采集最后一个class中name属性的文本：')
last_class_name = Selector(text=html).xpath('/html/body/class[last()]/name/text()').extract()
# pprint(last_class_name)

pprint("下面展示Xpath的嵌套使用")
subbody = Selector(text=html).xpath('/html/body/class[2]').extract()
pprint(Selector(text=subbody[0]).xpath('//name/text()').extract())
print(Selector(text=subbody[0]).xpath('//class/name/text()').extract()[0])
print(Selector(text=subbody[0]).xpath('//class/sex/text()').extract())

