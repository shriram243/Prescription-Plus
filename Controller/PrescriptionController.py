import imp
from typing import List, Union
from fastapi import File,UploadFile
# from datetime import datetime
import datetime
from beanie import PydanticObjectId
from Models.Medicine import Medicine
from datetime import date
import json
from Models.Prescription import Prescription
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

prescription_collection = Prescription
medicine_collection = Medicine


async def addRx(prescription: Prescription) -> Prescription:
    try:
        prescription.created = datetime.datetime.now()
        prescription.updated=datetime.datetime.now()
        ts = datetime.datetime.now().timestamp()
        ts = round(ts)
        prescription.Id ="Rx"+str(ts)
        doc = await prescription.create()
        docID = prescription.doctor_details.Id
        # med = await medicine_collection.find_one({docID})
        # if(med):
        return doc
    except:
        return False

async def findRxbyId(Id)->Prescription:
    try:
        rx = await prescription_collection.find_one({'Id':Id})
    except:
        return "Error Occur"
    return rx

async def findRxby_Id(_id)->Prescription:
    try:
        rx = await prescription_collection.get(_id)
    except:
        return "Error Occur"
    return rx

async def findRxbyDocId(docId)->Prescription:
    try:
        rx = await prescription_collection.find_one({'doctor_details.Id':docId})
    except:
        return "Error Occur"
    return rx

async def findAllofPatientRx(patiendId)->Prescription:
    try:
        rx = await prescription_collection.find_one({'patient_details.Id':patiendId})
    except:
        return "Error Occur"
    return rx

async def findAllofPatientRxbyUniqueHealthId(id)->Prescription:
    try:
        rx = await prescription_collection.find_one({'patient_details.unique_health_id':id})
    except:
        return "Error Occur"
    return rx

async def UpdateRx(id,data:dict)->Union[bool, Prescription]:
    try:
        data['updated'] = datetime.datetime.now()
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        rx = await prescription_collection.get(id)
        print(rx)
        if rx:
            await rx.update(update_query)
            return rx
        else:
            return False
    except:
        return False



async def generateRxPdf(_id:PydanticObjectId)->Prescription:
    data= await prescription_collection.get(_id)
    doctor_name = "Dr. "+data.doctor_details.firstname+' '+data.doctor_details.lastname
    doctor_id = data.doctor_details.council.id
    state_council = data.doctor_details.council.state
    doctor_num = data.doctor_details.mobile
    doctor_sign = data.doctor_details.signature
    doctor_address_locality = data.doctor_details.address.locality
    doctor_address_city = data.doctor_details.address.city
    doctor_address_pincode = data.doctor_details.address.pincode
    doctor_address_state = data.doctor_details.address.state
    doctor_degree = data.doctor_details.degree


    patient_name = data.patient_details.firstname+' '+data.patient_details.lastname
    patient_id = data.patient_details.unique_health_id
    patient_num = data.patient_details.mobile
    patient_address_locality = data.patient_details.address.locality
    patient_address_city = data.patient_details.address.city
    patient_address_pincode = data.patient_details.address.pincode
    patient_address_state = data.patient_details.address.state
    patient_age = data.patient_details.age
    patient_sex = data.patient_details.sex


    complaints = data.complaints
    medicine = data.medicine
    advice = data.advice
    tests = data.labtest

    follow_number = data.follow_up_date.next
    follow_type = data.follow_up_date.type
    follow_date = data.follow_up_date.date

    doc_name = "./Rx/"+str(_id)+".pdf"
    doc = SimpleDocTemplate(
        doc_name,
        pagesize=letter,
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('rightsidebig',
                              fontName="Helvetica-Bold",
                              fontSize=12,
                              parent=styles['Normal'],
                              alignment=TA_RIGHT,
                              spaceAfter=0.05)
               )
    styles.add(ParagraphStyle('rightside',
                    fontName="Helvetica",
                    fontSize=10,
                    parent=styles['Normal'],
                    alignment=TA_RIGHT,
                    spaceAfter=0.05)
    )
    styles.add(ParagraphStyle('rightsideb',
                    fontName="Helvetica-Bold",
                    fontSize=10,
                    parent=styles['Normal'],
                    alignment=TA_RIGHT,
                    spaceAfter=0.05)
    )
    styles.add(ParagraphStyle('leftside',
                    fontName="Helvetica",
                    fontSize=10,
                    parent=styles['Normal'],
                    alignment=TA_LEFT,
                    spaceAfter=0.05)
    )
    styles.add(ParagraphStyle('leftsideb',
                    fontName="Helvetica-Bold",
                    fontSize=10,
                    parent=styles['Normal'],
                    alignment=TA_LEFT,
                    spaceAfter=0.05)
    )




    flowables = []
    spacer = Spacer(1, 0.5*inch)


    para = Paragraph(doctor_name, styles["rightsidebig"])
    flowables.append(para)
    para = Paragraph("Medical State Council: {}".format(state_council), styles["rightside"])
    flowables.append(para)
    para = Paragraph("MCI ID: {}".format(doctor_id), styles["rightside"])
    flowables.append(para)
    para = Paragraph("{}".format(doctor_degree), styles["rightsideb"])
    flowables.append(para)
    para = Paragraph("Address: {}".format(doctor_address_locality), styles["rightside"])
    flowables.append(para)
    para = Paragraph("{}, {} {}".format(doctor_address_city, doctor_address_state, doctor_address_pincode), styles["rightside"])
    flowables.append(para)
    para = Paragraph("Contact: {}".format(doctor_num), styles["rightside"])
    flowables.append(para)
    flowables.append(spacer)


    para = Paragraph("Date: {}".format(date.today()), styles["leftsideb"])
    flowables.append(para)
    para = Paragraph("Patient Name: {}".format(patient_name), styles["leftside"])
    flowables.append(para)
    para = Paragraph("Age: {}, Gender: {}".format(patient_age, patient_sex), styles["leftside"])
    flowables.append(para)
    para = Paragraph("Address: {}".format(patient_address_locality), styles["leftside"])
    flowables.append(para)
    para = Paragraph("{}, {} {}".format(patient_address_city, patient_address_state, patient_address_pincode), styles["leftside"])
    flowables.append(para)
    para = Paragraph("Contact: {}".format(patient_num), styles["leftside"])
    flowables.append(para)
    flowables.append(spacer)

    para = Paragraph("Patient has complaints of: ", styles["leftsideb"])
    flowables.append(para)
    i=1
    for complaint in complaints:
        para = Paragraph(str(i) + ". "+complaint.term+" from the past {} days and the severity is {}".format(complaint.duration, complaint.severity), styles["leftside"])
        flowables.append(para)
        i = i+1
        para = Paragraph("Additional information: {}".format(complaint.additional_info), styles["leftside"])
        flowables.append(para)

    flowables.append(spacer)
    print("========med=========", medicine)
    dat1 = []
    cols = ["Medicine", "Dosage", "Duration", "When", "Quantity", "Additional Information"]
    dat1.append(cols)
    for med in medicine:
        temp = []
        temp.append(med.term)
        temp.append(med.dosage)
        temp.append(str(med.duration.frequency)+med.duration.type)
        temp.append(med.when)
        temp.append(med.quantity)
        temp.append(med.additional_info)
        dat1.append(temp)
    s = len(dat1)
    print("==========s=========", s)
    t=Table(dat1,[3*inch, 0.7*inch, 0.7*inch,0.7*inch,0.7*inch,1.5*inch ], s*[0.2*inch])
    t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
    ('FONTSIZE', (0,0),(-1,-1), 8),
    ('VALIGN',(0,0),(0,-1),'MIDDLE'),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ]))
    flowables.append(t)
    flowables.append(spacer)

    para = Paragraph("Advice: {}".format(advice), styles["leftsideb"])
    flowables.append(para)
    flowables.append(spacer)

    para = Paragraph("Tests: ", styles["leftsideb"])
    flowables.append(para)
    x = ""
    for test in tests:
        x = x+test.term
        x = x+', '
    para = Paragraph(x, styles["leftside"])
    flowables.append(para)
    flowables.append(spacer)
    para = Paragraph("Follow up: {} {}".format(follow_number, follow_type), styles["leftsideb"])
    flowables.append(para)
    doc.build(flowables)
    return "pdf Generated Successfully"