# nanoMET
Repository to use nanoAOD tuples to tune MET Significance, and produce validation plots

A detailed description can be found here:
https://twiki.cern.ch/twiki/bin/view/CMS/METSignificance

Recipe:

# CMSSW
```
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src/
cmsenv
git cms-init
```

# get all the packages
```
cd $CMSSW_BASE/src
git clone https://github.com/HephyAnalysisSW/RootTools.git
```

# nanoAOD-tools
```
cd $CMSSW_BASE/src
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
cd PhysicsTools/NanoAODTools
git remote add metsig https://github.com/cesarecazzaniga/nanoAOD-tools.git
git fetch metsig
git checkout metsig/MetSig_devel
```

# nanoMET
```
cd $CMSSW_BASE/src
git clone https://github.com/cesarecazzaniga/nanoMET.git
scram b -j 8
```

