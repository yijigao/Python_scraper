# 1.项目背景
爬取拉勾网关于数据分析岗位的数据，分析数据分析岗位目前的现状（地域，薪资，岗位要求）

# 2.使用Scrapy框架爬取数据
    ## 2.1 初次思路
    分析网站主页面的HTML源码，找到需要的变量的位置，提取，将数据写入文本
    1.首页地址为https://www.lagou.com
    2.搜索数据分析，地址转为https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=可以看到字段位置
    3.点开招聘页详情，地址转为https://www.lagou.com/jobs/4041848.html，拉勾为每个公司招聘页准备了一个代码，如上面的4041848
    4.这个代码在招聘页的源码中的```<input type="hidden" class="target_position" value="4041848">```找到
    5.需要的内容都在招聘详情页
    ```
    <title>数据分析师招聘-柏视医疗招聘-拉勾网</title>
    <!-- 页面主体START -->
    <div class="position-head" data-companyid="216758">
    <div class="position-content ">
        <div class="position-content-l">
            <div class="job-name" title="数据分析师">
                                <div class="company">柏视医疗医学部招聘</div>
                                <span class="name">数据分析师</span>
                                <div class="marEdit">
                                    </div>
            </div>
            <dd class="job_request">
                <p>
                    <span class="salary">8k-15k </span>
                    <span>/广州 /</span>
                    <span>经验1-3年 /</span>
                    <span>本科及以上 /</span>
                    <span>全职</span>
                </p>
                <!-- 职位标签 -->
                <ul class="position-label clearfix">
                                        <li class="labels">高级</li>
                                        <li class="labels">数据分析</li>
                                        <li class="labels">SPSS</li>
                                        <li class="labels">统计</li>
                                        <li class="labels">专员</li>
                                        <li class="labels">助理</li>
                                    </ul>
                <p class="publish_time">11:28&nbsp; 发布于拉勾网</p>
            </dd>
        </div>```
    职位详情包裹在<dd class="job_bt"> <div>
        <p>岗位职责：</p>
        <p>1、参与合作医院的研究项目的方案设计</p>
        <p>2、完成合作医院研究项目的数据分析工作并撰写统计分析报告</p>
        <p>3、为其他部门提供统计分析支持</p>
        <p><br></p>
        <p>岗位要求：</p>
        <p>1、优秀的执行能力和学习能力</p>
        <p>2、拥有良好的沟通技巧和团队合作精神，较强的责任感和进取精神</p>
        <p>3、熟悉R、SAS、SPSS等软件的使用</p>
        <p>4、统计学、生物统计、生物医学等相关背景优先</p>
        <p><br></p>
        <p>*可以接受兼职</p>
                </div></dd>```
    ## 2.1 尝试编写代码
    1. 首先编写items,将希望获取的字段填写进去
    