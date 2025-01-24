from FWCore.ParameterSet.VarParsing import VarParsing
import FWCore.ParameterSet.Config as cms
options = VarParsing('python')

options.register('isMC', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('globalTag', 'NOTSET',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Set global tag"
)
options.register('wantSummary', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('wantFullRECO', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('reportEvery', 1000,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "report every N events"
)
options.register('skip', 0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "skip first N events"
)
options.register('lhcRun', 2,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "LHC Run 2 or 3 (default)"
)

options.setDefault('maxEvents', -1)
options.setDefault('tag', '124X')
options.parseArguments()
print(options)

globaltag = None
if   options.lhcRun == 3: globaltag = '124X_mcRun3_2022_realistic_v11' if options.isMC else '124X_dataRun3_Prompt_v4'
elif options.lhcRun == 2: globaltag = '106X_upgrade2018_realistic_v16_L1v1' if options.isMC else '102X_dataRun2_v11'
if options._beenSet['globalTag']: globaltag = options.globalTag

ext1 = {2:'Run2', 3:'Run3'}
ext2 = {False:'data', True:'mc'}
outputFileNANO = cms.untracked.string('_'.join(['BParkingNANO',
                                                ext1[options.lhcRun],
                                                ext2[options.isMC],
                                                options.tag])+'.root')
outputFileFEVT = cms.untracked.string('_'.join(['BParkingFullEvt',
                                                ext1[options.lhcRun],
                                                ext2[options.isMC],
                                                options.tag])+'.root')
if not options.inputFiles:
     if options.lhcRun == 2:
        options.inputFiles = [
#'/store/mc/RunIISummer20UL18MiniAODv2/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/002F46B9-4287-194A-BA9B-469CFB34D146.root'
'/store/mc/RunIISummer20UL18MiniAODv2/GluGluHToBB_M-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/009776A3-959E-E544-AD66-211B0904441B.root',
        ] if options.isMC else [
         #  '/store/data/Run2018A/ParkingBPH1/MINIAOD/UL2018_MiniAODv2-v1/2430000/004BEEAD-CCCD-4A4F-9217-91A5A28EA0C8.root'
           'file:CFECF302-2EA1-8142-9981-1CE893918001.root'
	]
      #  options.inputFiles =cms.untracked.string(':'.join("file", options.infile))#'/store/mc/RunIISummer20UL18MiniAODv2/ZprimeToBB_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/16DD2093-2D82-8145-BB8F-7BB4DD3B3919.root'#'/store/mc/RunIISummer20UL18MiniAODv2/VectorZPrimeToQQ_M150_pT300_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/14F189A8-4903-4F4A-8BED-E56A0DE7E328.root'#'/store/mc/RunIISummer20UL18MiniAODv2/GluGluHToBB_M-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/009776A3-959E-E544-AD66-211B0904441B.root'#'/store/mc/RunIISummer20UL18MiniAOD/GluGluHToBB_M-125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/120000/0317A529-0086-E240-A702-BDC8617668AE.root'#'/store/mc/RunIISummer20UL18MiniAODv2/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/004EF875-ACBB-FE45-B86B-EAF83448CE62.root'
        #options.inputFiles = ['file:/pnfs/psi.ch/cms/trivcat/store/user/ratramon/GluGluSpin0ToBBbar_W_1p0_M_50/pnfs/psi.ch/cms/trivcat/store/user/ratramon/GluGluSpin0ToBBbar_W_1p0_M_50//RunIISummer20UL18_MINI/240815_194300/0000/MINI_10.root'#'/store/mc/RunIISummer20UL18MiniAODv2/ZprimeToBB_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/16DD2093-2D82-8145-BB8F-7BB4DD3B3919.root'#'/store/mc/RunIISummer20UL18MiniAODv2/VectorZPrimeToQQ_M150_pT300_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/14F189A8-4903-4F4A-8BED-E56A0DE7E328.root'#'/store/mc/RunIISummer20UL18MiniAODv2/GluGluHToBB_M-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/009776A3-959E-E544-AD66-211B0904441B.root'#'/store/mc/RunIISummer20UL18MiniAOD/GluGluHToBB_M-125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/120000/0317A529-0086-E240-A702-BDC8617668AE.root'#'/store/mc/RunIISummer20UL18MiniAODv2/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/004EF875-ACBB-FE45-B86B-EAF83448CE62.root'
        #  '/store/mc/RunIISummer20UL18MiniAODv2/BuToJpsiK_BMuonFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/0B472EDE-5100-1745-AFFA-478292A594EC.root'
            #'/store/mc/RunIISummer20UL18MiniAOD/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/230000/015912D7-514B-D044-9EAE-B6B703271379.root'#'/store/mc/Run3Summer22MiniAODv3/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2810000/07aa4e3f-b82a-41b5-b675-1c0b193a2c9e.root'#'/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/5AD092A6-C434-BB43-838E-325010B08718.root'#'/store/mc/RunIIAutumn18MiniAOD/BuToKJpsi_ToMuMu_probefilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PUPoissonAve20_BParking_102X_upgrade2018_realistic_v15-v2/120000/04E29E35-AB3C-8542-A210-E1F9F4A4D602.root'
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/01799CFD-BA2E-844B-87CB-273185CF1A4A.root',
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CFBFCA29-1649-2345-970E-731824064446.root',
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2EA135EF-43C9-624B-A50B-B72B2E2D5393.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A386A139-01EC-3C4C-AB48-F2FC8814FDF2.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/23EBA0E0-6729-7C41-9888-F8E07B20C677.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5A00A84C-ED50-B94B-A25D-EE2A6EAD3D4C.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/7010DF71-3814-3047-8786-3A3A894D0E02.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F338472B-D37A-8040-B482-111D21820AD7.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/DE59C01E-2184-334D-A77A-6D5B18697B02.root', 
#'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F7C64AA3-BA68-0F4D-B845-D59C363DF441.root', 
#'/store/mc/RunIISummer20UL18MiniAODv2/QCD_HT200to300_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/36E1C10A-F287-A74E-B874-6C359FACD755.root'
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/2C416EBB-5DEE-E811-B2B4-D48564592B02.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/14A607B2-5DEE-E811-B6B1-509A4C74D08F.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/3A86E8AC-5DEE-E811-8B2F-002590907826.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/988407DC-5DEE-E811-A28C-A4BF0101DB93.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/C074AF04-2BED-E811-B7D8-0CC47AFCC6A6.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/1A79E2C6-5DEE-E811-8692-0025905C3D6C.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/F4947FA5-25EC-E811-BE29-90B11C0DCA4B.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/D2946C2A-35EC-E811-94D2-002590E3A224.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/5A82EFA7-3CEC-E811-876D-0CC47AD98B8E.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/E0B52B60-48EC-E811-8B72-0CC47AD98D6E.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/90F5498C-59EC-E811-B2D1-1C6A7A26BCDB.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/54CA8ECF-4BED-E811-AD93-002590E39D52.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/1876BAD5-5DEE-E811-BE0C-0CC47AD9908C.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/28FEBABF-3CEC-E811-90CF-002590D9D8AE.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/E8F803A0-80EC-E811-98D3-0CC47AB0B704.root',
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToQQ_HT180_13TeV_TuneCP5-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/7C54C8B8-B7ED-E811-804F-002590FD5A72.root'
#] if options.isMC else [
 #       '/store/data/Run2018A/ParkingBPH1/MINIAOD/UL2018_MiniAODv2-v1/2430000/004BEEAD-CCCD-4A4F-9217-91A5A28EA0C8.root'
 #       ]
     elif options.lhcRun == 3:
        options.inputFiles = [#"/store/mc/RunIISummer20UL18MiniAODv2/EWKZ2Jets_ZToQQ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/00A69977-5A1C-8F4F-8E7C-8A05CA941E2C.root"
           '/store/mc/Run3Summer22EEMiniAODv3/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_postEE_v1-v1/2810000/00ab8c49-364e-4841-9070-914e15ed2d2f.root'
         #  '/store/mc/Run3Summer22EEMiniAODv4/QCD_Pt-120To170_TuneCP5_13p6TeV-pythia8/MINIAODSIM/Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/30000/0a67438e-76e7-4113-9206-2ecc667d63e7.root'
 #           '/store/mc/Run3Summer22MiniAODv3/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v1/2810000/bb973608-0565-4bd9-8539-1979e62d7e02.root'
            #'/store/mc/Run3Summer22MiniAODv3/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/80000/2146456c-2cd1-4390-bc6b-5df3e88fe56b.root'
           # '/store/mc/RunIISummer20UL18MiniAODv2/BuToJpsiK_BMuonFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/023A3977-8631-5D49-AEE4-D750DE066C8A.root'
            #'/store/mc/Run3Summer22MiniAODv3/ButoJpsiK_Jpsito2Mu_MuFilter_TuneCP5_13p6TeV_pythia8-evtgen/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2520000/0965bd20-fa2e-493f-be35-4bebeeaaffbe.root'
         #   '/store/mc/Run3Summer22MiniAODv3/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2810000/07aa4e3f-b82a-41b5-b675-1c0b193a2c9e.root'
        ] if options.isMC else [
            "/store/mc/RunIISummer20UL18MiniAODv2/EWKZ2Jets_ZToQQ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/00A69977-5A1C-8F4F-8E7C-8A05CA941E2C.root"
            #'/store/data/Run2022F/ParkingSingleMuon0/MINIAOD/PromptReco-v1/000/360/390/00000/2c1a8864-bc25-4b39-9601-b2d6250652b4.root'
        ]
annotation = '%s nevts:%d' % (outputFileNANO, options.maxEvents)

# Process
from Configuration.StandardSequences.Eras import eras
from PhysicsTools.BParkingNano.modifiers_cff import *
process = None
if   options.lhcRun == 3: process = cms.Process('BParkNANO',eras.Run3,BToKEE_DiEle)
elif options.lhcRun == 2: process = cms.Process('BParkNANO',eras.Run2_2018)

# import of standard configurations
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('PhysicsTools.BParkingNano.nanoBPark_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents=cms.untracked.uint32(options.skip),
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(options.wantSummary),
)

process.nanoMetadata.strings.tag = annotation
# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string(annotation),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = outputFileFEVT,
    outputCommands = (cms.untracked.vstring(
        'keep *',
        'drop *_*_SelectedTransient*_*',
                     )),
    splitLevel = cms.untracked.int32(0)
)

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = outputFileNANO,
    outputCommands = cms.untracked.vstring(
      'drop *',
      "keep nanoaodFlatTable_*Table*_*_*",     # event data
      "keep nanoaodUniqueString_nanoMetadata_*_*",   # basic metadata
    )

)


# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globaltag, '')

from PhysicsTools.BParkingNano.nanoBPark_cff import *
if options.lhcRun == 2:
    process =nanoAOD_customizeTriggerBitsBPark(process)
    process = nanoAOD_customizeMuonTriggerBPark(process)
    process = nanoAOD_customizeElectronFilteredBPark(process)
    process = nanoAOD_customizeTrackFilteredBPark(process)
#    process = nanoAOD_customizeBToKLL(process)
    process = nanoAOD_customizePho(process)
    #process = nanoAOD_customizeBToKstarEE(process)
    #process = nanoAOD_customizeBToKstarMuMu(process)
elif options.lhcRun == 3:
    process = nanoAOD_customizeMuonTriggerBPark(process)
    process = nanoAOD_customizeElectronFilteredBPark(process)
    process = nanoAOD_customizeTriggerBitsBPark(process)
    process = nanoAOD_customizeTrackFilteredBPark(process)
    process = nanoAOD_customizeBToKLL(process)
    process = nanoAOD_customizeTagAndProbeJPsiToMuMu(process,isMC= options.isMC)

if options.isMC:
    from PhysicsTools.BParkingNano.nanoBPark_cff import nanoAOD_customizeMC
    nanoAOD_customizeMC(process, ancestor_particles=[511, 521, 531, 541], addTriggerMuonCollection=True, addProbeTracksCollection=False) 

# Path and EndPath definitions
if options.lhcRun == 2:
    process.nanoAOD_Jets_step = cms.Path(process.nanoSequence)
    #process.nanoAOD_BToKMuMu_step = cms.Path(process.nanoSequence+process.nanoTracksSequence+ process.nanoBKMuMuSequence + CountBToKmumu)
   # process.nanoAOD_BToKee_step = cms.Path(process.nanoSequence+process.nanoTracksSequence+ process.nanoBKeeSequence + CountBToKee)
    process.nanoAOD_pho_step = cms.Path(process.nanoSequence+process.nanoPhoton)

   #process.nanoAOD_KMuMu_step = cms.Path(process.nanoSequence + process.nanoTracksSequence + process.nanoBKMuMuSequence + CountBToKmumu )
    #process.nanoAOD_Kee_step   = cms.Path(process.nanoSequence + process.nanoTracksSequence + process.nanoBKeeSequence   + CountBToKee   )
    #process.nanoAOD_KstarMuMu_step = cms.Path(process.nanoSequence + process.nanoTracksSequence + process.KstarToKPiSequence + process.nanoBKstarMuMuSequence + CountBToKstarMuMu )
    #process.nanoAOD_KstarEE_step  = cms.Path(process.nanoSequence + process.nanoTracksSequence + process.KstarToKPiSequence + process.nanoBKstarEESequence + CountBToKstarEE  )
elif options.lhcRun == 3:
    process.nanoAOD_BToKMuMu_step = cms.Path(process.nanoSequence+process.nanoTracksSequence+ process.nanoBKMuMuSequence + CountBToKmumu)
    process.nanoAOD_BToKee_step = cms.Path(process.nanoSequence+process.nanoTracksSequence+ process.nanoBKeeSequence + CountBToKee
                                          #+process.nanoDiEleSequence
                                          #+process.nanoTracksSequence
                                          #+process.nanoBKeeSequence
                                          #+CountBToKee
                                          )

#    process.nanoAOD_tnpJPsiMuMu_step = cms.Path(process.nanoSequence + process.nanoJPsiToMuMuSequence + CountJPsiToMuMu)# customisation of the process.
if options.isMC:
    from PhysicsTools.BParkingNano.nanoBPark_cff import nanoAOD_customizeMC
    nanoAOD_customizeMC(process)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
if options.lhcRun == 3:

    process.schedule = cms.Schedule(process.nanoAOD_BToKMuMu_step,
                                    process.endjob_step,
                                    process.NANOAODoutput_step)
    if options.wantFullRECO:
        process.schedule = cms.Schedule(process.nanoAOD_BToKMuMu_step,
                                        process.endjob_step,
                                        process.FEVTDEBUGHLToutput_step,
                                        process.NANOAODoutput_step)
    from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
    associatePatAlgosToolsTask(process)
    process.NANOAODoutput.SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('nanoAOD_BToKMuMu_step')
    )

elif options.lhcRun == 2:

    process.schedule = cms.Schedule(
        process.nanoAOD_pho_step,
      #  process.nanoAOD_BToKee_step,
      #  process.nanoAOD_BToKMuMu_step,
        #process.nanoAOD_KstarMuMu_step,
        #process.nanoAOD_KstarEE_step,
        process.endjob_step,
        process.NANOAODoutput_step
    )
    if options.wantFullRECO:
        process.schedule = cms.Schedule(
            process.nanoAOD_BToKMuMu_step,
            process.nanoAOD_BToKee_step,
            #process.nanoAOD_Kee_step,
            #process.nanoAOD_KstarMuMu_step,
            #process.nanoAOD_KstarEE_step,
            process.endjob_step,
            process.FEVTDEBUGHLToutput_step,
            process.NANOAODoutput_step
        )
    from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
    associatePatAlgosToolsTask(process)
    process.NANOAODoutput.SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'nanoAOD_pho_step',
     #       'nanoAOD_BToKMuMu_step',
     #       'nanoAOD_BToKee_step',
            #'nanoAOD_KstarMuMu_step',
            #'nanoAOD_KstarEE_step',
        )
    )

### from https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/3287/1/1/1/1/1.html
process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))
process.NANOAODoutput.fakeNameForCrab=cms.untracked.bool(True)

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
