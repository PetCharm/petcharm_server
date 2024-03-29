# PetCharm-Server

## API Document

http://petcharm.mcac.cc/doc/

## Environment

- CentOS 7.9.2009 x86_64
- Mysql Server 5.7.37
- Python 3.9.7
- Django 3.2.9
- Nginx 1.20.2


Python库见requirements


## ER

![petcharm](https://user-images.githubusercontent.com/59144459/171667212-65e6c7a8-4647-429e-b024-4b803c838633.png)


## Files

| 目录 | 文件名 | 功能 |
| ---- | ------ | ---- |
|myapp |  views.py   |视图  |
|myapp  |admin.py |  管理员视图  |
|myapp  |image.py  | 上传图片相关  |
|myapp | models.py  |模型文件  |
|myapp | infos.py  | 接口返回信息序列化  |
|myapp  |openIM.py | openIM后端实现  |
|myapp  |predict.py| 预测相关  |
|myapp | verification.py  |  验证码相关  |
|myapp  |tests.py |  测试文件  |
|myapp  |serializers.py| 序列化相关  |
|myapp/migrations |     数据库迁移文件  |
|bert_model |  | NLP机器学习相关  
|back |  settings.py  |  Django设置  
|back |  urls.py  |  API url相关  
|back   |wsgi.py  |  uwsgi配置相关  
|static/admin      | |管理端静态页面  
|static/def-yasg|    |   swagger静态页面  
|static/rest_framework  |  | REST框架静态页面  
|根目录  |  tools.py   |数据表转换工具代码  
|根目录  |  uwsgi.ini  |uwsgi配置文件  
|根目录   | manage.py  |Django自带管理工具入口  
|根目录  |  requirements.txt  | 需要的pip软件包  
|根目录   | README.md | readme文件|


## Models

| | | | | |
|-|-|-|-|-|
|0|1|2|3|4|
|Comment(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|comment_id|comment id|int|not null| |
|comment_content|comment content|varchar(500)| | |
|comment_post|comment post| | |外键, 和myapp包下的Post是many_to_one关系|
|comment_user|comment user| | |外键, 和myapp包下的User是many_to_one关系|
| | | | | |
| | | | | |
|Hospital(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|hospital_id|hospital id|int|not null| |
|hospital_name|hospital name|varchar(100)| | |
| | | | | |
| | | | | |
|Pet(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|pet_id|pet id|int|not null| |
|pet_name|pet name|varchar(100)| | |
|pet_type|pet type|varchar(100)| | |
|pet_breed|pet breed|varchar(100)| | |
|pet_gender|pet gender|varchar(100)| | |
|pet_date_of_birth|pet date of birth|datetime| | |
|pet_registration_number|pet registration number|varchar(100)| | |
| | | | | |
| | | | | |
|Post(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|post_id|post id|int|not null| |
|post_content|post content|varchar(500)| | |
|post_user|post user| | |外键, 和myapp包下的User是many_to_one关系|
|post_date|post date|datetime| | |
|post_cover|post cover|varchar(500)| | |
| | | | | |
| | | | | |
|Rating(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|rating_id|rating id|int|not null| |
|rating_content|rating content|varchar(200)| | |
|rating_score|rating score|int| | |
|rating_user|rating user| | |外键, 和myapp包下的User是many_to_one关系|
|rating_by_user|rating by user| | |外键, 和myapp包下的User是many_to_one关系|
| | | | | |
| | | | | |
|Service(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|service_id|service id|int|not null| |
|service_name|service name|varchar(100)| | |
|service_content|service content|varchar(500)| | |
|service_price|service price|decimal| | |
|service_type|service type|varchar(100)| | |
|service_user|service user| | |外键, 和myapp包下的User是many_to_one关系|
| | | | | |
| | | | | |
|Star(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|star_id|star id|int|not null| |
|star_user|star user| | |外键, 和myapp包下的User是many_to_one关系|
|star_by_user|star by user| | |外键, 和myapp包下的User是many_to_one关系|
| | | | | |
| | | | | |
|User(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|password|密码|varchar(128)|not null| |
|last_login|上次登录|datetime| | |
|is_superuser|超级用户状态|bool|not null|默认值为: False|
|username|用户名|varchar(150)|not null|唯一|
|first_name|名字|varchar(150)|not null| |
|last_name|姓氏|varchar(150)|not null| |
|email|电子邮件地址|varchar(254)|not null| |
|is_staff|工作人员状态|bool|not null|默认值为: False|
|is_active|有效|bool|not null|默认值为: True|
|date_joined|加入日期|datetime|not null|默认值为: <function now at 0x7fd2e0714430>|
|user_type|user type|varchar(100)| | |
|pet|pet| | |外键, 和myapp包下的Pet是many_to_one关系|
|user_icon_url|user icon url|varchar(200)| | |
|user_phone_number|user phone number|varchar(100)| | |
| | | | | |
| | | | | |
|VetHospital(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|vet_hospital_id|vet hospital id|int| | |
|vet|vet| |not null|唯一, 外键, 和myapp包下的User是one_to_one关系|
|hospital|hospital| | |外键, 和myapp包下的Hospital是many_to_one关系|
|(('vet', 'hospital'),)联合唯一| | | | |
| | | | | |
| | | | | |
|WalkPoint(None)| | | | |
|变量|变量名称|类型|null/not null|备注|
|walk_point_id|walk point id|int|not null| |
|walk_point_x|walk point x|double| | |
|walk_point_y|walk point y|double| | |
|walk_point_user|walk point user| | |外键, 和myapp包下的User是many_to_one关系|
| | | | | |
| | | | | |
|EmailVerificationCode(邮箱验证码)| | | | |
|变量|变量名称|类型|null/not null|备注|
|code|验证码|varchar(20)|not null| |
|email|邮箱|varchar(50)|not null| |
|send_type|验证码类型|varchar(10)|not null|(('register', '注册'), ('forget', '找回密码'))|
|send_time|发送时间|datetime|not null|默认值为: <built-in method now of type object at 0x10b2e0b68>|
