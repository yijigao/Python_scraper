from scrapy import Selector
from pprint import pprint

html = """
<ul class="item_con_list" style="display: block;">
    
    <li class="con_list_item first_row default_list" data-index="0" data-positionid="4041848" data-salary="8k-15k" data-company="柏视医疗" data-positionname="数据分析师" data-companyid="216758" data-hrid="8244707" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/4041848.html" target="_blank" data-index="0" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0101
                    
                
                " data-lg-tj-cid="4041848" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>广州·广州大…</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">11:28发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image3/M00/04/1D/Cgq2xlpdyTaAGp1TAAAdLQoB6LA003.png">
                            <input type="hidden" class="hr_name" value="柏视HR">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="8244707">
                            <input type="hidden" class="target_position" value="4041848">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0101" data-lg-tj-cid="216758" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">8k-15k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/216758.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0101
                    
                
                " data-lg-tj-cid="216758" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">柏视医疗</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    医疗健康,数据服务 / A轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/216758.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0101
                    
                
                " data-lg-tj-cid="216758" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/04/1D/CgotOVnDYR2AZpurAAAUTmtyMew826.png" alt="柏视医疗" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>高级</span>
                    
                        <span>专员</span>
                    
                        <span>助理</span>
                    
                        <span>统计</span>
                    
                        <span>SPSS</span>
                    
                </div>
            
            <div class="li_b_r">“人工智能,高成长,顶级医院”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="1" data-positionid="3492524" data-salary="10k-20k" data-company="浙江执御信息技术有限公司" data-positionname="数据分析师" data-companyid="2380" data-hrid="8668269" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3492524.html" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0102
                    
                
                " data-lg-tj-cid="3492524" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>杭州·三墩</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">09:23发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="bart">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="8668269">
                            <input type="hidden" class="target_position" value="3492524">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0102" data-lg-tj-cid="2380" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/2380.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0102
                    
                
                " data-lg-tj-cid="2380" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">浙江执御信息技术有限公司</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,数据服务 / B轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/2380.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0102
                    
                
                " data-lg-tj-cid="2380" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/5E/25/Cgp3O1fqMFWAJ4hgAAAUycalP_8040.png" alt="浙江执御信息技术有限公司" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>移动互联网</span>
                    
                        <span>大数据</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>SPSS</span>
                    
                        <span>sas</span>
                    
                </div>
            
            <div class="li_b_r">“专业”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="2" data-positionid="1462646" data-salary="8k-16k" data-company="美图公司" data-positionname="数据分析师" data-companyid="23291" data-hrid="272753" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/1462646.html" target="_blank" data-index="2" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0103
                    
                
                " data-lg-tj-cid="1462646" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>厦门·软件园</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">21:48发布</span>
                    
                        
                            <input type="hidden" class="hr_portrait" value="image2/M00/1C/75/CgpzWlZhYdeASgWsAAAP_SFhRsQ946.jpg">
                            <input type="hidden" class="hr_name" value="美图HR">
                            <input type="hidden" class="hr_position" value="HR mm">
                            <input type="hidden" class="target_hr" value="272753">
                            <input type="hidden" class="target_position" value="1462646">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0103" data-lg-tj-cid="23291" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">8k-16k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/23291.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0103
                    
                
                " data-lg-tj-cid="23291" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">美图公司</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,硬件 / 上市公司
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/23291.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0103
                    
                
                " data-lg-tj-cid="23291" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/00/2D/Cgo8PFTUXHmAQ6K2AAA-xp7F-7c908.jpg" alt="美图公司" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>大数据</span>
                    
                </div>
            
            <div class="li_b_r">“10亿级用户 大牛级团队 火箭成长”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="3" data-positionid="3958252" data-salary="10k-20k" data-company="集奥聚合（GEO）" data-positionname="数据分析师" data-companyid="13179" data-hrid="7108579" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3958252.html" target="_blank" data-index="3" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0104
                    
                
                " data-lg-tj-cid="3958252" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>北京·东四</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">10:19发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image/M00/5A/4F/CgpFT1mMFHSAOpXkAAAnOYFHNF4708.jpg">
                            <input type="hidden" class="hr_name" value="seven">
                            <input type="hidden" class="hr_position" value="HRD">
                            <input type="hidden" class="target_hr" value="7108579">
                            <input type="hidden" class="target_position" value="3958252">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0104" data-lg-tj-cid="13179" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/13179.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0104
                    
                
                " data-lg-tj-cid="13179" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">集奥聚合（GEO）</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    数据服务 / B轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/13179.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0104
                    
                
                " data-lg-tj-cid="13179" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/36/1C/Cgp3O1dc_QaAM9JMAAAnLLKx_z4066.jpg" alt="集奥聚合（GEO）" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>大数据</span>
                    
                        <span>专员</span>
                    
                        <span>商业</span>
                    
                        <span>数据挖掘</span>
                    
                </div>
            
            <div class="li_b_r">“六险一金,年终奖,补助,学习型组织”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="4" data-positionid="2578005" data-salary="10k-20k" data-company="LinkDoc" data-positionname="数据分析师" data-companyid="113697" data-hrid="2146709" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/2578005.html" target="_blank" data-index="4" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0105
                    
                
                " data-lg-tj-cid="2578005" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>北京·中关村</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">16:12发布</span>
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image/M00/62/92/CgpEMlmVKdCAKqf2AABMMvP9gvo55.jpeg">
                            <input type="hidden" class="hr_name" value="零氪">
                            <input type="hidden" class="hr_position" value="HR">
                            <input type="hidden" class="target_hr" value="2146709">
                            <input type="hidden" class="target_position" value="2578005">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0105" data-lg-tj-cid="113697" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/113697.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0105
                    
                
                " data-lg-tj-cid="113697" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">LinkDoc</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    医疗健康,数据服务 / C轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/113697.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0105
                    
                
                " data-lg-tj-cid="113697" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/14/EA/CgqKkVbqZuiAaXaMAACL_mOdkj8983.JPG" alt="LinkDoc" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>SPSS</span>
                    
                        <span>数据管理</span>
                    
                </div>
            
            <div class="li_b_r">“技术挑战 医疗大数据平台 15薪”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="5" data-positionid="3794212" data-salary="8k-15k" data-company="E-jade" data-positionname="数据分析师" data-companyid="136248" data-hrid="5479303" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3794212.html" target="_blank" data-index="5" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0106
                    
                
                " data-lg-tj-cid="3794212" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>长沙·雨花区…</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">08:31发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="jobs">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="5479303">
                            <input type="hidden" class="target_position" value="3794212">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0106" data-lg-tj-cid="136248" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">8k-15k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/136248.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0106
                    
                
                " data-lg-tj-cid="136248" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">E-jade</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,游戏 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/136248.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0106
                    
                
                " data-lg-tj-cid="136248" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/BF/3E/Cgp3O1jPkCWAM47KAADX8tjahB8130.jpg" alt="E-jade" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>游戏</span>
                    
                        <span>大数据</span>
                    
                        <span>SPSS</span>
                    
                        <span>sas</span>
                    
                        <span>R</span>
                    
                </div>
            
            <div class="li_b_r">“偏外企管理,90后,出国培训,游戏”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="6" data-positionid="4065530" data-salary="10k-20k" data-company="中移在线服务有限公司" data-positionname="数据分析" data-companyid="57353" data-hrid="1522409" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/4065530.html" target="_blank" data-index="6" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0107
                    
                
                " data-lg-tj-cid="4065530" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析</h3>
                        
                            
                                
                                    
                                        <span class="add">[<em>郑州·高新区</em>]</span>
                                    
                                
                            
                        

                    </a>
                    <span class="format-time">09:13发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="image1/M00/19/71/CgYXBlUZADuALeRXAAAb1SlYYWI608.JPG">
                            <input type="hidden" class="hr_name" value="林行总">
                            <input type="hidden" class="hr_position" value="中移在线公司招聘主管">
                            <input type="hidden" class="target_hr" value="1522409">
                            <input type="hidden" class="target_position" value="4065530">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0107" data-lg-tj-cid="57353" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/57353.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0107
                    
                
                " data-lg-tj-cid="57353" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">中移在线服务有限公司</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/57353.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0107
                    
                
                " data-lg-tj-cid="57353" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/02/D4/CgqKkVad8jiAIDHrAAGK0MmIVNs370.jpg" alt="中移在线服务有限公司" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>教育</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>SPSS</span>
                    
                </div>
            
            <div class="li_b_r">“五险一金,企业年金,带薪年假,话费餐补”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="7" data-positionid="3908272" data-salary="10k-20k" data-company="浦和数据" data-positionname="数据分析师" data-companyid="166659" data-hrid="6788982" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3908272.html" target="_blank" data-index="7" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0108
                    
                
                " data-lg-tj-cid="3908272" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>南京·尧化</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">2018-02-01</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image/M00/77/75/CgpFT1pFmbeABchSAAJhQUg5SfA341.jpg">
                            <input type="hidden" class="hr_name" value="Luna">
                            <input type="hidden" class="hr_position" value="HR">
                            <input type="hidden" class="target_hr" value="6788982">
                            <input type="hidden" class="target_position" value="3908272">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0108" data-lg-tj-cid="166659" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验不限 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/166659.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0108
                    
                
                " data-lg-tj-cid="166659" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">浦和数据</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    数据服务 / 天使轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/166659.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0108
                    
                
                " data-lg-tj-cid="166659" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/1F/A5/CgoB5loNWG6AcJ7xAAJkPNosJTw590.jpg" alt="浦和数据" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>算法</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>机器学习</span>
                    
                        <span>深度学习</span>
                    
                        <span>人工智能</span>
                    
                </div>
            
            <div class="li_b_r">“五险一金,年终奖金,带薪年假,法定节假”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="8" data-positionid="3115854" data-salary="10k-20k" data-company="大圣live" data-positionname="数据分析" data-companyid="165926" data-hrid="6767593" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3115854.html" target="_blank" data-index="8" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0109
                    
                
                " data-lg-tj-cid="3115854" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析</h3>
                        
                            
                                
                                    <span class="add">[<em>广州·东风</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">18:52发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image/M00/73/9F/CgpFT1pAav2AfjE2AAErUMHCboI467.png">
                            <input type="hidden" class="hr_name" value="Lenka">
                            <input type="hidden" class="hr_position" value="HR">
                            <input type="hidden" class="target_hr" value="6767593">
                            <input type="hidden" class="target_position" value="3115854">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0109" data-lg-tj-cid="165926" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验不限 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/165926.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0109
                    
                
                " data-lg-tj-cid="165926" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">大圣live</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,游戏 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/165926.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0109
                    
                
                " data-lg-tj-cid="165926" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/23/5A/CgoB5loWpAOAPahwAAEv_0lY_9I240.png" alt="大圣live" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>业务运营</span>
                    
                        <span>大数据</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>SPSS</span>
                    
                        <span>数据管理</span>
                    
                </div>
            
            <div class="li_b_r">“鹅厂投资,大牛团队,优质项目,游戏直播”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="9" data-positionid="4084200" data-salary="10k-20k" data-company="极光" data-positionname="极光调研 - 数据分析师" data-companyid="917" data-hrid="2153176" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/4084200.html" target="_blank" data-index="9" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0110
                    
               
                " data-lg-tj-cid="4084200" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">极光调研 - 数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>深圳·南头</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">13:20发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image2/M00/0A/38/CgotOVncPOGAR2E7AABUArhVY0U298.jpg">
                            <input type="hidden" class="hr_name" value="Maggie">
                            <input type="hidden" class="hr_position" value="HRBP">
                            <input type="hidden" class="target_hr" value="2153176">
                            <input type="hidden" class="target_position" value="4084200">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0110" data-lg-tj-cid="917" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/917.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0110
                    
               
                " data-lg-tj-cid="917" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">极光</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,数据服务 / D轮及以上
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/917.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0110
                    
               
                " data-lg-tj-cid="917" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/37/20/CgqKkVdfms6Ac6dNAABY3gBvuqI944.jpg" alt="极光" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>中级</span>
                    
                        <span>算法</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>机器学习</span>
                    
                        <span>大数据</span>
                    
                </div>
            
            <div class="li_b_r">“业界第一,14薪+,牛逼团队,D轮+”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="10" data-positionid="3323087" data-salary="10k-20k" data-company="广州银行信用卡中心" data-positionname="数据分析师" data-companyid="199056" data-hrid="8402527" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3323087.html" target="_blank" data-index="10" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0111
                    
               
                " data-lg-tj-cid="3323087" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>广州·天河城</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">09:20发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="陈子琳">
                            <input type="hidden" class="hr_position" value="数据运营岗">
                            <input type="hidden" class="target_hr" value="8402527">
                            <input type="hidden" class="target_position" value="3323087">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0111" data-lg-tj-cid="199056" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/199056.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0111
                    
               
                " data-lg-tj-cid="199056" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">广州银行信用卡中心</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    金融 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/199056.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0111
                    
               
                " data-lg-tj-cid="199056" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/1A/3C/CgpFT1kH3Y-ASlZEAADZ9PulO7M328.png" alt="广州银行信用卡中心" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>算法</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>机器学习</span>
                    
                        <span>深度学习</span>
                    
                        <span>大数据</span>
                    
                </div>
            
            <div class="li_b_r">“大数据,互联网金融,金融科技,机器学习”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="11" data-positionid="4001717" data-salary="8k-15k" data-company="博悦科创" data-positionname="急聘数据分析" data-companyid="117217" data-hrid="9637977" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/4001717.html" target="_blank" data-index="11" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0112
                    
               
                " data-lg-tj-cid="4001717" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">急聘数据分析</h3>
                        
                            
                                
                                    <span class="add">[<em>深圳·购物公…</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">16:49发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image2/M00/37/ED/CgoB5lpLW4uAKX6SAAEJCo3pzQs484.jpg">
                            <input type="hidden" class="hr_name" value="何小姐">
                            <input type="hidden" class="hr_position" value="招聘专员">
                            <input type="hidden" class="target_hr" value="9637977">
                            <input type="hidden" class="target_position" value="4001717">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0112" data-lg-tj-cid="117217" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">8k-15k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/117217.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0112
                    
               
                " data-lg-tj-cid="117217" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">博悦科创</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/117217.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0112
                    
               
                " data-lg-tj-cid="117217" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/10/8F/CgqKkVbf8TKACeAMAAAop3DnaW4486.png" alt="博悦科创" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>大数据</span>
                    
                        <span>数据挖掘</span>
                    
                        <span>建模</span>
                    
                </div>
            
            <div class="li_b_r">“福利待遇好，发展空间大”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="12" data-positionid="3019985" data-salary="10k-20k" data-company="广州棒谷科技股份有限公司" data-positionname="大数据分析师" data-companyid="20473" data-hrid="181231" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3019985.html" target="_blank" data-index="12" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0113
                    
               
                " data-lg-tj-cid="3019985" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">大数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>广州·白云大…</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">17:24发布</span>
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image/M00/10/B0/CgpFT1jxhMCAXsJHAAB_GDt2Cvk071.jpg">
                            <input type="hidden" class="hr_name" value="aiko">
                            <input type="hidden" class="hr_position" value="大数据人工智能HRBP">
                            <input type="hidden" class="target_hr" value="181231">
                            <input type="hidden" class="target_position" value="3019985">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0113" data-lg-tj-cid="20473" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/20473.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0113
                    
               
                " data-lg-tj-cid="20473" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">广州棒谷科技股份有限公司</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    电子商务 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/20473.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0113
                    
               
                " data-lg-tj-cid="20473" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/01/11/CgotOVm-PqeAffsOAAEGuZjfXlw785.jpg" alt="广州棒谷科技股份有限公司" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>电商</span>
                    
                        <span>SPSS</span>
                    
                </div>
            
            <div class="li_b_r">“海量数据,人工智能,高学历团队”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="13" data-positionid="4083879" data-salary="10k-20k" data-company="河狸家" data-positionname="数据分析J10298" data-companyid="135258" data-hrid="4134361" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/4083879.html" target="_blank" data-index="13" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0114
                    
               
                " data-lg-tj-cid="4083879" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析J10298</h3>
                        
                            
                                
                                    
                                        <span class="add">[<em>北京·朝阳区</em>]</span>
                                    
                                
                            
                        

                    </a>
                    <span class="format-time">17:46发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image/M00/7F/65/CgpFT1pVleSAT9CxAADLS_P-K8U976.jpg">
                            <input type="hidden" class="hr_name" value="小河狸">
                            <input type="hidden" class="hr_position" value="总部HR">
                            <input type="hidden" class="target_hr" value="4134361">
                            <input type="hidden" class="target_position" value="4083879">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0114" data-lg-tj-cid="135258" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/135258.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0114
                    
               
                " data-lg-tj-cid="135258" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">河狸家</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,O2O / C轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/135258.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0114
                    
               
                " data-lg-tj-cid="135258" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/39/C3/Cgp3O1dntLKAKb3dAADLS_P-K8U683.jpg" alt="河狸家" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>电商</span>
                    
                        <span>运营</span>
                    
                        <span>BI</span>
                    
                </div>
            
            <div class="li_b_r">“提供午餐；五险一金；临近地铁；氛围好”</div>
        </div>
    </li>
    
    
    
    <li class="con_list_item default_list" data-index="14" data-positionid="3795960" data-salary="6k-12k" data-company="普强信息" data-positionname="数据分析师" data-companyid="48188" data-hrid="9291112" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3795960.html" target="_blank" data-index="14" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0115
                    
               
                " data-lg-tj-cid="3795960" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">
                        <h3 style="max-width: 180px;">数据分析师</h3>
                        
                            
                                
                                    <span class="add">[<em>北京·西北旺</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">17:39发布</span>
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                            <input type="hidden" class="hr_portrait" value="i/image2/M00/1B/0E/CgoB5loCXcyABK2OAABQkJlWUXs843.png">
                            <input type="hidden" class="hr_name" value="liusha">
                            <input type="hidden" class="hr_position" value="人事专员">
                            <input type="hidden" class="target_hr" value="9291112">
                            <input type="hidden" class="target_position" value="3795960">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0115" data-lg-tj-cid="48188" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">6k-12k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/48188.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0115
                    
               
                " data-lg-tj-cid="48188" data-lg-tj-abt="dm-csearch-useUserAllInterest|1">普强信息</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    数据服务 / C轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/48188.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                
                    
                    0115
                    
               
                " data-lg-tj-cid="48188" data-lg-tj-abt="dm-csearch-useUserAllInterest|1"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/02/5D/CgqKkVaNBY6AdaOaAAASNGYxiz4616.jpg" alt="普强信息" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>建模</span>
                    
                        <span>系统分析</span>
                    
                        <span>数学专业</span>
                    
                        <span>统计学专业</span>
                    
                </div>
            
            <div class="li_b_r">“项目奖,弹性工作,下午茶,年度旅游”</div>
        </div>
    </li>
    
    </ul>
"""
print(Selector(text=html).xpath('//@data-positionid').extract())