import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms
from torch import nn, optim, cuda, no_grad, max
import os
from os import listdir
from PIL import Image
from src.model import MLP
from src.dataset import DigitDataset
from torch.utils.data import DataLoader
import pyecharts.options as opts
from pyecharts.charts import Line


def loadDataset(path):
    data_dictionary = {}
    for category in listdir(path):
        data_dictionary[category] = []
        category_path = os.path.join(path, category)
        for image_path in listdir(category_path):
            image = Image.open(os.path.join(category_path, image_path))
            data = np.asarray(image)
            data_dictionary[category].append(data)
    return data_dictionary


def showDatasetStatus(data_dictionary, path):
    for category in listdir(path):
        print(f'{category} | {len(data_dictionary[category])}')


def produceAnnotationMapping(path, map_path):
    with open(map_path, 'w+') as f:
        for category in listdir(path):
            category_path = os.path.join(path, category)
            for image_path in listdir(category_path):
                image_path = os.path.join(category_path, image_path)
                row = f'{image_path}|{str(category)}'
                f.write(row+'\n')


def showFirstImageStatis(dataloader):
    features, labels = next(iter(dataloader))
    print(f"Feature batch shape: {features.size()}")
    print(f"Labels batch shape: {labels.size()}")
    img = features[0].squeeze()
    label = labels[0]
    plt.imshow(img, cmap="gray")
    plt.show()
    print(f"Label: {label}")


def train(model, data_loader):
    print('===== start training =====')
    loss_results = []
    epoch_list = []
    loss_function = nn.CrossEntropyLoss()
    optimizer = optim.SGD(params=model.parameters(), lr=0.01)
    for epoch in range(EPOCH):
        train_loss = 0.0
        step_per_epoch = 0
        for data, target in data_loader:
            step_per_epoch += 1
            data, target = data.to(DEVICE), target.to(DEVICE)
            optimizer.zero_grad()
            pred = model(data)
            loss = loss_function(pred, target)
            loss.backward()
            optimizer.step()
            train_loss += loss.item() * data.size(0)
            print(f'{step_per_epoch} | {loss.item() * data.size(0)}')
        train_loss = train_loss / len(data_loader.dataset)
        loss_results.append(train_loss)
        epoch_list.append(epoch)
        print('Epoch: {} \tTraining Loss: {:.6f}'.format(
            epoch + 1, train_loss))
    return loss_results, epoch_list


def test(model, data_loader):
    correct = 0
    total = 0
    with no_grad():  # 訓練集中不需要反向傳播
        for data, target in data_loader:
            data, target = data.to(DEVICE), target.to(DEVICE)
            outputs = model(data)
            _, predicted = max(outputs.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()
        print('Accuracy of the network on the test images: %d %%' % (
            100 * correct / total))
        return 100.0 * correct / total


if __name__ == '__main__':

    # 模型超參數
    EPOCH = 200
    BATCH_SIZE = 16
    DEVICE = 'cuda' if cuda.is_available() else 'cpu'

    # 檔案路徑
    annotation_file_path = r'./src/MNIST Dataset JPG format'
    training_data_path = r'./src/MNIST Dataset JPG format/MNIST - JPG - training'
    testing_data_path = r'./src/MNIST Dataset JPG format/MNIST - JPG - testing'

    # 讀取訓練資料
    # training_data_dictionary = loadDataset(training_data_path)
    # showDatasetStatus(training_data_dictionary, training_data_path)
    produceAnnotationMapping(
        training_data_path,
        os.path.join(annotation_file_path, 'training_map.txt')
    )

    # 讀取測試資料 & 產出映射檔
    # testing_data_dictionary = loadDataset(testing_data_path)
    # showDatasetStatus(testing_data_dictionary, testing_data_path)
    produceAnnotationMapping(
        testing_data_path,
        os.path.join(annotation_file_path, 'testing_map.txt')
    )

    # 使用映射檔建立training dataset
    train_data = DigitDataset(
        os.path.join(
            annotation_file_path, 'training_map.txt'
        ),
        transform=transforms.ToTensor()
    )
    train_dataloader = DataLoader(
        train_data, batch_size=BATCH_SIZE, shuffle=True)

    # 使用映射檔建立test dataset
    test_data = DigitDataset(
        os.path.join(
            annotation_file_path, 'testing_map.txt'
        ),
        transform=transforms.ToTensor()
    )
    test_dataloader = DataLoader(
        test_data, batch_size=BATCH_SIZE, shuffle=True)

    # 視覺化圖片
    showFirstImageStatis(train_dataloader)
    showFirstImageStatis(test_dataloader)

    model = MLP().to(DEVICE)

    loss_results, epoch_list = train(model, train_dataloader)
    print(loss_results, epoch_list)
    test(model, test_dataloader)

    (
        Line()
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(xaxis_data=epoch_list)
        .add_yaxis(
            series_name="",
            y_axis=loss_results,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .render("loss_graph.html")
    )



   