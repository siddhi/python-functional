def compose2(fn1, fn2):
    def composed(*args, **kwargs):
        return fn2(fn1(*args, **kwargs))
    return composed


def update_dict(dict, key, value):
    new_dict = {}
    new_dict[key] = value
    return dict | new_dict


def stream_logs(logs):
    print(*logs, sep='\n')


