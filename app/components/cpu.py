import psutil


def get_cpu_data():
    return {
        "cpu_load": psutil.cpu_percent(interval=0),
        "cpu_freq": psutil.cpu_freq().current,
    }