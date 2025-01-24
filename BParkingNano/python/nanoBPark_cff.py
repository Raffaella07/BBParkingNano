from __future__ import print_function
import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.globals_cff import *
#from PhysicsTools.NanoAOD.nano_cff import *
from PhysicsTools.NanoAOD.genWeightsTable_cfi import *
from PhysicsTools.NanoAOD.vertices_cff import *
from PhysicsTools.NanoAOD.NanoAODEDMEventContent_cff import *
from PhysicsTools.BParkingNano.trgbits_cff import *
from PhysicsTools.NanoAOD.taus_cff import *
from PhysicsTools.NanoAOD.photons_cff import *
from PhysicsTools.NanoAOD.boostedTaus_cff import *
#from PhysicsTools.NanoAOD.jetsAK4_CHS_cff import *
from PhysicsTools.NanoAOD.jets_cff import *
#from PhysicsTools.NanoAOD.jetsAK4_Puppi_cff import *
#from PhysicsTools.NanoAOD.jetMC_cff import *
from PhysicsTools.NanoAOD.muons_cff import *

##for gen and trigger muon
from PhysicsTools.BParkingNano.genparticlesBPark_cff import *
from PhysicsTools.BParkingNano.particlelevelBPark_cff import *
from PhysicsTools.BParkingNano.triggerObjectsBPark_cff import *
from PhysicsTools.BParkingNano.muonsBPark_cff import * 

## filtered input collections
from PhysicsTools.BParkingNano.electronsBPark_cff import * 
from PhysicsTools.BParkingNano.tracksBPark_cff import *

## B collections
from PhysicsTools.BParkingNano.BToKLL_cff import *
from PhysicsTools.BParkingNano.BToKstarLL_cff import *
from PhysicsTools.BParkingNano.tagAndProbeJPsiMuMu_cff import * 

nanoMetadata = cms.EDProducer("UniqueStringProducer",
    strings = cms.PSet(
        tag = cms.string("untagged"),
    )
)
linkedObjectsNew = cms.EDProducer("PATObjectCrossLinker",
   jets=cms.InputTag("finalJets"),
   muons=cms.InputTag("muonTrgSelector:SelectedMuons"),
   electrons=cms.InputTag("slimmedElectrons"),
   lowPtElectrons=cms.InputTag(""),
   taus=cms.InputTag("slimmedTaus"),
   boostedTaus=cms.InputTag(""),
   photons=cms.InputTag("slimmedPhotons"),
   vertices=cms.InputTag("slimmedSecondaryVertices")
)

nanoSequenceOnlyFullSim = cms.Sequence(triggerObjectBParkTables + l1bits)

nanoSequenceCommon = cms.Sequence(nanoMetadata +
                                 muonBParkSequence + cms.Sequence(tauTask) +
                                 jetSequence +                                       # dont know how to handle the muonsubptraw missing
                                 #cms.Sequence(jetTask) +
                                 linkedObjectsNew +
                                 jetTables+
                            cms.Sequence(vertexTask) + 
                            cms.Sequence(globalTablesTask) + cms.Sequence(vertexTablesTask)+triggerObjectBParkTables + l1bits)
nanoSequence = cms.Sequence(nanoSequenceCommon + nanoSequenceOnlyFullSim)

nanoTableTask = cms.Task(globalTablesMCTask,genWeightsTableTask)
nanoSequenceMC = cms.Sequence(particleLevelBParkSequence + genParticleBParkSequence + nanoSequenceCommon + jetMC + genTable + genFilterTable 
                                + genParticleBParkTables + lheInfoTable +cms.Sequence(nanoTableTask))

from PhysicsTools.BParkingNano.electronsTrigger_cff import *
def nanoAOD_customizeDiEle(process):
    process.nanoDiEleSequence = cms.Sequence(
        myUnpackedPatTrigger
        +myTriggerMatches
        +mySlimmedElectronsWithEmbeddedTrigger
        +electronTrgSelector
        +countTrgElectrons)
    return process



def nanoAOD_customizeMuonTriggerBPark(process):
    process.nanoSequence = cms.Sequence( process.nanoSequence + muonBParkSequence + muonBParkTables)#+ muonTriggerMatchedTables)   ###comment in this extra table in case you want to create the TriggerMuon collection again.
    return process

def nanoAOD_customizeTrackFilteredBPark(process):
    process.nanoTracksSequence = cms.Sequence( tracksBParkSequence + tracksBParkTables)
    return process

def nanoAOD_customizeElectronFilteredBPark(process):
    process.nanoBKeeSequence     = cms.Sequence( electronsBParkSequence + electronBParkTables)
    process.nanoBKstarEESequence = cms.Sequence( electronsBParkSequence + electronBParkTables)
    return process

def nanoAOD_customizeTriggerBitsBPark(process):
    process.nanoSequence = cms.Sequence( process.nanoSequence + trgTables)
    return process

def nanoAOD_customizePho(process):
    process.nanoPhoton = cms.Sequence(photonTablesTask)
    return process

def nanoAOD_customizeBToKLL(process):
    process.nanoBKeeSequence   = cms.Sequence( process.nanoBKeeSequence + BToKEESequence    + BToKeeTable   )
    process.nanoBKMuMuSequence = cms.Sequence( BToKMuMuSequence + BToKmumuTable )
    return process

#three possibilities for K*LL
def nanoAOD_customizeBToKstarLL(process):
    #process.nanoBKstarLLSequence   = cms.Sequence( KstarToKPiSequence + BToKstarLLSequence + KstarToKPiTable + BToKstarLLTables )
    return process

def nanoAOD_customizeBToKstarEE(process):
    #process.nanoBKstarEESequence   = cms.Sequence( process.nanoBKstarEESequence + BToKstarEESequence + BToKstarEETable + KstarToKPiTable )
    return process

def nanoAOD_customizeBToKstarMuMu(process):
    #process.nanoBKstarMuMuSequence = cms.Sequence( BToKstarMuMuSequence + BToKstarMuMuTable + KstarToKPiTable )
    return process
def nanoAOD_customizeTagAndProbeJPsiToMuMu(process, isMC=False):
    if isMC == False:
      process.nanoJPsiToMuMuSequence = cms.Sequence( JPsiToMuMuSequence + JPsiToMuMuTable )
    else:
      process.nanoJPsiToMuMuSequence = cms.Sequence( JPsiToMuMuSequenceMC + JPsiToMuMuTable )
    return process

from FWCore.ParameterSet.MassReplace import massSearchReplaceAnyInputTag

def nanoAOD_customizeMC(process, ancestor_particles=[511, 521, 531, 541], addTriggerMuonCollection=False, addProbeTracksCollection=False):
    for name, path in process.paths.iteritems():
        # replace all the non-match embedded inputs with the matched ones
        massSearchReplaceAnyInputTag(path, 'muonTrgSelector:SelectedMuons', 'selectedMuonsMCMatchEmbedded')
       # massSearchReplaceAnyInputTag(path, 'muonTrgSelector:trgMuons', 'triggerMuonsMCMatchEmbedded')
        #massSearchReplaceAnyInputTag(path, 'electronTrgSelector:SelectedElectrons', 'selectedElectronsMCMatchEmbedded') # Is this needed if the trigger is emulated ???
        massSearchReplaceAnyInputTag(path, 'electronsForAnalysis:SelectedElectrons', 'selectedElectronsMCMatchEmbedded')
        massSearchReplaceAnyInputTag(path, 'tracksBPark:SelectedTracks', 'tracksBParkMCMatchEmbedded')

        # make the JPsiToMuMuTable/count talk to the correct producer
        massSearchReplaceAnyInputTag(path, 'JPsiToMuMu', 'JPsiToMuMuMC')

        # modify the path to include mc-specific info
        path.insert(0, nanoSequenceMC)
        path.replace(process.muonBParkSequence, process.muonBParkMC)
        path.replace(process.electronsBParkSequence, process.electronBParkMC)
        path.replace(process.tracksBParkSequence, process.tracksBParkMC)
        #path.replace(process.muonBParkSequence, process.muonBParkMCWithTriggerMuon)
        
        if addTriggerMuonCollection:
          path.replace(process.muonBParkSequence, process.muonBParkMCWithTriggerMuon)
        else:
          path.replace(process.muonBParkSequence, process.muonBParkMC)
        path.replace(process.electronsBParkSequence, process.electronBParkMC)
        if addProbeTracksCollection:
          path.replace(process.tracksBParkSequence, process.tracksBParkMCWithTable)
        else:
          path.replace(process.tracksBParkSequence, process.tracksBParkMC)
