import subprocess


def get_gpu_data() -> dict:
    '''
    Uses subprocess to call nvidia-smi and retrieve the following GPU statistics:
     - VRAM usage (used and total),
     - Core temperature,
     - Clock speed.
     - GPU load.
    '''
    result = subprocess.check_output([
        "nvidia-smi",
        "--query-gpu=memory.used,memory.total,temperature.gpu,clocks.gr,utilization.gpu",
        "--format=csv,noheader,nounits"
    ], encoding="utf-8")

    #  Values are all returned as Strings.
    vram_used, vram_total, gpu_temp, gpu_clock, gpu_load = result.strip().split(", ")
    
    return {
        "vram_used": int(vram_used),
        "vram_total": int(vram_total),
        "gpu_temp": int(gpu_temp),
        "gpu_clock": int(gpu_clock),
        "gpu_load": int(gpu_load)
    }