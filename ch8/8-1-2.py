import os

def delete_dir(dir_name="save_dir"):
  if os.path.exists(dir_name):
    print(f"ディレクトリ '{dir_name}' が存在します。")
    os.rmdir(dir_name)
    print(f"ディレクトリ '{dir_name}' を消去しました。")
  else:
    print(f"ディレクトリ '{dir_name}' はありません。")