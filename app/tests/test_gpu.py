from unittest.mock import patch
from app.components.gpu import get_gpu_data


@patch("app.components.gpu.subprocess.check_output")
def test_get_gpu_data(mock_nvidia_smi_output):
    # Fake nvidia-smi output replaces the actual subprocess.check_output in gpu.py during the test, bypassing the need to do any actual queries.
    mock_nvidia_smi_output.return_value = "500, 1000, 65, 1500, 75\n"

    result = get_gpu_data()

    assert result == {
        "vram_used": 500,
        "vram_total": 1000,
        "gpu_temp": 65,
        "gpu_clock": 1500,
        "gpu_load": 75
    }

