from pprint import pprint

from scrapy.selector import Selector

html = """
			<div class="day7">
				<ul class="week">
											<li><b>01月17日</b><span>星期三</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b0.png"></li>
											<li><b>01月18日</b><span>星期四</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b0.png"></li>
											<li><b>01月19日</b><span>星期五</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b1.png"></li>
											<li><b>01月20日</b><span>星期六</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b2.png"></li>
											<li><b>01月21日</b><span>星期日</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b1.png"></li>
											<li><b>01月22日</b><span>星期一</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b2.png"></li>
											<li><b>01月23日</b><span>星期二</span><img src="http://pic9.tianqijun.com/static/wap2018/ico1/b2.png"></li>
									</ul>
				<ul class="txt txt2">
											<li>晴</li>
											<li>晴</li>
											<li>多云</li>
											<li>阴</li>
											<li>多云</li>
											<li>阴</li>
											<li>阴</li>
									</ul>
				<div class="zxt_shuju" style="display: none;">
				<ul>
											<li><span>12</span><b>0</b></li>
											<li><span>11</span><b>4</b></li>
											<li><span>13</span><b>4</b></li>
											<li><span>11</span><b>6</b></li>
											<li><span>16</span><b>6</b></li>
											<li><span>11</span><b>6</b></li>
											<li><span>10</span><b>7</b></li>
									</ul>
				</div>
				<canvas id="canvas"></canvas>
				<script type="text/javascript" src="//pic9.tianqijun.com/static/js/canvas.js"></script>
				<ul class="txt">
											<li>西北风</li>
											<li>北风</li>
											<li>北风</li>
											<li>西北风</li>
											<li>西北风</li>
											<li>北风</li>
											<li>北风</li>
									</ul>			
			</div>

"""
# print(Selector(text=html).xpath('//ul[@class="week"]/li/img/@src').extract()[0])
print(Selector(text=html).xpath('//div[@class="zxt_shuju"]/ul/li/b/text()').extract())


# print("如果我们要采集第一个class的内容：")
# first_class = Selector(text=html).xpath('/html/body/class[1]').extract()
# # pprint(first_class)
#
# pprint('如果我们要采集最后一个class的内容:')
# last_class = Selector(text=html).xpath('/html/body/class[last()]').extract()
# # pprint(last_class)
#
# pprint('如果我们要采集最后一个class中name属性的文本：')
# last_class_name = Selector(text=html).xpath('/html/body/class[last()]/name/text()').extract()
# # pprint(last_class_name)
#
# pprint("下面展示Xpath的嵌套使用")
# subbody = Selector(text=html).xpath('/html/body/class[2]').extract()
# pprint(Selector(text=subbody[0]).xpath('//name/text()').extract())
# print(Selector(text=subbody[0]).xpath('//class/name/text()').extract()[0])
# print(Selector(text=subbody[0]).xpath('//class/sex/text()').extract())
