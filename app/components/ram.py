import psutil


def get_ram_data() -> dict:
    ram = psutil.virtual_memory()
    return {
        "total": ram.total,
        "available": ram.available,
        "used": ram.used,
        "percent": ram.percent
    }