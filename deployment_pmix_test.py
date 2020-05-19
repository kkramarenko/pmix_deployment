import os
import subprocess

# Base variables
abs_path_name = ''

base_dir_name = 'deploy'
openmpi_dir_name = 'openmpi'
pmix_dir_name = 'pmix'
hwloc_dir_name = 'hwloc'
libevent_dir_name = 'libevent'
install_dir_name = 'install'

# Git base variables
openmpi_git_url = 'https://github.com/open-mpi/ompi.git'
openmpi_branch_name = 'v3.0.3'
openmpi_conf_param = '--prefix='

pmix_git_url = 'https://github.com/artpol84/pmix.git'
pmix_branch_name = 'origin/eurompi2018/poc_base_lockless'
pmix_conf_param = '--disable-debug --with-libevent='

libevent_git_url = 'https://github.com/libevent/libevent.git'
libevent_branch_name = ''
libevent_conf_param = '--prefix='

hwloc_git_url = 'https://github.com/open-mpi/hwloc.git'
hwloc_branch_name = 'hwloc-1.11.1'
hwloc_conf_param = '--prefix='

def create_directories():
    # Create all needed directories
    print('<========== Create deploy folder =========>')
    ret = os.system('mkdir ' + base_dir_name)
    if (ret != 0):
        print('<========== Can`t create directory: ' + base_dir_name)
        os._exit(1)

    print('<========== Goto deploy folder =========>')
    os.chdir(base_dir_name)
 
    needed_dirs = [openmpi_dir_name, pmix_dir_name, hwloc_dir_name, libevent_dir_name, install_dir_name]

    needed_dirs_name = ''
    for name in needed_dirs:
        needed_dirs_name += name + ' '

    print('<========== Creating all needed folders ==========>')
    print(needed_dirs_name)
    ret = os.system('mkdir ' + needed_dirs_name)
    if (ret != 0):
        print('<========== Can`t create directories: ' + needed_dirs_name)
        os._exit(2)
 
def hwloc_get_sources_routine():
    # Get hwloc sources
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    print('<========== Get hwloc sources ==========>')
    ret = os.system('git clone ' + hwloc_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for hwloc: ' + hwloc_git_url)
        os._exit(3)

    if (hwloc_branch_name != ''):
        print('<========== Change work branch to: ' + hwloc_branch_name)
        ret = os.system('git checkout ' + hwloc_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + hwloc_branch_name)
            os._exit(4)

def hwloc_conf_routine(): 
    global hwloc_conf_param
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    print('<========== Create configure scripts ==========>')
    ret = os.system('git clean -dfX')
    if (ret != 0):
        print('<========== Can`t clean repository')
        os._exit(5)

    ret = os.system('./autogen.sh')
    if (ret != 0):
        print('<========== Run autogen.sh error')
        os._exit(5)

    # Configure hwloc
    hwloc_install_dir = abs_path_name + '/install/' + hwloc_dir_name
    hwloc_conf_param += hwloc_install_dir
    print('<========== Run configure with parameters: ' + hwloc_conf_param)
    ret = os.system('./configure ' + hwloc_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(6)

def hwloc_compile_routine():
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    # Compile hwloc
    print('<========== Compile hwloc ==========>')
    ret = os.system('make')
    if (ret != 0):
        print('<========== Can`t compile hwloc')
        os._exit(7)

def hwloc_install_routine():
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    # Install hwloc
    hwloc_install_dir = abs_path_name + '/install/' + hwloc_dir_name
    print('<========== Install hwloc in: ' + hwloc_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install hwloc to: ' + hwloc_install_dir)
        os._exit(8)

def libevent_get_sources_routine():
    # Get libevent sources
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)

    print('<========== Get libevent sources ==========>')
    ret = os.system('git clone ' + libevent_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for libevent: ' + libevent_git_url)
        os._exit(9)

    if (libevent_branch_name != ''):
        print('<========== Change work branch to: ' + libevent_branch_name)
        ret = os.system('git checkout ' + libevent_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + libevent_branch_name)
            os._exit(10)

    print('<========== Create configure scripts ==========>')
    ret = os.system('./autogen.sh')
    if (ret != 0):
        print('<========== Run autogen.sh error')
        os._exit(11)

def libevent_conf_routine():
    global libevent_conf_param
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)
   
    # Configure libevent
    libevent_install_dir = abs_path_name + '/install/' + libevent_dir_name
    libevent_conf_param += libevent_install_dir
    print('<========== Run configure with parameters: ' + libevent_conf_param)
    ret = os.system('./configure ' + libevent_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(12)

def libevent_compile_routine():
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)
    
    # Compile libevent
    print('<========== Compile libevent ==========>')
    ret = os.system('make')
    if (ret != 0):
        print('<========== Can`t compile libevent')
        os._exit(13)

def libevent_install_routine():
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)
 
    # Install libevent 
    libevent_install_dir = abs_path_name + '/install/' + libevent_dir_name
    print('<========== Install libevent in: ' + libevent_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install libevent to: ' + libevent_install_dir)
        os._exit(14)

def pmix_get_sources_routine():
    # Get pmix sources
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)

    print('<========== Get pmix sources ==========>')
    ret = os.system('git clone ' + pmix_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for pmix: ' + pmix_git_url)
        os._exit(15)

    if (pmix_branch_name != ''):
        print('<========== Change work branch to: ' + pmix_branch_name)
        ret = os.system('git checkout ' + pmix_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + pmix_branch_name)
            os._exit(16)

    print('<========== Create configure scripts ==========>')
    ret = os.system('./autogen.pl')
    if (ret != 0):
        print('<========== Run autogen.pl error')
        os._exit(17)

def pmix_conf_routine():
    global pmix_conf_param
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)
   
    # Configure pmix
    pmix_conf_param += abs_path_name + '/install/' + libevent_dir_name + ' --prefix='
    pmix_install_dir = abs_path_name + '/install/' + pmix_dir_name
    pmix_conf_param += pmix_install_dir
    print('<========== Run configure with parameters: ' + pmix_conf_param)
    ret = os.system('./configure ' + pmix_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(18)

def pmix_compile_routine():
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)
    
    # Compile pmix
    print('<========== Compile pmix ==========>')
    ret = os.system('make')
    if (ret != 0):
        print('<========== Can`t compile pmix')
        os._exit(19)

def pmix_install_routine():
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)
 
    # Install pmix 
    pmix_install_dir = abs_path_name + '/install/' + pmix_dir_name
    print('<========== Install pmix in: ' + pmix_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install pmix to: ' + pmix_install_dir)
        os._exit(20)

def openmpi_get_sources_routine():
    # Get openmpi sources
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)

    print('<========== Get openmpi sources ==========>')
    ret = os.system('git clone ' + openmpi_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for openmpi: ' + openmpi_git_url)
        os._exit(21)

    if (openmpi_branch_name != ''):
        print('<========== Change work branch to: ' + openmpi_branch_name)
        ret = os.system('git checkout ' + openmpi_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + openmpi_branch_name)
            os._exit(22)

    print('<========== Create configure scripts ==========>')
    ret = os.system('./autogen.pl')
    if (ret != 0):
        print('<========== Run autogen.pl error')
        os._exit(23)

def openmpi_conf_routine():
    global openmpi_conf_param
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)
   
    # Configure openmpi
#    openmpi_conf_param += abs_path_name + '/install/' + openmpi_dir_name + ' --prefix='
    openmpi_install_dir = abs_path_name + '/install/' + openmpi_dir_name
    openmpi_conf_param += openmpi_install_dir
    print('<========== Run configure with parameters: ' + openmpi_conf_param)
    ret = os.system('./configure ' + openmpi_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(24)

def openmpi_compile_routine():
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)
    
    # Compile pmix
    print('<========== Compile openmpi  ==========>')
    ret = os.system('make')
    if (ret != 0):
        print('<========== Can`t compile openmpi')
        os._exit(25)

def openmpi_install_routine():
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)
 
    # Install openmpi 
    openmpi_install_dir = abs_path_name + '/install/' + openmpi_dir_name
    print('<========== Install openmpi in: ' + openmpi_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install openmpi to: ' + openmpi_install_dir)
        os._exit(26)


def main():
    create_directories()
#    hwloc_get_sources_routine()
#    hwloc_conf_routine()
#    hwloc_compile_routine()
#    hwloc_install_routine()
#    libevent_get_sources_routine()
#    libevent_conf_routine()
#    libevent_compile_routine()
#    libevent_install_routine()
#    pmix_get_sources_routine()
#    pmix_conf_routine()
#    pmix_compile_routine()
#    pmix_install_routine()
    openmpi_get_sources_routine()
    openmpi_conf_routine()
    openmpi_compile_routine()
    openmpi_install_routine()


if __name__ == '__main__':
    abs_path_name = os.path.abspath(os.getcwd()) + '/' + base_dir_name
    main()
