import torch
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter

class TensorsOperate:

    def build(self):
        x = torch.empty(3,5)
        print(f"x:\n{x}")
        x2 = x.reshape(-1, 1)
        print(f"x2:\n{x2}")
        x3 = x.view(-1, 1)
        print(f"x3:\n{x3}")
    def views(self):
        """
        原始想法：把得到的一维或多维tensor转成可视化的图形来表示，方便理解
        但下面的代码好像没有达到预期效果
        :return:
        """
        x = torch.empty(3, 5) # 3行 5列
        print(f"x:\n{x}")
        print("-----------------")
        print(f"x.shape:\n{x.shape}")
        print("-----------------")
        x3 = x.view(-1, 1) # 15行 1列
        print(f"x3:\n{x3}")
        print("-----------------")
        print(f"x3.shape:\n{x3.shape}")
        x4 = x.reshape(1, -1) # 1行 15列
        print(f"x4:\n{x4}")
        print("-----------------")
        print(f"x4.shape:\n{x4.shape}")
        """
        这种方法适用于二维或三维张量（对于三维张量，每个切片将被绘制成一系列图像）
        """
        plt.imshow(x, cmap='viridis')
        plt.colorbar()
        plt.show()
    def summary_graph(self):
        """
        失败了，没有成功保存，原因是缺少依赖包安装，tensorboard可以正常起来
        后面再捣鼓
        本函数是想通过tensorboard的SummaryWriter保存tensor维度数据
        然后通过tensorboard来显示
        安装tensorboard
        pip install tensorboard -i https://pypi.tuna.tsinghua.edu.cn/simple
        支持tensorbaord
        tensorboard --logdir=runs
        :return:
        """
        writer = SummaryWriter('runs/tensor_dim')
        x = torch.empty(3, 5) # 3行 5列
        writer.add_graph(x)
        writer.close()


if __name__ == '__main__':
    t = TensorsOperate()
    if False:
        t.build()
        t.views()
    else:
        t.summary_graph()
