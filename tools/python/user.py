import os

if os.environ['USER'] in ['dspitzbart', 'dspitzba']:
    plot_directory          = "/afs/hephy.at/user/d/dspitzbart/www/nanoMET/"
    data_directory          = "/afs/hephy.at/data/dspitzbart03/nanoSamples/"
    postprocessing_output_directory = "/afs/hephy.at/data/dspitzbart03/nanoSamples/"
    
if os.environ['USER'] in ['llechner']:
    plot_directory                  = "/eos/user/l/llechner/www/nanoMET/"
    data_directory                  = "/eos/cms/store/group/phys_susy/hephy/nanoMET/"
    postprocessing_output_directory = "/eos/cms/store/group/phys_susy/hephy/nanoMET/"
    
dbDir = '%s/src/nanoMET/tools/cache/'%os.environ['CMSSW_BASE']
redirector_global = 'root://cms-xrd-global.cern.ch/'

