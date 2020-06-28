import os
import subprocess

old_env_path =''

def run_test(ompi_base, pmix_base_run, pmix_base_lib, base_dir_name, max_nodes):
    os.environ['PATH']  = ompi_base + '/bin:' + old_env_path
    os.environ['LD_LIBRARY_PATH'] = ompi_base + '/lib:' + pmix_base_lib

    print(os.environ['PATH'], os.environ['LD_LIBRARY_PATH'])

    key_length = 50
    key_count = 100
    iter = 6
    for np in range(2, max_nodes + 1, 2):
        dir_name = str(key_length) + '_' + str(key_count) + '_' + str(np)
    
        for idx in range(1, iter):
            filename = base_dir_name + str(np) + '/' + dir_name + '/rez_' + str(key_length) + '_' + str(key_count) + '_' + str(idx)
            process = subprocess.run(['mpirun', '-n', str(np), '--bind-to', 'core', '--output-filename',
    			                filename, pmix_base_run + 'pmix_intra_perf', '-s', 
                                        str(key_length), '-c', str(key_count)], 
                                        stdout=subprocess.PIPE, universal_newlines=True)
#        for idy in range(1, np):
#    	    os.remove(filename+'.1.' + str(idy))

old_env_path = os.environ['PATH']
max_nodes = 28
deploy_dir_name = 'deploy'
abs_path_name = os.path.abspath(os.getcwd()) + '/' + deploy_dir_name
base_dir_name = 'v315/'
ompi_base = abs_path_name + '/install/openmpi_v403'
pmix_base = 'pmix_v315'
pmix_base_run = abs_path_name + '/sources/' + pmix_base + '/contrib/perf_tools/'
pmix_base_lib = abs_path_name + '/install/' + pmix_base + '/lib'
run_test(ompi_base, pmix_base_run, pmix_base_lib, base_dir_name, max_nodes)

#base_dir_name = 'euro2018_poc/'
#ompi_base = abs_path_name + '/install/openmpi_poc'
#pmix_base = 'pmix_poc'
#pmix_base_run = abs_path_name + '/sources/' + pmix_base + '/contrib/perf_tools/'
#pmix_base_lib = abs_path_name + '/install/' + pmix_base + '/lib'
#run_test(ompi_base, pmix_base_run, pmix_base_lib, base_dir_name, max_nodes)

#base_dir_name = 'euro2018_poc_base/'
#ompi_base = abs_path_name + '/install/openmpi_poc_base'
#pmix_base = 'pmix_poc_base'
#pmix_base_run = abs_path_name + '/sources/' + pmix_base + '/contrib/perf_tools/'
#pmix_base_lib = abs_path_name + '/install/' + pmix_base + '/lib'
#run_test(ompi_base, pmix_base_run, pmix_base_lib, base_dir_name, max_nodes)

#base_dir_name = 'euro2018_poc_base_lockless/'
#ompi_base = abs_path_name + '/install/openmpi_poc_base_lockless'
#pmix_base = 'pmix_poc_base_lockless'
#pmix_base_run = abs_path_name + '/sources/' + pmix_base + '/contrib/perf_tools/'
#pmix_base_lib = abs_path_name + '/install/' + pmix_base + '/lib'
#run_test(ompi_base, pmix_base_run, pmix_base_lib, base_dir_name, max_nodes)

