import torch
from torch import nn
# from torchsummary import summary
import torch.onnx
# import netron


class MixedNeuralNetwork(nn.Module):
    def __init__(self, options):
        super(MixedNeuralNetwork, self).__init__()

        # Convolution Pipeline
        self.convolutionPipeline = nn.Sequential(
            nn.Conv2d(options['tensor_num'], 16,
                      kernel_size=5, stride=2, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Dropout(),
            nn.Conv2d(16, 64, kernel_size=5, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Dropout()
        )

        # Tabular Pipeline
        self.tabularPipeline = nn.Sequential(
            nn.Linear(options['mlp_num'], 64),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(64, 64*64),
            nn.ReLU(),
            nn.Dropout()
        )

        # Shared Pipeline
        self.sharedPipeline = nn.Sequential(
            nn.Linear(64*64*2, 64*64*2*2),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(64*64*2*2, 64*64*2),
            nn.ReLU(),
            nn.Linear(64*3*3*2, 64),
            nn.Linear(64, 1)
        )

    def forward(self, x, y):
        x = self.convolutionPipeline(x)
        x = x.view(-1, 64*64)
        y = self.tabularPipeline(y)
        z = torch.cat((x, y), 1)
        z = self.sharedPipeline(z)
        return z


class ControlNeuralNetwork(nn.Module):
    def __init__(self, options):
        super(ControlNeuralNetwork, self).__init__()

        # Tabular Pipeline
        self.tabularPipeline = nn.Sequential(
            nn.Linear(options['mlp_num'], 64),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(64, 64*64),
            nn.ReLU(),
            nn.Dropout()
        )

        # Shared Pipeline
        self.sharedPipeline = nn.Sequential(
            nn.Linear(64*64, 64*64*2*2),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(64*64*2*2, 64*64*2),
            nn.ReLU(),
            nn.Linear(64*3*3*2, 64),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        y = self.tabularPipeline(x)
        z = self.sharedPipeline(y)
        return z


class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10),
            nn.Softmax()
        )

    def forward(self, x):
        x = x.view(-1, 28*28)
        y_hat = self.model(x)
        return y_hat


if __name__ == '__main__':

    # # 實驗模型
    # mixedModel = MixedNeuralNetwork({
    #     'tensor_num': 3,  # convolution pipeline輸入的張數
    #     'mlp_num': 9      # tabular pipeline輸入的參數量
    # }).cuda()
    # summary(mixedModel, input_size=[(3, 64, 64), (1, 9)])
    # print('\n\n')

    # # 對照模型
    # controlModel = ControlNeuralNetwork({
    #     'mlp_num': 9      # tabular pipeline輸入的參數量
    # })
    # summary(controlModel, input_size=(1, 9))

    # vector = torch.rand(1, 9)
    # model = ControlNeuralNetwork({'mlp_num': 9})
    # vector = vector.view(-1, 9)
    # output = model(vector)

    # onnx_path = 'control_model_name.onnx'
    # torch.onnx.export(model, vector, onnx_path)

    # netron.start(onnx_path)
    print('aa')
