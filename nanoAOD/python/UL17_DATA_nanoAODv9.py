import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
from nanoMET.tools.user import redirector_global as redirector

# DB
from nanoMET.tools.user import dbDir
dbFile = dbDir+'/DB_UL17_DATA_nanoAODAPVv9.sql'

logger.info("Using db file: %s", dbFile)


################################################################################
# Double Muon
DoubleMuon_Run2017B  = Sample.nanoAODfromDAS("DoubleMuon_Run2017B", "/DoubleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017C  = Sample.nanoAODfromDAS("DoubleMuon_Run2017C", "/DoubleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017D  = Sample.nanoAODfromDAS("DoubleMuon_Run2017D", "/DoubleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017E  = Sample.nanoAODfromDAS("DoubleMuon_Run2017E", "/DoubleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017F  = Sample.nanoAODfromDAS("DoubleMuon_Run2017F", "/DoubleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017 = [DoubleMuon_Run2017B, DoubleMuon_Run2017C, DoubleMuon_Run2017D, DoubleMuon_Run2017E, DoubleMuon_Run2017F]


################################################################################

allSamples = DoubleMuon_Run2017 

for s in allSamples:
    s.isData = True
    s.json = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt")

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
