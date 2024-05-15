"""
pip install tiktoken openai pandas matplotlib plotly scikit-learn numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

class Functions:
    """
    定义模板函数
    """
    def get_functions(self):
        weather_functions = [
            {
                "name": "get_current_weather",  # 功能的名称
                "description": "Get the current weather",  # 功能的描述
                "parameters": {  # 定义该功能需要的参数
                    "type": "object",
                    "properties": {  # 参数的属性
                        "location": {  # 地点参数
                            "type": "string",  # 参数类型为字符串
                            "description": "The city and state, e.g. San Francisco, CA",  # 参数的描述
                        },
                        "format": {  # 温度单位参数
                            "type": "string",  # 参数类型为字符串
                            "enum": ["celsius", "fahrenheit"],  # 参数的取值范围
                            "description": "The temperature unit to use. Infer this from the users location.",  # 参数的描述
                        },
                    },
                    "required": ["location", "format"],  # 该功能需要的必要参数
                },
            },
            {
                "name": "get_n_day_weather_forecast",  # 功能的名称
                "description": "Get an N-day weather forecast",  # 功能的描述
                "parameters": {  # 定义该功能需要的参数
                    "type": "object",
                    "properties": {  # 参数的属性
                        "location": {  # 地点参数
                            "type": "string",  # 参数类型为字符串
                            "description": "The city and state, e.g. San Francisco, CA",  # 参数的描述
                        },
                        "format": {  # 温度单位参数
                            "type": "string",  # 参数类型为字符串
                            "enum": ["celsius", "fahrenheit"],  # 参数的取值范围
                            "description": "The temperature unit to use. Infer this from the users location.",  # 参数的描述
                        },
                        "num_days": {  # 预测天数参数
                            "type": "integer",  # 参数类型为整数
                            "description": "The number of days to forecast",  # 参数的描述
                        }
                    },
                    "required": ["location", "format", "num_days"]  # 该功能需要的必要参数
                },
            },
        ]
        return weather_functions
