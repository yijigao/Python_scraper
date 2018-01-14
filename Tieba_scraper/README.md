# 使用BeautifulSoup 爬取贴吧页面主题信息

## 1. 目标
爬取wp7吧目前页面的主题信息，将标题、发帖人、日期、回复数量、链接保存文本

## 2. 步骤
	1. 分析地址
		* 贴吧地址：http://tieba.baidu.com/f?kw=wp7&ie=utf-8&pn=0#
		* 页面采用utf-8编码
		* 每次翻页地址后面的“pn”加50
	2. 使用浏览器开发者模式分析Html
		* 每个帖子内容包裹在<li class=" j_thread_list clearfix">
		* 关注上面的信息，找到需要信息所在的class

## 有哪些坑？
	* 开始用soup扒帖子信息时发现没内容，检查发现" j_thread_list clearfix"前面有个空格...后续还是直接复制好了
	* 装填txt时，得到的内容乱码，后面加上encodind='utf-8'解决
		```
	    with open('TB.txt', 'a+', encoding='utf-8') as f:
	        for comment in dict:
	            f.write('标题:{} \t 链接:{} \t 发帖人:{} \t 发帖时间:{} \t 回复数量:{} \n'
	                    .format(comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
	        print("当前页面爬取完成！")
        	f.close()
		```

