import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')

django.setup()
from django.db import models
from pandas import DataFrame

from django.conf import settings


# # 获取 模型类 unique_together数据
# model_name.PositionKind._meta.original_attrs.get('unique_together')
# # 获取 模型类 verbose_name
# model_name.PositionKind._meta.original_attrs.get('verbose_name')
# # 获取模型类


class HandleModelInfoExport(object):
    def __init__(self, *model_py_list):
        """
        初始化
        :param model_py_list: models.py的列表
        """
        self.model_py_list = list(model_py_list)
        self.columns = ['变量', '变量名称', '类型', 'null/not null', '备注']

    def get_model_excel(self, excel_name):
        """
        获取数据库模型excel
        :param excel_name:  要导出的excel名字
        :return: 格式:  xxx.xlsx
        """
        model_info = self.get_model_data()
        df = DataFrame(model_info, index=None)
        path = os.path.join(settings.BASE_DIR, f'{excel_name}.xlsx')
        df.to_excel(path, index=False)
        return '导出数据成功'

    def get_model_data(self):
        """
        获取模型导出数据
        :return:
        """
        model_info = []
        for model_py in self.model_py_list:
            model_info.extend(self.get_model_py_info(model_py))
        return model_info

    def get_model_py_info(self, model_py):
        """
        获取每一个models.py下的信息, 便利每个models.py的模型类获取数据
        :param model_py:  模型文件
        :return:
        """
        un_except_list = ['AbstractUser']  # 不希望获取信息的类名
        data_info_list = []
        model_name_keys = model_py.__dict__.keys()
        for key in model_name_keys:
            # 排除系统变量, 获取模型类名
            # 判断__dict__.keys() 中的key数据是否是模型类
            if model_py.__dict__.get(key).__class__ is models.base.ModelBase and key not in un_except_list:
                model_info = model_py.__dict__.get(key)  # 通过模型类名获取模型类
                if model_info:
                    original_attrs = model_info._meta.original_attrs  # 获取模型类 class Meta中的数据
                    table_name = original_attrs.get('verbose_name')  # 获取模型类的verbose_name
                    unique_together = original_attrs.get('unique_together')  # 获取联合唯一数据unique_together
                    data_info_list.append(self.add_blank_info(
                        f'{model_info.__name__}({table_name})'))  # 添加模型的verbose_name到表格数据中    用f进行占位需python3.6+

                    data_info_list.append(self.columns)  # 添加每个表格的表头

                    data_info_list.extend(self.get_every_model_info(model_info))  # 添加每个表格数据

                    if unique_together:  # 添加联合唯一备注信息
                        unique_together = f'{unique_together}联合唯一'
                        data_info_list.append(self.add_blank_info(unique_together))
                    data_info_list.append(self.add_blank_info(''))  # 添加空白行
                    data_info_list.append(self.add_blank_info(''))  # 添加空白行

        return data_info_list

    def get_every_model_info(self, model):
        """
        获取每一个模型类中的变量数据
        :param model:
        :return: 二位列表, 每个变量都是一维列表 存储'变量', '变量名称', '类型', 'null/not null', '备注'五个字段信息
        """
        fields_info_list = []
        un_except_list = ['id']  # 不希望获取的属性字段
        fields = model._meta.fields
        for field in fields:
            if field.name not in un_except_list:
                db_info = self.get_db_info(field)
                type_info = db_info[0]
                is_null = db_info[1]
                remark = db_info[2]
                fields_info_list.append([field.name, field.verbose_name, type_info, is_null, remark])

        return fields_info_list

    @staticmethod
    def add_blank_info(data_info):
        """
        添加空白数据, 凑数据
        :param data_info: 要凑数据的值
        :return:
        """
        return [data_info, '', '', '', '']

    def get_db_info(self, field):
        """
        获取该字段对象相关信息
        :param field: 字段对象
        :return:  [数据类型, 空值信息, 备注信息]
        """
        is_null = 'not null' if not field.null else ''  # 是否为空
        remark = '唯一' if field._unique else ''  # 是否唯一
        if field.choices:  # 是否有选择项目
            remark += f', {field.choices}'
        if field.default is not None and field.default is not models.fields.NOT_PROVIDED:  # 是否有默认值
            remark += f', 默认值为: {field.default}'
        if field.remote_field:  # 是否是外键引用  获取外键数据
            remark += f', {self.get_relation_info(field)}'
        if remark.startswith(','):
            remark = remark[2:]
        return [self.get_type_info(field), is_null, remark]

    @staticmethod
    def get_type_info(field):
        """
        获取数据类型
        :param field:
        :return:
        """
        if isinstance(field, models.fields.CharField):
            max_length = field.max_length
            return f'varchar({max_length})'
        elif isinstance(field, models.fields.TextField):
            return 'longtext'
        elif isinstance(field, models.fields.BooleanField):
            return 'bool'
        elif isinstance(field, models.fields.DateTimeField):
            return 'datetime'
        elif isinstance(field, models.fields.DateField):
            return 'date'
        elif isinstance(field, models.fields.TimeField):
            return 'time'
        elif isinstance(field, models.fields.IntegerField):
            return 'int'
        elif isinstance(field, models.fields.DecimalField):
            return 'decimal'
        elif isinstance(field, models.fields.FloatField):
            return 'double'
        elif isinstance(field, models.fields.IntegerField):
            return 'int'
        else:
            return ''

    @staticmethod
    def get_relation_info(field):
        """
        获取外键信息
        :param field:
        :return:
        """
        field_type = type(field)
        relation_class_name = field.remote_field.model.__name__  # 获取关联模型名
        relation_model_py = field.remote_field.model.__module__.split('.')[0]  # 获取关联模型所在的包名
        db_relation_list = ['many_to_one', 'many_to_one', 'one_to_many', 'one_to_one']  # 判断关系
        relation_name = ''
        for db_relation in db_relation_list:
            relation_name = db_relation
            if field_type.__dict__.get(db_relation):
                break
        return f'外键, 和{relation_model_py}包下的{relation_class_name}是{relation_name}关系'


import myapp.models as model

model_list = [model]
HandleModelInfoExport(*model_list).get_model_excel('数据库信息')
