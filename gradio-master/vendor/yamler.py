import yaml
import os

class HandleYaml:
    yaml_content = None

    def __init__(self,path):
        cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前项目路径
        log_path = os.path.join(os.path.dirname(cur_path), 'config')
        self.yaml_content = self.read_yaml(os.path.join(log_path,path))

    def read_yaml(self, path):
        print(f'getcwd:{os.getcwd()}')  # 获取当前工作目录路径
        print(f'abspath:{os.path.abspath(".")}')  # 获取当前工作目录路径
        print(f'path:{path}')
        with open(path, 'rb') as f:
            cf = f.read()
        config = yaml.load(cf,Loader=yaml.Loader)
        return config

yml = HandleYaml('application.yaml')

if __name__ == '__main__':
    yml = HandleYaml('application.yaml')
    print(yml.yaml_content['database']['db_host'])
    print(yml.yaml_content['database']['db_port'])
    print(yml.yaml_content['database']['db_name'])