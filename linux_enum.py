import subprocess
import os

def get_ip_addresses():
    """
    Çalışan ana bilgisayarın IP adreslerini döndürür.
    """
    ip_addresses = subprocess.check_output(["ip", "addr", "show"]).decode("utf-8")
    return ip_addresses

def get_local_users():
    """
    Çalışan ana bilgisayardaki yerel kullanıcıları döndürür.
    """
    local_users = subprocess.check_output(["cat", "/etc/passwd"]).decode("utf-8")
    return local_users

def get_installed_packages():
    """
    Çalışan ana bilgisayardaki kurulu paketleri ve sürümlerini döndürür.
    """
    installed_packages = subprocess.check_output(["dpkg", "-l"]).decode("utf-8")
    return installed_packages

def get_open_ports():
    """
    Çalışan ana bilgisayardaki açık portları döndürür.
    """
    open_ports = subprocess.check_output(["netstat", "-tuln"]).decode("utf-8")
    return open_ports

def get_network_services():
    """
    Çalışan ana bilgisayardaki ağ hizmetlerini döndürür.
    """
    network_services = subprocess.check_output(["netstat", "-punta"]).decode("utf-8")
    return network_services

def get_bash_history():
    """
    Çalışan ana bilgisayarın Bash geçmişini döndürür.
    """
    if os.path.exists(os.path.expanduser("~/.bash_history")):
        bash_history = subprocess.check_output(["cat", "~/.bash_history"]).decode("utf-8")
        return bash_history
    else:
        return "Bash history not available or disabled."

def get_allowed_sudoers():
    """
    Çalışan ana bilgisayarda sudo yetkisi olan kullanıcıları döndürür.
    """
    allowed_sudoers = subprocess.check_output(["cat", "/etc/sudoers"]).decode("utf-8")
    return allowed_sudoers

def get_running_processes():
    """
    Çalışan ana bilgisayardaki çalışan işlemleri döndürür.
    """
    running_processes = subprocess.check_output(["ps", "-aux"]).decode("utf-8")
    return running_processes

def get_elevated_processes():
    """
    Çalışan ana bilgisayardaki yüksek ayrıcalıklı işlemleri döndürür.
    """
    processes = subprocess.check_output(["ps", "-aux"]).decode("utf-8")
    elevated_processes = [line for line in processes.split('\n') if 'sudo' in line]
    return '\n'.join(elevated_processes)

def get_environment_variables():
    """
    Çalışan ana bilgisayardaki çevre değişkenlerini döndürür.
    """
    environment_variables = subprocess.check_output(["printenv"]).decode("utf-8")
    return environment_variables

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)
        
# Tarama adında bir klasör oluşturma fonksiyonu
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

# Örnek kullanım
if __name__ == "__main__":
    directory_name = "tarama"

    create_directory(directory_name)

    ip_output = get_ip_addresses()
    save_to_file(ip_output, f'{directory_name}/ip_addresses.txt')

    local_users_output = get_local_users()
    save_to_file(local_users_output, f'{directory_name}/local_users.txt')

    installed_packages_output = get_installed_packages()
    save_to_file(installed_packages_output, f'{directory_name}/installed_packages.txt')

    open_ports_output = get_open_ports()
    save_to_file(open_ports_output, f'{directory_name}/open_ports.txt')

    network_services_output = get_network_services()
    save_to_file(network_services_output, f'{directory_name}/network_services.txt')

    bash_history_output = get_bash_history()
    save_to_file(bash_history_output, f'{directory_name}/bash_history.txt')

    allowed_sudoers_output = get_allowed_sudoers()
    save_to_file(allowed_sudoers_output, f'{directory_name}/allowed_sudoers.txt')

    running_processes_output = get_running_processes()
    save_to_file(running_processes_output, f'{directory_name}/running_processes.txt')

    elevated_processes_output = get_elevated_processes()
    save_to_file(elevated_processes_output, f'{directory_name}/elevated_processes.txt')

    environment_variables_output = get_environment_variables()
    save_to_file(environment_variables_output, f'{directory_name}/environment_variables.txt')