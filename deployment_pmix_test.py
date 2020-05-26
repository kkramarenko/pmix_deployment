import os
import subprocess

# Base variables
abs_path_name = ''

def create_directories(base_dir_name, needed_dirs_name):
    # Create all needed directories
    print('<========== Create deploy folder =========>')
    ret = os.system('mkdir ' + base_dir_name)
    if (ret != 0):
        print('<========== Can`t create directory: ' + base_dir_name)
        os._exit(1)

    print('<========== Goto deploy folder =========>')
    os.chdir(base_dir_name)

    print('<========== Create install/sources folders =========>')
    ret = os.system('mkdir install sources')
    if (ret != 0):
        print('<========== Can`t create directory: install or sources')
        os._exit(2)

    print('<========== Goto sources folder =========>')
    os.chdir('sources')


    print('<========== Creating all needed folders ==========>')
    print(needed_dirs_name)
    ret = os.system('mkdir ' + needed_dirs_name)
    if (ret != 0):
        print('<========== Can`t create directories: ' + needed_dirs_name)
        os._exit(3)
 
def hwloc_get_sources_routine(hwloc_dir_name, hwloc_git_url, hwloc_branch_name=''):
    # Get hwloc sources
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/sources/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    print('<========== Get hwloc sources ==========>')
    ret = os.system('git clone ' + hwloc_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for hwloc: ' + hwloc_git_url)
        os._exit(4)

    if (hwloc_branch_name != ''):
        print('<========== Change work branch to: ' + hwloc_branch_name)
        ret = os.system('git checkout ' + hwloc_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + hwloc_branch_name)
            os._exit(5)

def hwloc_conf_routine(hwloc_dir_name, hwloc_conf_param): 
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/sources/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    print('<========== Create configure scripts ==========>')
    ret = os.system('git clean -dfX')
    if (ret != 0):
        print('<========== Can`t clean repository')
        os._exit(6)

    ret = os.system('./autogen.sh')
    if (ret != 0):
        print('<========== Run autogen.sh error')
        os._exit(7)

    # Configure hwloc
#    hwloc_install_dir = abs_path_name + '/install/' + hwloc_dir_name
#    hwloc_conf_param += hwloc_install_dir
    print('<========== Run configure with parameters: ' + hwloc_conf_param)
    ret = os.system('./configure ' + hwloc_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(8)

def hwloc_compile_routine(hwloc_dir_name, thread_num=1):
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/sources/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    # Compile hwloc
    print('<========== Compile hwloc ==========>')
    ret = os.system('make -j' + str(thread_num))
    if (ret != 0):
        print('<========== Can`t compile hwloc')
        os._exit(9)

def hwloc_install_routine(hwloc_dir_name):
    print('<========== Goto hwloc folder ==========>')
    hwloc_abs_path_name = abs_path_name + '/sources/' + hwloc_dir_name 
    print(hwloc_abs_path_name)
    os.chdir(hwloc_abs_path_name)

    # Install hwloc
    hwloc_install_dir = abs_path_name + '/install/' + hwloc_dir_name
    print('<========== Install hwloc in: ' + hwloc_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install hwloc to: ' + hwloc_install_dir)
        os._exit(10)

def libevent_get_sources_routine(libevent_dir_name, libevent_git_url, libevent_branch_name=''):
    # Get libevent sources
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/sources/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)

    print('<========== Get libevent sources ==========>')
    ret = os.system('git clone ' + libevent_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for libevent: ' + libevent_git_url)
        os._exit(11)

    if (libevent_branch_name != ''):
        print('<========== Change work branch to: ' + libevent_branch_name)
        ret = os.system('git checkout ' + libevent_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + libevent_branch_name)
            os._exit(12)

def libevent_conf_routine(libevent_dir_name, libevent_conf_param):
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/sources/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)

    print('<========== Create configure scripts ==========>')
    ret = os.system('git clean -dfX')
    if (ret != 0):
        print('<========== Can`t clean repository')
        os._exit(13)

    print('<========== Create configure scripts ==========>')
    ret = os.system('./autogen.sh')
    if (ret != 0):
        print('<========== Run autogen.sh error')
        os._exit(14)

    # Configure libevent
#    libevent_install_dir = abs_path_name + '/install/' + libevent_dir_name
#    libevent_conf_param += libevent_install_dir
    print('<========== Run configure with parameters: ' + libevent_conf_param)
    ret = os.system('./configure ' + libevent_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(15)

def libevent_compile_routine(libevent_dir_name, thread_num=1):
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/sources/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)
    
    # Compile libevent
    print('<========== Compile libevent ==========>')
    ret = os.system('make -j' + str(thread_num))
    if (ret != 0):
        print('<========== Can`t compile libevent')
        os._exit(16)

def libevent_install_routine(libevent_dir_name):
    print('<========== Goto libevent folder ==========>')
    libevent_abs_path_name = abs_path_name + '/sources/' + libevent_dir_name 
    print(libevent_abs_path_name)
    os.chdir(libevent_abs_path_name)
 
    # Install libevent 
    libevent_install_dir = abs_path_name + '/install/' + libevent_dir_name
    print('<========== Install libevent in: ' + libevent_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install libevent to: ' + libevent_install_dir)
        os._exit(17)

def pmix_get_sources_routine(pmix_dir_name, pmix_git_url, pmix_branch_name):
    # Get pmix sources
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/sources/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)

    print('<========== Get pmix sources ==========>')
    ret = os.system('git clone ' + pmix_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for pmix: ' + pmix_git_url)
        os._exit(18)

    if (pmix_branch_name != ''):
        print('<========== Change work branch to: ' + pmix_branch_name)
        ret = os.system('git checkout ' + pmix_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + pmix_branch_name)
            os._exit(19)

def pmix_conf_routine(pmix_dir_name, pmix_conf_param):
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/sources/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)
   
    print('<========== Create configure scripts ==========>')
    ret = os.system('git clean -dfX')
    if (ret != 0):
        print('<========== Can`t clean repository')
        os._exit(20)

    print('<========== Create configure scripts ==========>')
    ret = os.system('./autogen.pl')
    if (ret != 0):
        print('<========== Run autogen.pl error')
        os._exit(21)

   # Configure pmix
#    pmix_conf_param += abs_path_name + '/install/' + libevent_dir_name + ' --prefix='
#    pmix_install_dir = abs_path_name + '/install/' + pmix_dir_name
#    pmix_conf_param += pmix_install_dir
    print('<========== Run configure with parameters: ' + pmix_conf_param)
    ret = os.system('./configure ' + pmix_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(22)

def pmix_compile_routine(pmix_dir_name, thread_num=1):
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/sources/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)
    
    # Compile pmix
    print('<========== Compile pmix ==========>')
    ret = os.system('make -j' + str(thread_num))
    if (ret != 0):
        print('<========== Can`t compile pmix')
        os._exit(23)

def pmix_install_routine(pmix_dir_name):
    print('<========== Goto pmix folder ==========>')
    pmix_abs_path_name = abs_path_name + '/sources/' + pmix_dir_name 
    print(pmix_abs_path_name)
    os.chdir(pmix_abs_path_name)
 
    # Install pmix 
    pmix_install_dir = abs_path_name + '/install/' + pmix_dir_name
    print('<========== Install pmix in: ' + pmix_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install pmix to: ' + pmix_install_dir)
        os._exit(24)

    os.chdir('contrib/perf_tools')
    os.system('make PMIX_BASE=' + abs_path_name + '/install/' + pmix_dir_name)


def openmpi_get_sources_routine(openmpi_dir_name, openmpi_git_url, openmpi_branch_name):
    # Get openmpi sources
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/sources/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)

    print('<========== Get openmpi sources ==========>')
    ret = os.system('git clone ' + openmpi_git_url + ' .')
    if (ret != 0):
        print('<========== Can`t get sources for openmpi: ' + openmpi_git_url)
        os._exit(25)

    if (openmpi_branch_name != ''):
        print('<========== Change work branch to: ' + openmpi_branch_name)
        ret = os.system('git checkout ' + openmpi_branch_name)
        if (ret != 0):
            print('<========== Can`t change branch to: ' + openmpi_branch_name)
            os._exit(26)

def openmpi_conf_routine(openmpi_dir_name, openmpi_conf_param):
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/sources/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)
   
    print('<========== Create configure scripts ==========>')
    ret = os.system('git clean -dfX')
    if (ret != 0):
        print('<========== Can`t clean repository')
        os._exit(27)

    print('<========== Create configure scripts ==========>')
    ret = os.system('./autogen.pl')
    if (ret != 0):
        print('<========== Run autogen.pl error')
        os._exit(28)

   # Configure openmpi
#    openmpi_conf_param += abs_path_name + '/install/' + openmpi_dir_name + ' --prefix='
#    openmpi_install_dir = abs_path_name + '/install/' + openmpi_dir_name
#    openmpi_conf_param += openmpi_install_dir
    print('<========== Run configure with parameters: ' + openmpi_conf_param)
    ret = os.system('./configure ' + openmpi_conf_param)
    if (ret != 0):
        print('<========== Configure error')
        os._exit(29)

def openmpi_compile_routine(openmpi_dir_name, thread_num=1):
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/sources/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)
    
    # Compile openmpi
    print('<========== Compile openmpi  ==========>')
    ret = os.system('make -j' + str(thread_num))
    if (ret != 0):
        print('<========== Can`t compile openmpi')
        os._exit(30)

def openmpi_install_routine(openmpi_dir_name):
    print('<========== Goto openmpi folder ==========>')
    openmpi_abs_path_name = abs_path_name + '/sources/' + openmpi_dir_name 
    print(openmpi_abs_path_name)
    os.chdir(openmpi_abs_path_name)
 
    # Install openmpi 
    openmpi_install_dir = abs_path_name + '/install/' + openmpi_dir_name
    print('<========== Install openmpi in: ' + openmpi_install_dir)
    ret = os.system('make install')
    if (ret != 0):
        print('<========== Can`t install openmpi to: ' + openmpi_install_dir)
        os._exit(31)


def main(base_dir_name, thread_num):
#    needed_dirs = ['hwloc', 'libevent', 
#                   'pmix_base', 'pmix_poc','pmix_poc_base',
#                   'pmix_poc_base_lockless','openmpi_base',
#                   'openmpi_poc', 'openmpi_poc_base',
#                   'openmpi_poc_base_lockless']

    needed_dirs = ['hwloc_master', 'libevent_master', 
                   'pmix_master','openmpi_master',]


    needed_dirs_name = ''
    for name in needed_dirs:
        needed_dirs_name += name + ' '

    create_directories(base_dir_name, needed_dirs_name)
    
    hwloc_dir_name = 'hwloc_master'
    hwloc_git_url = 'https://github.com/open-mpi/hwloc.git'
    hwloc_branch_name = ''
    hwloc_conf_param = '--prefix=' + abs_path_name + '/install/' + hwloc_dir_name
    hwloc_get_sources_routine(hwloc_dir_name, hwloc_git_url, hwloc_branch_name)
    hwloc_conf_routine(hwloc_dir_name, hwloc_conf_param)
    hwloc_compile_routine(hwloc_dir_name, thread_num)
    hwloc_install_routine(hwloc_dir_name)

    libevent_dir_name = 'libevent_master'
    libevent_git_url = 'https://github.com/libevent/libevent.git'
    libevent_branch_name = ''
    libevent_conf_param = '--prefix=' + abs_path_name + '/install/' + libevent_dir_name
    libevent_get_sources_routine(libevent_dir_name, libevent_git_url, libevent_branch_name)
    libevent_conf_routine(libevent_dir_name, libevent_conf_param)
    libevent_compile_routine(libevent_dir_name, thread_num)
    libevent_install_routine(libevent_dir_name)

    pmix_dir_name = 'pmix_master'
    pmix_git_url = 'https://github.com/openpmix/openpmix.git'
    pmix_branch_name = 'v3.1.5'
    pmix_conf_param = '--disable-debug --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    pmix_conf_param += ' --prefix=' + abs_path_name + '/install/' + pmix_dir_name 
    pmix_get_sources_routine(pmix_dir_name, pmix_git_url, pmix_branch_name)
    pmix_conf_routine(pmix_dir_name, pmix_conf_param)
    pmix_compile_routine(pmix_dir_name, thread_num)
    pmix_install_routine(pmix_dir_name)
    
    openmpi_dir_name = 'openmpi_master'
    openmpi_git_url = 'https://github.com/open-mpi/ompi.git'
    openmpi_branch_name = 'v4.0.3'
    openmpi_conf_param = '--disable-debug --prefix=' + abs_path_name + '/install/' + openmpi_dir_name
    openmpi_conf_param += ' --with-hwloc=' + abs_path_name + '/install/' + hwloc_dir_name
    openmpi_conf_param += ' --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    openmpi_conf_param += ' --with-pmix=' + abs_path_name + '/install/' + pmix_dir_name
    openmpi_get_sources_routine(openmpi_dir_name, openmpi_git_url, openmpi_branch_name)
    openmpi_conf_routine(openmpi_dir_name, openmpi_conf_param)
    openmpi_compile_routine(openmpi_dir_name, thread_num)
    openmpi_install_routine(openmpi_dir_name)

    #pmix_dir_name = 'pmix_poc'
    #pmix_git_url = 'https://github.com/artpol84/pmix.git'
    #pmix_branch_name = 'origin/eurompi2018/poc'
    #pmix_conf_param = '--disable-debug --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    #pmix_conf_param += ' --prefix=' + abs_path_name + '/install/' + pmix_dir_name 
    #pmix_get_sources_routine(pmix_dir_name, pmix_git_url, pmix_branch_name)
    #pmix_conf_routine(pmix_dir_name, pmix_conf_param)
    #pmix_compile_routine(pmix_dir_name, thread_num)
    #pmix_install_routine(pmix_dir_name)
    
    #openmpi_dir_name = 'openmpi_poc'
    #openmpi_git_url = 'https://github.com/open-mpi/ompi.git'
    #openmpi_branch_name = 'v3.0.3'
    #openmpi_conf_param = '--disable-debug --prefix=' + abs_path_name + '/install/' + openmpi_dir_name
    #openmpi_conf_param += ' --with-hwloc=' + abs_path_name + '/install/' + hwloc_dir_name
    #openmpi_conf_param += ' --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    #openmpi_conf_param += ' --with-pmix=' + abs_path_name + '/install/' + pmix_dir_name
    #openmpi_get_sources_routine(openmpi_dir_name, openmpi_git_url, openmpi_branch_name)
    #openmpi_conf_routine(openmpi_dir_name, openmpi_conf_param)
    #openmpi_compile_routine(openmpi_dir_name, thread_num)
    #openmpi_install_routine(openmpi_dir_name)

    #pmix_dir_name = 'pmix_poc_base'
    #pmix_git_url = 'https://github.com/artpol84/pmix.git'
    #pmix_branch_name = 'origin/eurompi2018/poc_base'
    #pmix_conf_param = '--disable-debug --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    #pmix_conf_param += ' --prefix=' + abs_path_name + '/install/' + pmix_dir_name 
    #pmix_get_sources_routine(pmix_dir_name, pmix_git_url, pmix_branch_name)
    #pmix_conf_routine(pmix_dir_name, pmix_conf_param)
    #pmix_compile_routine(pmix_dir_name, thread_num)
    #pmix_install_routine(pmix_dir_name)
    
    #openmpi_dir_name = 'openmpi_poc_base'
    #openmpi_git_url = 'https://github.com/open-mpi/ompi.git'
    #openmpi_branch_name = 'v3.0.3'
    #openmpi_conf_param = '--disable-debug --prefix=' + abs_path_name + '/install/' + openmpi_dir_name
    #openmpi_conf_param += ' --with-hwloc=' + abs_path_name + '/install/' + hwloc_dir_name
    #openmpi_conf_param += ' --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    #openmpi_conf_param += ' --with-pmix=' + abs_path_name + '/install/' + pmix_dir_name
    #openmpi_get_sources_routine(openmpi_dir_name, openmpi_git_url, openmpi_branch_name)
    #openmpi_conf_routine(openmpi_dir_name, openmpi_conf_param)
    #openmpi_compile_routine(openmpi_dir_name, thread_num)
    #openmpi_install_routine(openmpi_dir_name)

    #pmix_dir_name = 'pmix_poc_base_lockless'
    #pmix_git_url = 'https://github.com/artpol84/pmix.git'
    #pmix_branch_name = 'origin/eurompi2018/poc_base_lockless'
    #pmix_conf_param = '--disable-debug --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    #pmix_conf_param += ' --prefix=' + abs_path_name + '/install/' + pmix_dir_name 
    #pmix_get_sources_routine(pmix_dir_name, pmix_git_url, pmix_branch_name)
    #pmix_conf_routine(pmix_dir_name, pmix_conf_param)
    #pmix_compile_routine(pmix_dir_name, thread_num)
    #pmix_install_routine(pmix_dir_name)
    
    #openmpi_dir_name = 'openmpi_poc_base_lockless'
    #openmpi_git_url = 'https://github.com/open-mpi/ompi.git'
    #openmpi_branch_name = 'v3.0.3'
    #openmpi_conf_param = '--disable-debug --prefix=' + abs_path_name + '/install/' + openmpi_dir_name
    #openmpi_conf_param += ' --with-hwloc=' + abs_path_name + '/install/' + hwloc_dir_name
    #openmpi_conf_param += ' --with-libevent=' + abs_path_name + '/install/' + libevent_dir_name
    #openmpi_conf_param += ' --with-pmix=' + abs_path_name + '/install/' + pmix_dir_name
    #openmpi_get_sources_routine(openmpi_dir_name, openmpi_git_url, openmpi_branch_name)
    #openmpi_conf_routine(openmpi_dir_name, openmpi_conf_param)
    #openmpi_compile_routine(openmpi_dir_name, thread_num)
    #openmpi_install_routine(openmpi_dir_name)


if __name__ == '__main__':
    thread_num = 28
    base_dir_name = 'deploy'
    abs_path_name = os.path.abspath(os.getcwd()) + '/' + base_dir_name
    main(base_dir_name, thread_num)
