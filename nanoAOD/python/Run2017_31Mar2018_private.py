import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser
    
# Logging
if __name__=="__main__":
    import nanoMET.tools.logger as logger
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
dbFile = dbDir+"/DB_Run2017_31Mar2018_private.sql"

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2017B_31Mar2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2017B_31Mar2018", "/DoubleMuon/schoef-crab_Run2017B-31Mar2018-v1_legacy_nano_v4-ef59f0c1717f190a6e4b4df4955a4722/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017C_31Mar2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2017C_31Mar2018", "/DoubleMuon/schoef-crab_Run2017C-31Mar2018-v1_legacy_nano_v4-ef59f0c1717f190a6e4b4df4955a4722/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017D_31Mar2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2017D_31Mar2018", "/DoubleMuon/schoef-crab_Run2017D-31Mar2018-v1_legacy_nano_v4-ef59f0c1717f190a6e4b4df4955a4722/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017E_31Mar2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2017E_31Mar2018", "/DoubleMuon/schoef-crab_Run2017E-31Mar2018-v1_legacy_nano_v4-ef59f0c1717f190a6e4b4df4955a4722/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017F_31Mar2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2017F_31Mar2018", "/DoubleMuon/schoef-crab_Run2017F-31Mar2018-v1_legacy_nano_v4-ef59f0c1717f190a6e4b4df4955a4722/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2017B_31Mar2018,
    DoubleMuon_Run2017C_31Mar2018,
    DoubleMuon_Run2017D_31Mar2018,
    DoubleMuon_Run2017E_31Mar2018,
    DoubleMuon_Run2017F_31Mar2018,
]

allSamples = DoubleMuon

for s in allSamples:
    s.json   = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt")
    s.isData = True

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
