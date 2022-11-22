
from torch.utils.data import Dataset
from PIL import Image


def default_loader(path):
    return Image.open(path)


class DigitDataset(Dataset):

    # data loading
    def __init__(self, annotation_map_path, transform=None, target_transform=None, loader=default_loader):
        with open(annotation_map_path, 'r') as fh:
            imgs = []
            for line in fh:
                line = line.strip('\n')
                line = line.rstrip()
                words = line.split('|')
                imgs.append((words[0], int(words[1])))
            self.imgs = imgs
            self.transform = transform
            self.target_transform = target_transform
            self.loader = loader

    # working for indexing
    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = self.loader(fn)
        if self.transform is not None:
            img = self.transform(img)
        return img, label

    # return the length of our dataset
    def __len__(self):
        return len(self.imgs)
