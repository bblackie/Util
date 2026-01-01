import os

folder = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\Subjects'


def list_folders(path):
    items = os.listdir(path)
    for item in items:
        print(item)


def list_folders_recursive(path, max_depth=1, indent=0):
    if indent // 4 >= max_depth:
        return
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            print(' ' * indent + item)
            list_folders_recursive(item_path, max_depth, indent + 4)


if __name__ == "__main__":
    list_folders_recursive(folder, 2)



        