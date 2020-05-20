import os
import subprocess

ompi_base = "/opt/test/openmpi_euro2018_poc_base_lockless"
pmix_libs = "/opt/test/pmix_euro2018_poc_base_lockless/lib"
base_dir_name = "euro2018_poc_base_lockless_test/"

os.environ['PATH']  = ompi_base + '/bin:' + os.environ['PATH']
os.environ['LD_LIBRARY_PATH'] = ompi_base + '/lib:' + pmix_libs

#print(os.environ['PATH'], os.environ['LD_LIBRARY_PATH'])


np = 8
key_length = 50

for key_count in range(500,701, 100):
    dir_name = str(key_length) + '_' + str(key_count)
    
    for idx in range(1,51):
        filename = base_dir_name + str(np) + '/' + dir_name + '/rez_' + str(key_length) + '_' + str(key_count) + '_' + str(idx)
        process = subprocess.run(['mpirun', '-n', str(np), '--bind-to', 'core', '--output-filename',
    			     filename,'./pmix_intra_perf', '-s', 
                            str(key_length), '-c', str(key_count)], 
                            stdout=subprocess.PIPE, universal_newlines=True)
#        for idy in range(1, np):
#    	    os.remove(filename+'.1.' + str(idy))
