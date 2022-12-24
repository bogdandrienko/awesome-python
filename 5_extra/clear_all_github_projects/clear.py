import os
import shutil

if __name__ == "__main__":
    path = r'C:\github_projects'
    for root, dirs, files in os.walk(path, topdown=False):
        # for name in files:
        #     os.remove(os.path.join(root, name))
        for folder in dirs:
            print(folder)
            if folder in ["env", "venv", "node_modules", ".idea", "__pycache__"]:
                try:
                    # os.rmdir(os.path.join(root, folder))
                    shutil.rmtree(os.path.join(root, folder))
                except Exception as error:
                    print(error)
