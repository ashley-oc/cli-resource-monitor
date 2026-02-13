from app.components.gpu import get_gpu_data
from app.components.cpu import get_cpu_data
from app.components.ram import get_ram_data
from .bar import create_bar


def render_display():
    #  GPU 
    print("\n--- GPU Data ---")
    gpu_data = get_gpu_data()
    gpu_bar = create_bar(gpu_data["gpu_load"])

    print(f"GPU Usage: [{gpu_bar}] {float(gpu_data['gpu_load']):.1f}%")
    print(f"VRAM: {gpu_data['vram_used']} MB / {gpu_data['vram_total']} MB" + "  |  " + f"Temperature: {gpu_data['gpu_temp']} °C" + "  |  " + f"Clock Speed: {gpu_data['gpu_clock']} MHz")


    #  CPU
    print("\n--- CPU Data ---")
    cpu_data = get_cpu_data()
    cpu_bar = create_bar(cpu_data["cpu_load"])
    print(f"CPU Usage: [{cpu_bar}] {float(cpu_data['cpu_load']):.1f}")
    print(f"CPU Frequency: {cpu_data['cpu_freq']:.1f} MHz")


    #  RAM
    print("\n--- RAM Data ---")
    ram_data = get_ram_data()
    ram_bar = create_bar(ram_data["percent"])
    print(f"RAM Usage: [{ram_bar}] {float(ram_data['percent']):.1f}%")
    print(f"Used: {ram_data['used'] / (1024 * 1024):.1f} GB / Total: {ram_data['total'] / (1024 * 1024):.1f} GB")