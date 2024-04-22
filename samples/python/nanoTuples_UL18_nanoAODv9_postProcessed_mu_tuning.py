import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT
from nanoMET.samples.color import color

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
try:
    data_directory = sys.modules['__main__'].data_directory
except:
    from nanoMET.tools.user import data_directory as user_data_directory
    data_directory = user_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except:
  postProcessing_directory = "2018_UL_v9/singlemu_afterTuning/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}

dirs['DY_LO']           = ["DYJetsToLL_M50"]
dirs['Top']             = ["TToLeptons_sch_amcatnlo","T_tWch","TBar_tWch","T_tch_pow","TBar_tch_pow"] #"TTLep_pow"
dirs['diboson']         = ['WZTo3LNu']
dirs['triboson']        = ['WWW_4F','WZZ', 'ZZZ']
dirs['QCD']             = ['QCD_HT100to200','QCD_HT200to300','QCD_HT300to500','QCD_HT500to700','QCD_HT700to1000','QCD_HT1000to1500','QCD_HT1500to2000','QCD_HT2000toInf']
dirs['WJets']           = ['WJetsToLNu_HT70to100','WJetsToLNu_HT100to200','WJetsToLNu_HT200to400','WJetsToLNu_HT400to600','WJetsToLNu_HT600to800','WJetsToLNu_HT800to1200','WJetsToLNu_HT1200to2500']


directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

DY_LO_18            = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,            texName="DY (LO)",                  directory=directories['DY_LO'])
Top_18              = Sample.fromDirectory(name="Top",              treeName="Events", isData=False, color=color.TTJets,        texName="t(#bar{t})",               directory=directories['Top'])
diboson_18          = Sample.fromDirectory(name="diboson",          treeName="Events", isData=False, color=color.diboson,       texName="diboson",                  directory=directories['diboson'])
rare_18             = Sample.fromDirectory(name="rare",             treeName="Events", isData=False, color=color.rare,          texName="rare",                     directory=directories['triboson'])
QCD_18              = Sample.fromDirectory(name="QCD",              treeName="Events", isData=False, color=color.QCD,           texName="QCD",                      directory=directories['QCD'])
WJets_18            = Sample.fromDirectory(name="WJets",            treeName="Events", isData=False, color=color.WJets,         texName="WJets",                    directory=directories['WJets'])