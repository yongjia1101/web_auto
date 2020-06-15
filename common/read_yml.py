import yaml


def get_yaml_data(yamlpath):
    """获取文件数据"""
    f = open(yamlpath, "r", encoding='utf-8')
    yaml_data = f.read()

    # 把文件数据转字典
    data = yaml.load(yaml_data)
    f.close()
    return data
