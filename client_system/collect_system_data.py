import psutil
#import GPUtil
import json
from time import time

system_name = "test system"
system_uptime = 0
battery_charge = 0
disk_space_used = 0
total_disk_space = 0
fan_speed = 0
gpu_load = 0
gpu_temp = 0
ram_load = 0
total_ram_space = 0
cpu_load = 0
cpu_temp = 0

def return_data():
    data = {
        "device_name": "Test Device 0",
        "uptime": get_uptime_data(),
        "battery_charge": "Battery Charge",
        "battery_status": "Battery Status",
        "disk_space_used": get_storage_used_data(),
        "total_disk_space": get_storage_total_data(),
        "fan_speed": "Fan Speed",
        "gpu_load": "GPU Load",
        "gpu_temp": "GPU Temp",
        "ram_load": get_ram_load_data(),
        "total_ram_space": get_ram_total_data(),
        "cpu_load": get_cpu_load_data(),   
        "cpu_temp": "CPU Temp"
    }

    data = [data]
    data = json.dumps(data)
    return data
    '''
    data = []
    data.append("device_name": 'Test Device 0')
    data.append(f"uptime: {get_uptime_data()}")
    data.append(f"device_name: 'Battery Charge'")
    data.append(f"uptime: {get_storage_used_data()}")
    data.append(get_storage_total_data())
    data.append(fan_speed)
    data.append("GPU load")
    data.append("GPU temp")
    data.append(get_ram_load_data())
    data.append(get_ram_total_data())
    data.append(get_cpu_load_data())
    data.append("CPU temp")
    return data
    '''

def get_uptime_data():
    try:
        system_boot_time = psutil.boot_time
        system_uptime = time() - system_boot_time
        return system_uptime
    except:
        return "Can't retrieve system uptime"

def get_ram_load_data():
    try:
        ram = psutil.virtual_memory()
        return ram.used
    except:
        return "Can't retrieve RAM load data"

def get_ram_total_data():
    try:
        ram = psutil.virtual_memory()
        return ram.total
    except:
        return "Can't retrieve RAM total data"

def get_cpu_load_data(): #Temperature remains unhandled.
    try:
        cpu_load = psutil.cpu_percent(interval=1)
        return cpu_load
    except:
        return "Can't get CPU data"

def get_gpu_data():
    #For NVIDIA GPUs apparantly. Can be handled later.
    all_gpus = GPUtil.getGPUs()
    gpu_temps = []

    for i in range(all_gpus):
        temp = all_gpus[i].temperature
        gpu_temps.append(temp)

    index = 0
    highest_temp = 0
    
    for i in range(gpu_temps):
        if gpu_temps[i] > highest_temp:
            highest_temp = gpu_temps[i]
            index = i

    gpu_load = all_gpus[index].load
    gpu_temp = all_gpus[index].temperature

def get_storage_used_data(): 
    try:
        disk = psutil.disk_usage("/")
        return disk.used
    except:
        return "Can't get storage used data"
    
def get_storage_total_data(): 
    try:
        disk = psutil.disk_usage("/")
        return disk.total
    except:
        return "Can't get storage total data"
