#!/usr/bin/env python
# coding: utf-8

# In[2]:


from owlready2 import *
from owlready2.pymedtermino2 import *
from owlready2.pymedtermino2.umls import *
medWorld = World(filename = "D:/medcatPymedSqliteFiles/pym.sqlite3")


# In[ ]:


PYM = medWorld.get_ontology("http://PYM/").load()


# In[ ]:


import pickle


# In[ ]:


##file = open("alltextEntitiesAllStr2.data",'rb')
file = open("alltextEntitiesKaggleStrDisorders.data",'rb')
alltextEntitiesAllStr = pickle.load(file)
file.close()


# In[ ]:


ICD10 = PYM["ICD10"]


# In[ ]:


SNOMEDCT_US = PYM["SNOMEDCT_US"]
concept = SNOMEDCT_US[302509004]
print(concept)


# In[ ]:


allowedRelationsSNOMED=["has_finding_site"]

for prop in SNOMEDCT_US[code].get_class_properties():
        #print(prop.name)
        if (prop.name not in rejectedPropsList) and (prop.name in allowedRelationsSNOMED):


# In[ ]:


#Only child concepts for ICD10 because applying Lin's
for i,case in enumerate(alltextEntitiesAllStr):
    ##print(case)
    snomedConcepts=case[2]
    #print("Case3 "+str(case[3])+" case4 "+str(case[4]))
    icdconcepts=case[3]
    snomedConceptsOnt=[]
    for snomedid in snomedConcepts:
        try:
            for props in SNOMEDCT_US[int(snomedid)].get_class_properties():
                if (prop.name not in rejectedPropsList) and (prop.name in allowedRelationsSNOMED):
                    conceptsnomed = SNOMEDCT_US[int(snomedid)]
        except:
            conceptsnomed=''
    
        #print(conceptsnomed)
        snomedConceptsOnt.append(conceptsnomed)
        
    icdconceptsOnt=[]
    for icdid in icdconcepts:
        #print(icdid)
        try:
            concepticd10=ICD10[str(icdid)]
            #print(concepticd10)
        except:
            concepticd10=''
        icdconceptsOnt.append(concepticd10)
        
    case[2]=[x for x in snomedConceptsOnt if x]
    case[3]=[x for x in icdconceptsOnt if x]
    


# In[ ]:


#ICD10["R22.1"].ancestors()
def addAllAncestorsICD(ICDchildConcept):
    completecodes=[]
    for eachAncestor in ICDchildConcept.ancestor_concepts():
        #if eachAncestor not in [PYM.Concept,PYM["ICD10"],PYM["SRC"],owl.Thing]:
        if eachAncestor not in completecodes:
            completecodes.append(eachAncestor)

    print(completecodes)
    return completecodes


# In[ ]:


#file = open("alltextEntitiesAllStr2.data",'rb')
file = open("alltextEntitiesKaggleStr.data",'rb')
alltextEntitiesAllStrForProbCalc = pickle.load(file)
file.close()


# In[ ]:


#Code where ICD10 codes ancestors are also added
#append if a string is added to list
#extend if a list is added to a list but we want it to be stored as elements not list/sublist
#Due to ancestors, SNOMED indices donot map to ICD indices
for i,case in enumerate(alltextEntitiesAllStrForProbCalc):
    print(i)
    snomedConcepts=case[2]
    #print(snomedConcepts)
    icdconcepts=case[3]
    snomedConceptsOnt=[]
    for snomedid in snomedConcepts:
        try:
            conceptsnomed = SNOMEDCT_US[int(snomedid)]
        except:
            conceptsnomed=''
    
        print(conceptsnomed)
        
        snomedConceptsOnt.append(conceptsnomed)
        
    icdconceptsOnt=[]
    for icdid in icdconcepts:
        #print(icdid)
        try:
            concepticd10=ICD10[str(icdid)]
            concepticd10list=addAllAncestorsICD(concepticd10)
            icdconceptsOnt.extend(concepticd10list)
            #print(concepticd10)
        except:
            concepticd10list=''
            icdconceptsOnt.append(concepticd10list)
            #concepticd10=''
        
        
    case[2]=[x for x in snomedConceptsOnt if x]
    case[3]=[x for x in icdconceptsOnt if x]
    


# mylist=[]
# a=[1,2,3]
# b="11"
# mylist.extend(a)
# mylist.append(b)
# print(mylist)

# In[ ]:


alltextEntitiesAllStr[0:10]


# In[ ]:


alltextEntitiesAllStr[6][4]


# In[ ]:


PYM.Concepts(alltextEntitiesAllStr[6][4]).lowest_common_ancestors()


# In[ ]:


print(PYM.Concepts(alltextEntitiesAllStr[6][4]).)


# In[ ]:


alltextEntitiesAllStr[6][4]


# In[ ]:


newlist


# In[ ]:


SNOMEDCT_US["301777002"].ancestor_concepts()


# In[ ]:


print(PYM.Concepts(SNOMEDCT_US["301777002"].ancestor_concepts()).lowest_common_ancestors())


# In[ ]:


SNOMEDCT_US["301777002"].ancestors()


# In[ ]:


SNOMEDCT_US["301777002"].has_part


# In[ ]:


for o in PYM.individuals():
    print(o.name)


# In[ ]:


for o in PYM.object_properties():
    print(o.name)


# In[ ]:


SNOMEDCT_US["301777002"].has_finding_site


# In[ ]:


code="51185008"#"301777002"
for prop in SNOMEDCT_US[code].get_class_properties():
    print(prop.name,getattr(SNOMEDCT_US[code],prop.name))


# In[ ]:


for prop in SNOMEDCT_US["24484000"].get_class_properties():
    print(prop.name,getattr(SNOMEDCT_US["24484000"],prop.name))


# In[ ]:


SNOMEDCT_US["301777002"]


# #ICD10["R22.1"].ancestors()
# def addAllAncestorsICD(ICDchildConcept):
#     completecodes=[]
#     for eachAncestor in ICDchildConcept.ancestors():
#         if eachAncestor not in [PYM.Concept,PYM["ICD10"],PYM["SRC"],owl.Thing]:
#             if eachAncestor not in completecodes:
#                 completecodes.append(eachAncestor)
# 
#     print(completecodes)
#     return completecodes

# In[ ]:


#ICD10["R22.1"].ancestors()
def addAllAncestorsICD(ICDchildConcept):
    completecodes=[]
    for eachAncestor in ICDchildConcept.ancestor_concepts():
        #if eachAncestor not in [PYM.Concept,PYM["ICD10"],PYM["SRC"],owl.Thing]:
        if eachAncestor not in completecodes:
            completecodes.append(eachAncestor)

    print(completecodes)
    return completecodes


# In[ ]:


addAllAncestorsICD(ICD10["D56.9"])


# In[ ]:


ICD10["D56.9"].ancestor_concepts()


# In[ ]:


countICD=0
countSNOMED=0
allICDnames=[]
allSNOMEDnames=[]
for case in alltextEntitiesAllStrForProbCalc:
    icd10conceptslist=case[4]
    snomedconceptslist=case[3]
    for icd10singleConcept in icd10conceptslist:
        if icd10singleConcept:
            if icd10singleConcept not in allICDnames:
                allICDnames.append(icd10singleConcept)
            countICD=countICD+1
    for snomedsingleConcept in snomedconceptslist:
        if snomedsingleConcept:
            countSNOMED=countSNOMED+1
            if snomedsingleConcept not in allSNOMEDnames:
                allSNOMEDnames.append(snomedsingleConcept)
print(countICD)
print(countSNOMED)
#allTopics=ontology.Topic.instances()


# In[ ]:


allICDnames


# In[ ]:


print(len(allICDnames))
print(len(allSNOMEDnames))


# In[ ]:


allSNOMEDnames


# In[ ]:


def get_all_ICD_probability():
    icdProbability=[]
    totalICDcodes=countICD
    for searchICDcode in allICDnames:
        countICDcode=0
        #totalTopics=0
        for case in alltextEntitiesAllStrForProbCalc:
            icd10conceptslist=case[4]
            snomedconceptslist=case[3]
            for icd10singleConcept in icd10conceptslist:
                if icd10singleConcept:
                    if icd10singleConcept==searchICDcode:
                        countICDcode=countICDcode+1
        res=countICDcode/totalICDcodes
        ##icdProbability.append([searchICDcode.name,res])
        icdProbability.append([searchICDcode,res])
    return icdProbability


# In[ ]:


def get_all_SNOMED_probability():
    snomedProbability=[]
    totalSNOMEDcodes=countSNOMED
    for searchSNOMEDcode in allSNOMEDnames:
        countSNOMEDcode=0
        #totalTopics=0
        for case in alltextEntitiesAllStrForProbCalc:
            #icd10conceptslist=case[4]
            snomedconceptslist=case[3]
            #print(snomedconceptslist)
            for SNOMEDsingleConcept in snomedconceptslist:
                if SNOMEDsingleConcept:
                    if SNOMEDsingleConcept==searchSNOMEDcode:
                        #print(SNOMEDsingleConcept)
                        countSNOMEDcode=countSNOMEDcode+1
        res=countSNOMEDcode/totalSNOMEDcodes
        ##icdProbability.append([searchICDcode.name,res])
        snomedProbability.append([searchSNOMEDcode,res])
    return snomedProbability


# In[ ]:


ICD10Probability=get_all_ICD_probability()


# In[ ]:


SNOMEDProbability=get_all_SNOMED_probability()


# In[ ]:


SNOMEDProbability


# In[ ]:


#allTopicsProb
def ConvertToDict(lst):
    res_dct = {x[0]: x[1] for x in lst}
    return res_dct


# In[ ]:


snomedProbDict=ConvertToDict(SNOMEDProbability)
icd10ProbDict=ConvertToDict(ICD10Probability)
#ICD10["R19.8"].name


# In[ ]:


ICD10["R19.8"].name


# In[ ]:


def get_ICD_probability(SearchICD):
    #print("SEarch "+SearchTopic)
    if SearchICD != "Thing":
        print(icd10ProbDict[SearchICD])
        if icd10ProbDict[SearchICD]:
            return icd10ProbDict[SearchICD]
        else:
            return 0
    else:
        return 0


# In[ ]:


print(icd10ProbDict[ICD10["R19.8"]])
get_ICD_probability(ICD10["R19.8"])


# In[ ]:


print(icd10ProbDict[ICD10["R19.8"]])
get_ICD_probability(ICD10["R19.8"])


# with open('icdProbDict.data', 'wb') as filehandle: # store the data as binary data stream 
#     pickle.dump(icdProbDict, filehandle) 
# filehandle.close()

# with open('icdProbDict.data', 'wb') as filehandle: # store the data as binary data stream 
#     pickle.load(icdProbDictNames, filehandle) 
# filehandle.close()

# In[ ]:


import math


# In[ ]:


def get_IC_ICD10(SearchTopic):
    if SearchTopic != "Thing":
        prob=icd10ProbDict[SearchTopic]
    else:
        prob=0
    if prob>0:
        IC=-math.log(prob)
    else:
        IC=0
    #print(IC)
    return IC


# In[ ]:


def score_Resnik(concept1,concept2):
    lca=PYM.Concepts([concept1,concept2]).lowest_common_ancestors()
    #print(list(lca))
    if lca:
        res=get_IC_ICD10(list(lca)[0])
    else:
        res=0
    #lcaName=getattr(ontology,lca).TopicCompleteName
    #normalisedScore=res/11
    #print("score_Resnik"+str(res))
    return res,lca


# In[ ]:


score_Resnik(ICD10["R19.8"],ICD10["R19.5"])


# In[ ]:


def score_lin(concept1,concept2):
    simRes,lca=score_Resnik(concept1,concept2)
    s_IC=get_IC_ICD10(concept1)
    t_IC=get_IC_ICD10(concept2)
    #print(s_IC,t_IC)
    scoreLin=2*simRes/(s_IC+t_IC)
    ##print("score_lin "+str(scoreLin))
    return scoreLin,lca


# In[ ]:


score_lin(ICD10["R19.8"],ICD10["R19.4"])


# In[ ]:


alltextEntitiesAllStr[3][4]


# In[ ]:


alltextEntitiesAllStr[6][4]


# In[ ]:


#This uses maximum distance as measure
def computeTopicsLinScores(queryIndex,testIndex,scoreMethod=None):
    
    queryTopics=alltextEntitiesAllStr[queryIndex][4]
    testTopics=alltextEntitiesAllStr[testIndex][4]
    #print(queryTopics)
    #print(testTopics)
    #print("---")
    if queryTopics != [''] and testTopics != [''] and queryTopics != [] and testTopics != []:
        if len(queryTopics)>len(testTopics):
                largerSet=queryTopics
                smallerSet=testTopics
                #print(largerSet,smallerSet)
        else:
            largerSet=testTopics
            smallerSet=queryTopics            
            #print(largerSet,smallerSet)
        ScoresList=[]
        ScoresListAvg=[]
        LCAlist=[]
        for qtopic in largerSet:
            scoresTemp=[]
            lcaTemp=[]
            for ttopics in smallerSet:
                #if scoreMethod=="WuPalmer":
                    score,lca=score_lin(qtopic,ttopics)
                    
                    #print("score_lin "+str(score))
                    scoresTemp.append(score)
                    if lca not in lcaTemp and lca:
                        lcaTemp.append(lca)
            for x in lcaTemp:
                #print(x)
                if (x not in LCAlist and x != []):
                    LCAlist.append(x)
           # print(scoresTemp)
            print(scoresTemp)
            #if scoresTemp != []:
            ScoresList.append(max(scoresTemp))
            ScoresListAvg.append(sum(scoresTemp)/len(scoresTemp))

        FinalScoreLin=sum(ScoresList)/len(ScoresList)
        FinalScoreLinAvg=sum(ScoresListAvg)/len(ScoresListAvg)
        #print("FinalScoreLin "+str(queryIndex)+" ** "+str(testIndex)+" is "+str(FinalScoreLin))
       
        if LCAlist != []:
            #specificTopics=getSpecificTopic(LCAlist)
            #print(specificTopics)
            lcaSpecificTopicNames=[x for x in LCAlist]
            #print(" lcaSpecificTopicNames "+str(lcaSpecificTopicNames))
            return FinalScoreLin,lcaSpecificTopicNames
        else:
            return FinalScoreLin,LCAlist
    else:
        return 0,[]


# In[ ]:


alltextEntitiesAllStr[4][3]


# In[ ]:


alltextEntitiesAllStr[6][3]


# In[ ]:


computeTopicsLinScores(3,6)


# In[ ]:


computeTopicsLinScores(3,6)


# In[ ]:


ICD10["R00-R99.9"].label


# In[ ]:


ICD10["R99"].parents


# In[ ]:


def union(lst1, lst2): 
    return list(set(lst1).union(set(lst2)))


# In[ ]:


ontologyScoringSNOMEDBasicModifiedFormula(4,6)


# In[ ]:


ontologyScoringSNOMEDBasicModifiedFormula(7,8)


# In[ ]:


alltextEntitiesAllStr[4][3]


# In[ ]:


alltextEntitiesAllStr[6][3]


# In[ ]:


list1=alltextEntitiesAllStr[4][3]
list1.extend(alltextEntitiesAllStr[6][3])
list1


# In[ ]:


print(PYM.Concepts(list1).lowest_common_ancestors())


# In[ ]:


print(PYM.Concepts([SNOMEDCT_US["106051002"],SNOMEDCT_US["301272007"]]).lowest_common_ancestors())


# In[ ]:


ontSimilarity(alltextEntitiesAllStr[7],alltextEntitiesAllStr[8])


# In[ ]:


SNOMEDCT_US["51185008"].ancestor_concepts()


# In[ ]:


print(SNOMEDCT_US["51185008"].has_finding_method)
print(SNOMEDCT_US["416550000"].term_type)
print(SNOMEDCT_US["417437006"].term_type)
print(SNOMEDCT_US["67734004"].term_type)


# In[ ]:


print(SNOMEDCT_US["51185008"].get_class_properties())


# In[ ]:


print(SNOMEDCT_US["51185008"].definition_status_id)
print(SNOMEDCT_US["249543005"].definition_status_id)


# In[ ]:


ontSimilarity(alltextEntitiesAllStr[4],alltextEntitiesAllStr[6])


# In[ ]:


alltextEntitiesAllStr[5:10]


# In[ ]:


ontSimilarity(alltextEntitiesAllStr[4],alltextEntitiesAllStr[9])


# In[ ]:


print(PYM.Concepts([SNOMEDCT_US["106051002"],SNOMEDCT_US["301272007"]]).lowest_common_ancestors())


# def ontSimilarity(case1_alignment,case2_alignment):
#     sim=0.00
#     
#     if len(case1_alignment)>0 and len(case2_alignment)>0:
#         intersectionConceptsSNOMED=intersection(case1_alignment[3],case2_alignment[3])
#         
#          if intersectionConceptsSNOMED:
# 
#             for eachIntersect in eachIntersectList:
#                     #print("eachIntersect "+str(eachIntersect))
#                     interSection=[]
#                     interSection.append("Both cases mention "+str(eachIntersect))
#                     interSection.append(str(eachIntersect)+" is a type of "+str(eachIntersect.parents))
#                     
#             for singleInterSection in interSection:
#                     if singleInterSection not in intersectionAlignmentExplanation:
#                         intersectionAlignmentExplanation.append(singleInterSection)
#                     else:
#                         pass

# In[ ]:


#FINAL
def ontSimilarity(case1_alignment,case2_alignment):
    sim=0.00
    differenceAlignmentExplanation=[]
    intersectionAlignmentExplanation=[]
    if len(case1_alignment)>0 and len(case2_alignment)>0:
         
        intersectionConceptsSNOMED=intersection(case1_alignment[3],case2_alignment[3])
        intersectionConceptsICD=intersection(case1_alignment[4],case2_alignment[4])
        
        interSection=[]
        if intersectionConceptsICD:

            for eachIntersect in intersectionConceptsICD:
                #print("eachIntersect "+str(eachIntersect))
                
                interSection.append("Both cases mention "+str(eachIntersect))
                for p in eachIntersect.parents:
                    interSection.append(str(eachIntersect)+" is a type of "+str(p))

        #ICD!)
        
        if intersectionConceptsSNOMED:

            for eachIntersect in intersectionConceptsSNOMED:
                    #print("eachIntersect "+str(eachIntersect))
                    interSection.append("Both cases mention "+str(eachIntersect))
                    for p in eachIntersect.parents:
                        interSection.append(str(eachIntersect)+" is a type of "+str(p))
                       
        #ICD!)
        
        for singleInterSection in interSection:
            if singleInterSection not in intersectionAlignmentExplanation:
                intersectionAlignmentExplanation.append(singleInterSection)
            else:
                pass
                #print("already in list "+str(singleInterSection))
                
        return intersectionAlignmentExplanation,differenceAlignmentExplanation



   


# In[ ]:


def ontSimilarity(case1_alignment,case2_alignment,detailedOldCaseAlignment):
    sim=0.00
    #print("case1_alignment in ontSimi is "+str(case1_alignment))
    #print("case2_alignment in ontSimi is "+str(case2_alignment))
    #print("detailedOldCaseAlignment in ontSimi is "+str(detailedOldCaseAlignment))
    #print("************************************")
    
    if len(case1_alignment)>0 and len(case2_alignment)>0:
   
            #d1nd2= computeD(list(set(getConceptAlignment1D(case1_alignment))&set(detailedOldCaseAlignment)))# //common features of nc and sci
     

        D1= computeD([case1_alignment])
        #print("done with d1 == "+str(D1))
        D2=computeD([case2_alignment])
        D2detailed=computeD([detailedOldCaseAlignment])

        ##D2=computeD([detailedOldCaseAlignment])
        #print("done with d2 === "+str(D2))
        if len(detailedOldCaseAlignment)>1:
            #print("NESTED LIST")
            intersection=dAOdB([case1_alignment], [detailedOldCaseAlignment], 'intersection')

        else:
             intersection=dAOdB([case1_alignment], [detailedOldCaseAlignment], 'intersection')
       
        d1nd2= computeD(intersection)



       #_________________________________-

        #intersectionAlignment=dAOdBexplain([case1_alignment], [detailedOldCaseAlignment], 'intersection')
        #intersectionAlignmentBasic=dAOdB([case1_alignment], [detailedOldCaseAlignment], 'intersection')
        differenceAlignmentExplanation=[]
        intersectionAlignmentExplanation=[]
        
        
        #intersectionAlignment=dAOdB([case1_alignment],[detailedOldCaseAlignment], 'intersection')
        #print("intersectionAlignment this is "+str(intersection))
        ##print(str(case1_alignment)+" *** "+str(detailedOldCaseAlignment))
        if intersection:

            for eachIntersectList in intersection:
                for eachIntersect in eachIntersectList:
                    #print("eachIntersect "+str(eachIntersect))
                    interSection=[]
                    #print(eachIntersect)
                    if eachIntersect[8].find('quran')>-1:
                        
                        if eachIntersect[7] != "DiscussTopic":
                            interSection.append("Both verses mention "+str(getMainTopic(eachIntersect[0])))
                            interSection.append(str(eachIntersect[0])+" is a type of "+getattr(ontology,eachIntersect[0]).is_a[0].name)
                        else:
                            interSection.append("Both verses are about "+str(getMainTopic(eachIntersect[0])))
                    else:

                        interSection.append(str(getattr(ontology,eachIntersect[8]).name)+" "+str(getattr(ontology,eachIntersect[7]).label[1])+" "+str(getattr(ontology,eachIntersect[0]).label[1]))
                        interSection.append(str(getattr(ontology,eachIntersect[0]).label[1])+" is a type of "+str(getattr(ontology,eachIntersect[0]).is_a[0].name))

                    for singleInterSection in interSection:
                        if singleInterSection not in intersectionAlignmentExplanation:
                            intersectionAlignmentExplanation.append(singleInterSection)
                        else:
                            pass
                            #print("already in list "+str(singleInterSection))


        #print("done with d1nd2 -------------------------------"+str(d1nd2))
    #MODIFIED 
        miufunction=0.8 #keep constant althouht it ought to be in [0.0 , 1.0]

        difference12=dAOdB([case1_alignment], [case2_alignment], 'difference')
        ##difference12=set(getConceptAlignment1D(case1_alignment)).difference(set(detailedOldCaseAlignment))
        #print('difference12 '+str(difference12))
        d1ORd2=computeD(difference12) #distinct features of nc to sci

        ##difference21=set(getConceptAlignment1D(case2_alignment)).difference(set(case1_alignment))
        ##print('difference21 '+str(difference21))

        differenceAlignment=dAOdB([case2_alignment], [case1_alignment], 'difference')
        #print("differenceAlignment this is "+str(differenceAlignment))
        if len(differenceAlignment)>0:
            #for eachDiff in differenceAlignment[0]:
             for eachDiffList in differenceAlignment:
                for eachDiff in eachDiffList:
                    if eachDiff[8].find('quran')>-1:
                        if eachDiff[7] != "DiscussTopic":
                            diffSection="This ayat mentions "+str(getattr(ontology,eachDiff[0]).label[1])
                        else:
                            diffSection="This ayat is about "+str(getMainTopic(eachDiff[0]))
                    else:
                        diffSection=str(getattr(ontology,eachDiff[8]).name)+" "+getattr(ontology,eachDiff[7]).name+" "+str(getattr(ontology,eachDiff[0]).label[1])
                    differenceAlignmentExplanation.append(diffSection)
                    if eachDiff[7] != "DiscussTopic":
                        diffSection=str(getattr(ontology,eachDiff[0]).label[1])+" is a type of "+str(getattr(ontology,eachDiff[0]).is_a[0].label[1])
                        differenceAlignmentExplanation.append(diffSection)
                
                    
                    
        else:
            differenceAlignmentExplanation.append("")

        #print("done with d1nd2 -------------------------------"+str(d1nd2))
        #MODIFIED 

        ##difference21=set(getConceptAlignment1D(case2_alignment)).difference(set(case1_alignment))
        ##print('difference21 '+str(difference21))


        secondIntersection=dAOdB([case1_alignment], [detailedOldCaseAlignment], 'intersection')
            #d1nd2= computeD(list(set(getConceptAlignment1D(case1_alignment))&set(detailedOldCaseAlignment)))# //common features of nc and sci
        d1nd2= computeD(intersection)


        intersectionFirst=dAOdB([case1_alignment], [case2_alignment], 'intersection')
            #d1nd2= computeD(list(set(getConceptAlignment1D(case1_alignment))&set(detailedOldCaseAlignment)))# //common features of nc and sci
        d1InterSectFirstd2= computeD(intersectionFirst)



    else:
        #print("no case alignments found")
        return None
    #print("totalScore "+str(TotalScore))
    #print("intersectionAlignmentExplanation is "+str(intersectionAlignmentExplanation))
    #print("differenceAlignmentExplanation is "+str(differenceAlignmentExplanation))
    return intersectionAlignmentExplanation,differenceAlignmentExplanation


# In[ ]:


def retrieveAllSimilarCases(Case,x):
    resultsArray=[]
    resultsArrayText=[]
    intersectionAlignment=[]
    newCaseAlignment=None
    if x=='new':
        caseID1=str(Case)
        ###print("ccccccccccccccc "+str(Case))
        newCaseAlignment=getNewAlignment(Case)
        caseText=Case
        
    else:
        caseID1=Case
        
        if Case<=len(alltextEntitiesAllStr):
            #&&&&&&&&&&&&&&&&&&&7MODIFIED ========== MODIFIED -----==============
            #newCaseAlignment,explain,alignm=getAlignmentOldCase(QuranCases[int(Case)])
            newCaseAlignment=alltextEntitiesAllStr[int(Case)]
            ##newCaseAlignment=oldCaseAlignments[int(caseID1)]
            try:
                caseText="Ayat Translation of "+str(alltextEntitiesAllStr[int(Case)][1])
            except:
                print("Text not found ")
                return None,None
                
        else:
            print("Case not found "+str(Case))
            return None,None
    if not newCaseAlignment or newCaseAlignment==[None]:
        print("not found new case alignment")
        return None,None
   
    for i,alignments in enumerate(alltextEntitiesAllStr):
        #print(i)
    #for i in range(1215,1217):
        
        #int(caseID1)
        oldCaseID=i
        oldCaseAlignment=alltextEntitiesAllStr[i]
        detailedOldCaseAlignment=detailedSNOMEDCTconceptslist[i]

        if oldCaseAlignment:
             similarityScoresMentions=0
            ScoreRensik=0
            ScoreWuPalmer=0
            ScoreLin=0
            LCAlist=[]
            UnionTopics=[]
            UnionMentions=[]

            similarityScores1,intersectionAlignment,differenceAlignment=ontSimilarity(newCaseAlignment,oldCaseAlignment,detailedOldCaseAlignment)
            if oldCaseAlignmentsBasic[oldCaseID] == None:
                similarityScoresMentions=-1
                if oldCaseAlignmentsBasic[caseID1] != None:
                    UnionMentions=getConceptAlignment1D(oldCaseAlignmentsBasic[caseID1])


            else:
                if oldCaseAlignmentsBasic[caseID1] != None:
                #using modified FOR TESTING 28-9
                    ####similarityScoresMentions=ontologyScoringMentionsBasic(oldCaseID,caseID1)
                    ####MODIFICATION FIXED parameter order for mentions modified formula
                    similarityScoresMentions=ontologyScoringMentionsBasicModifiedFormula(caseID1,oldCaseID)
                    UnionMentions=union(getConceptAlignment1D(oldCaseAlignmentsBasic[oldCaseID]),getConceptAlignment1D(oldCaseAlignmentsBasic[caseID1]))
                else:
                    UnionMentions=getConceptAlignment1D(oldCaseAlignmentsBasic[oldCaseID])

            print(oldCaseID,caseID1)
            ###ScoreRensik,ScoreWuPalmer,ScoreLin=computeTopicsScoresAverage(oldCaseID,caseID1)
            ###ScoreRensik,ScoreWuPalmer,ScoreLin,LCAlist=computeTopicsScores(oldCaseID,caseID1)
            ScoreLin,LCAlist=computeTopicsLinScores(oldCaseID,caseID1)
            testTopics=getSpecificTopic(QuranCases[oldCaseID].DiscussTopic)
            queryTopics=getSpecificTopic(QuranCases[caseID1].DiscussTopic)
            #print(queryTopics)
            #print(testTopics)
            #print("---")
            if queryTopics != [''] and queryTopics != None: 
                if testTopics != [''] and testTopics != None:
                    UnionTopics=union(queryTopics,testTopics)
                else:
                    UnionTopics=queryTopics
            else:
                if testTopics != [''] and testTopics != None:
                    UnionTopics=testTopics


            if differenceAlignment==[]:

                differenceAlignment=""

            if intersectionAlignment==[]:
                intersectionAlignment="This ayat has no intersection with query ayat"

                
            if similarityScores1:
                
                result=[similarityScoresMentions,ScoreLin,LCAlist,UnionTopics,UnionMentions]
                
                if getattr(QuranCases[i],'DiscussTopic'):
                    topicList=getattr(QuranCases[i],'DiscussTopic')
                else:
                    topicList=[]

                indexQuranText=ayatNumbers.index(str(QuranCases[oldCaseID].name).replace("quran","").replace("-",":"))

                resultsArray.append([caseID1,oldCaseID,quranVerses[indexQuranText],result,str(topicList),intersectionAlignment,differenceAlignment])
                #print("caseText "+str(caseText))
                #print(oldCaseID-1)
                #try:
                #indexQuranTextQueryVerse=ayatNumbers.index(str(QuranCases[caseID1].name).replace("quran","").replace("-",":"))
                #query,ayat number, verse,score,topic,explan,further
                newayatNumber=str(QuranCases[oldCaseID].name).replace("quran","").replace("-",":")
                resultsArrayText.append([QuranCases[caseID1].label[1],newayatNumber,quranVerses[indexQuranText],result,str(topicList),intersectionAlignment,differenceAlignment])
               
            else:
                #print("this if 1 ---------")
                resultsArray.append([None,None,None,None,None,None,None])
                resultsArrayText.append([None,None,None,None,None,None,None])
        else:
            #print("this if 2 None. alignment not found for case "+str(i))
            resultsArray.append([None,None,None,None,None,None,None])
            resultsArrayText.append([None,None,None,None,None,None,None])

    return resultsArray,resultsArrayText
            


# In[ ]:


def get_IC_SNOMED(SearchTopic):
    if SearchTopic != "Thing" and snomedProbDict[SearchTopic]:
        prob=snomedProbDict[SearchTopic]
    else:
        prob=0
    if prob>0:
        IC=-math.log(prob)
    else:
        IC=0
    #print(IC)
    return IC


# In[ ]:


PYM(SNOMEDCT_US["77765009"]).objectproperties()


# In[ ]:


def getDetailed2hopsConcepts(code):
    #"301777002"
    #print(SNOMEDCT_US[code].name)
    detailedConcepts2hops=[]
    for prop in SNOMEDCT_US[code].get_class_properties():
        #print(prop.name)
        if prop.name not in rejectedPropsList:
            #print(prop,getattr(SNOMEDCT_US[code],prop.name))
            if SNOMEDCT_US[code] not in detailedConcepts2hops:
                detailedConcepts2hops.extend(getattr(SNOMEDCT_US[code],prop.name))
                #print(prop.name,getattr(SNOMEDCT_US[code],prop.name))
    return detailedConcepts2hops


# In[ ]:


rejectedPropsList=["definition_status_id",
"synonyms",
"label",
"ctv3id",
"icd-o-3_code",
"unifieds",
"term_type",
"active",
"effective_time",
"type_id",
"terminology",
"case_significance_id",
"definition_status_id",
"subset_member",
"rdf-schema.label"]


# In[ ]:


detailedSNOMEDCTconceptslist=[]
for i,case in enumerate(alltextEntitiesAllStrForProbCalc):
    print(i)
    #print(case)
    casedetailedSNOMEDconcepts=[]
    snomedCode=case[3]
    
    if snomedCode != []:
        if case[3] not in casedetailedSNOMEDconcepts:
            #print("----------------------------------")
            casedetailedSNOMEDconcepts.extend(case[3])
        detailedconceptlistcase=getDetailed2hopsConcepts(code)
        for hopsconcept in detailedconceptlistcase:
            if hopsconcept not in detailedSNOMEDCTconceptslist:
                casedetailedSNOMEDconcepts.append(hopsconcept)
        #print(detailedconceptlistcase)
    #print(casedetailedSNOMEDconcepts)
    detailedSNOMEDCTconceptslist.append(casedetailedSNOMEDconcepts)
    #list(set(detailedSNOMEDCTconceptslist) & set(casedetailedSNOMEDconcepts))


# In[ ]:


print(detailedSNOMEDCTconceptslist[0][0])
print(detailedSNOMEDCTconceptslist[1][0])


# In[ ]:


alltextEntitiesAllStrForProbCalc[1][3]


# In[ ]:


detailedSNOMEDCTconceptslist


# In[ ]:


len(getDetailed2hopsConcepts(code="51185008"))


# In[ ]:


#Intersection between Query_Level1 and Test case Level1+Level2
#Union of first levels of both query and result
def ontologyScoringSNOMEDBasicModifiedFormula(ind1,ind2):
    I=intersection(alltextEntitiesAllStr[ind1][3],detailedSNOMEDCTconceptslist[ind2])
    U=union(alltextEntitiesAllStr[ind1][3],alltextEntitiesAllStr[ind2][3])
    #print("I is "+str(I))
    #print("U is "+str(U))
    res=len(I)/len(U)
    #print("ontMentionsScoreModified "+str(res))
    return res


# In[ ]:


def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 


# In[ ]:


concepts = PYM.Concepts([ ICD10["E10"], ICD10["E11"], ICD10["E12"] ])


# In[ ]:


concepts2 = PYM.Concepts([ ICD10["E10"], ICD10["E13"], ICD10["E14"] ])


# In[ ]:


intersection(concepts,concepts2)


# In[ ]:


concepts = PYM.Concepts([ ICD10["G30.0"], ICD10["G31.0"]])


# In[ ]:


concepts.lowest_common_ancestors()


# In[ ]:


concepts = PYM.Concepts([ ICD10["G30.0"], ICD10["G31.0"],ICD10["G71"]])


# In[ ]:


concepts.lowest_common_ancestors()


# In[ ]:


concept.get_class_properties()


# In[ ]:


print(PYM.Concepts([concept.ancestor_concepts()[0],concept.ancestor_concepts()[1],concept.ancestor_concepts()[2],concept.children[0]]))


# In[ ]:


print(PYM.Concepts([concept.ancestor_concepts()[0],concept.ancestor_concepts()[2]]))


# In[ ]:


print(PYM.Concepts([concept.ancestor_concepts()[0],concept.ancestor_concepts()[2]]).lowest_common_ancestors())


# In[ ]:


PYM.Concepts([SNOMEDCT_US["189180007"],SNOMEDCT_US["428089008"]])


# In[ ]:


print(PYM.Concepts([SNOMEDCT_US["189180007"],SNOMEDCT_US["428089008"]]).lowest_common_ancestors())


# In[ ]:


print(PYM.Concepts([SNOMEDCT_US["189180007"],SNOMEDCT_US["428089008"]]).lowest_common_ancestors())


# In[ ]:


SNOMEDCT_US[189180007] >> ICD10


# In[ ]:


SNOMEDCT_US[428089008] >> ICD10


# In[ ]:


print(PYM.Concepts([ICD10["D16.4"], ICD10["D18.0"]]).lowest_common_ancestors())


# In[ ]:


ICD10["D10-D36.9"] >> SNOMEDCT_US


# In[ ]:


print(PYM.Concepts([SNOMEDCT_US["189180007"],SNOMEDCT_US["428089008"]]).keep_most_specific())


# In[ ]:


PYM.Concepts([concept.ancestor_concepts()[0],concept.children[0]])


# In[ ]:


concept.ancestor_concepts()[0]


# In[ ]:


concept.ancestor_concepts()


# In[ ]:


concept.children


# In[ ]:


#print(concept.ancestor_concepts())
print(PYM.Concepts(concept.ancestor_concepts()).lowest_common_ancestors())


# In[ ]:


concept.subset_member


# In[ ]:


for prop in concept.get_class_properties():
    try:
        print(str(prop)+" "+str(getattr(concept,prop)))
    except:
        getattr(concept,str(prop))
        print(prop)


# In[ ]:


for c in concept.ancestors()


# In[ ]:


#SNOMEDCT_US = PYM["SNOMEDCT_US"]

