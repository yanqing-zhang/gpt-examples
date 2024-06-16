import torch


class TensorsOperate:

    def build(self):
        x = torch.empty(3,5)
        print(f"x:\n{x}")
        x2 = x.reshape(-1, 1)
        print(f"x2:\n{x2}")
        x3 = x.view(-1, 1)
        print(f"x3:\n{x3}")

if __name__ == '__main__':
    t = TensorsOperate()
    t.build()