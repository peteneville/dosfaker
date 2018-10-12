import random

#from faker import Faker
from faker.providers import BaseProvider

#fake = Faker()


class CountyProvider (BaseProvider):



  def county(self):
    countyArray = ['DEVON','CORNWALL']

    return random.choice(countyArray)

class GenderProvider (BaseProvider):

  def gender(self):
    genders = ['M','F']

    return random.choice(genders)

class OdsCodeProvider (BaseProvider):


    def odscode(self):
        odscodeList = ['Ambulance','Therapist','Council']
        retval = random.choice(odscodeList)

        return retval


class ServiceTypeDescProvider(BaseProvider):


    def serviceTypeDesc(self,typeId):
        serviceTypeDict = {
        '-2':'Local Templates',
'-1':'DoS Region',
'3':'Council',
'4':'Therapist',
'5':'Ambulance Service',
'6':'Organisational Cluster',
'7':'Mental Health',
'8':'Social Care',
'11':'Voluntary agency',
'12':'Dental Services',
'13':'Pharmacist',
'14':'Optician',
'15':'NHS Trust',
'17':'Clinics',
'18':'Health Visitor',
'19':'Midwifery',
'20':'Community Based Services',
'21':'Retired Services',
'22':'Commissioning Organisation',
'24':'Care Home',
'25':'GP Out of Hours Provider (OOH)',
'27':'Intermediate Care',
'28':'Community Hospital',
'29':'Sexual Health',
'30':'Single Point of Access (SPoA)',
'31':'Emergency Care Practitioner (ECP)',
'32':'Primary Care Practitioner (PCP)',
'35':'MIU',
'38':'District/Community Nurse',
'40':'Emergency Department',
'41':'Acute Assessment unit',
'42':'Inpatient General Ward',
'45':'WIC',
'46':'UCC',
'47':'Dental Emergency',
'48':'Specialist Service',
'49':'Multi-Disciplinary Services',
'50':'Palliative Care',
'100':'GP in hours',
'105':'Speciality Emergency Department (Spec ED)',
'106':'GP-Led UCC with ED',
'107':'Critical Care (CC)',
'108':'Paediatrics Intensive Care Unit (PICU)',
'109':'Burns (B)',
'110':'Maternity & Neonate (M&N)',
'111':'Paediatrics (PDR)',
'112':'Minor Eye Condition service (MECS)',
'113':'Health Information',
'114':'Acute Hospital (Capacity)',
'115':'Provider Escalation/RAG (Capacity)',
'116':'Pharmacist - Extended Hours',
'117':'GP Choice',
'120':'Eye Casualty',
'121':'Primary Percutaneous Coronary Intervention (PPCI)',
'122':'Hyper-Acute Stroke Unit (HASU)',
'123':'GP Extended Hours ',
'124':'Domiciliary Dentist',
'125':'Domiciliary Optician',
'129':'Safeguarding',
'130':'NHS111 Provider',
'131':'Pharmacist UrgentPrescription',
'132':'Pharmacist Enhanced Service',
'133':'Integrated Urgent Care (IUC) Clinical Assessment Service (CAS)',
'134':'Distance Selling Pharmacy (DSP)'
}



        return serviceTypeDict[typeId]
