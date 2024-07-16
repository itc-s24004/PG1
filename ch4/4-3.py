def show_args(*args):
    '''与えられた低数の位置引数をタプルにまとめて受取そのタプルを表示して返す'''
    print("Positional arguments:", args)
    return args

def show_kwargs(**kwargs):
    '''与えられた複数のキーワード引数を辞書にまとめて受取その辞書を表示して返す'''
    print("Keyword arguments:", kwargs)
    return kwargs
    
positional_args = (4, 5, 6, "ya")
keyword_args = {
    "pasta": "ペンネ",
    "drink": "赤ワイン",
    "main_dish": "肉料理",
    "n_customers": 3
}
