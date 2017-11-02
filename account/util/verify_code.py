from random import Random


def generate_verify_code():
    rt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_%$'
    length = len(chars) - 1
    random = Random()
    for i in range(128):
        rt += chars[random.randint(0, length)]
    return rt
