import os

def getPaths():
    PREFIX = os.environ['PROTEUS_PREFIX']
    INCDIR = PREFIX+'/'+'include'
    LIBDIR = PREFIX+'/'+'lib'

    # HDF5 paths
    HDF5_keys = ['HDF5_dir', 'HDF5_incdir', 'HDF5_libdir']
    HDF5_dirs = [PREFIX, INCDIR, LIBDIR]
    HDF5_dict = {}
    index = 0
    for key in HDF5_keys:
        HDF5_dict[key] = HDF5_dirs[index]
        index+=1

    # szip paths
    szip_keys = ['szip_dir', 'szip_incdir', 'szip_incdir']
    szip_dirs = [PREFIX, INCDIR, LIBDIR]
    szip_dict = {}
    index = 0
    for key in szip_keys:
        szip_dict[key] = szip_dirs[index]
        index+=1

    # netCDF paths
    netCDF4_keys = ['netCDF4_dir','netCDF4_incdir','netCDF4_libdir']
    netCDF4_dirs = [PREFIX, INCDIR, LIBDIR]
    netCDF4_dict = {}
    index = 0
    for key in netCDF4_keys:
        netCDF4_dict[key] = netCDF4_dirs[index]
        index+=1

    return HDF5_dict, szip_dict, netCDF4_dict


def generate_setup_cfg(HDF5_dict, szip_dict, netCDF4_dict):
    """ Initialize input/out for setup.cfg file"""
    f = open('setup.cfg', 'w')

    output = {}
    comments = ['# path to nc-config script.','# HDF5 directories path',
                '# szip directories path','# netCDF4 directories path']
    
    output['options'] = '[options]'
    output['directories'] = '[directories]'
    output['ncconfigFlag'] = 'use_ncconfig=True'
    output['ncconfigComment'] = comments[0]
    output['ncconfigPath'] = os.environ['PROTEUS_PREFIX']+'/'+'bin'+'/'+'nc-config'

    # Preamble
    f.write(output['options']+'\n')
    f.write(output['ncconfigFlag']+'\n')
    f.write(output['ncconfigComment']+'\n')
    f.write('ncconfg'+'='+output['ncconfigPath']+'\n')

    #Directories
    f.write(output['directories']+'\n')
    f.write(comments[1]+'\n')
    for key in HDF5_dict.keys():
        dirVariable = key+'='+HDF5_dict[key]
        f.write(dirVariable+'\n')

    f.write(comments[2]+'\n')
    for key in szip_dict.keys():
        dirVariable = key+'='+szip_dict[key]
        f.write(dirVariable+'\n')

    f.write(comments[3]+'\n')
    for key in netCDF4_dict.keys():
        dirVariable = key+'='+netCDF4_dict[key]
        f.write(dirVariable+'\n')

    f.close()

if __name__=='__main__':
    """ Script that generates a setup.cfg file which will 
        read system variable PROTEUS_PREFIX and write in
        the necessary include and library directories for
        HDF5, szip, and netCDF4. """
    
    [HDF5_dict, szip_dict, netCDF4_dict] = getPaths()

    generate_setup_cfg(HDF5_dict, szip_dict, netCDF4_dict)
