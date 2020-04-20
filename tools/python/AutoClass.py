''' class that stores all arguments as attributes
'''
        
import os, sys
import subprocess
from multiprocessing import Pool

def copy( job ):
    source, target = job
    cmd = ["/usr/bin/rfcp",  source, target]
    dir = os.path.dirname( target )
    if not os.path.exists(dir):
        #try:
            os.makedirs(dir)
        #except:
        #    pass
            
    if not os.path.exists(target):
        print ( " ".join( cmd ) )
        subprocess.call(cmd)
    else:
        print( "Found %s. Skip.", target)

def echo( job ):
    source, target = job
    cmd = ["/usr/bin/xrdcp", source, target ]
    print (" ".join( cmd ))

def checkFile( job ):
    from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile
    filename = job
    if filename.startswith('root://'):
        if not (checkRootFile( filename, checkForObjects = ["Events"]) and deepCheckRootFile( filename )):
            return str(filename)
    else:
        if not (os.path.exists(filename) and os.stat(filename).st_size > 0 and checkRootFile( filename, checkForObjects = ["Events"]) and deepCheckRootFile( filename )):
            return str(filename)

## Logger
#import logging
#logger = logging.getLogger(__name__)

class AutoClass:
    def __init__( self, samples):
        for s in samples:
            setattr( self, s.name, s )

        self.__samples = samples

        names = [ s.name for s in samples ]
        for name in names:
            if names.count( name )>1:
                raise RuntimeError( "Sample name is not unique: %s", name )

    def find( self, name ):
        for s in self.__samples:
            if s.name == name:
                return s.DASname
            if s.DASname == name:
                return s.name 

    def copy_to_local( self, path = "/data/dpm/", n_processes = 4, do_it = False):
        import os
        if not path.endswith('/'): path+='/'
        jobs = []
        for sample in self.__samples:
            for source in sample.files:
                _source = os.path.join( "/dpm/oeaw.ac.at/home/cms", ("".join( source.split('//')[2:])).lstrip('/') )
                _target = os.path.join( path, ("".join( source.split('//')[2:])).lstrip('/') )
                jobs.append( [_source, _target] )

        pool = Pool(processes = n_processes)
        if do_it:
            results = pool.map(copy, jobs)
        else:
            results = pool.map(echo, jobs)
        pool.close()
        pool.join()

    def check_completeness( self, cores=1 ):

        jobs = []
        for sample in self.__samples:
            for filename in sample.files:
                jobs.append( filename )

        if cores==1:
            failed = map(checkFile, jobs)
        else:
            pool = Pool( processes=cores )
            failed = pool.map( checkFile, jobs )
            pool.close()
            pool.join()

        failed = filter( lambda res: res, failed )

        if len(failed)>0:
            for filename in failed:
                print filename
            raise RuntimeError("Found %i missing files!"%len(failed)) 
