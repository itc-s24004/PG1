import os
def prepare_dir(dir_name="save_dir"):
  if os.path.exists(dir_name):
    print(f"ディレクトリ '{dir_name}' が存在します。")
  else:
    os.mkdir(dir_name)
    print(f"ディレクトリ '{dir_name}' を作成しました。")
