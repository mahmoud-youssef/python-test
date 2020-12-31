
ContactsList = {"1" : "Alice Brown / None / 1231112223","2" : "Bob Crown / bob@crowns.com / None","3" : "Carlos Drew / carl@drewess.com / 3453334445","4" : "Doug Emerty / None / 4564445556","5" : "Egan Fair / eg@fairness.com / 5675556667"}


LeadsList = {'1' : 'None / kevin@keith.com / None','2' : 'Lucy / lucy@liu.com / 3210001112','3' : 'Mary Middle / mary@middle.com / 3331112223','4' : 'None / None / 4442223334','5' : 'None / ole@olson.com / None'}


RegistrantsList = {
              "registrant": 
                 [{ 
                    "name": "Lucy Liu", 
                    "email": "lucy@liu.com",
                    "phone": "None",
                 },
                 { 
                    "name": "Doug", 
                    "email": "doug@emmy.com",
                    "phone": "4564445556",
                 },
                 { 
                    "name": "Uma Thurman", 
                    "email": "uma@thurs.com",
                    "phone": "None",
                 }]
            }
            
for Registrant in RegistrantsList['registrant']:
    for contacts in ContactsList:
        if Registrant['email'] != 'None':
            if ContactsList[contacts].find(Registrant['email']) == -1:
                if Registrant['phone'] != 'None':
                    if ContactsList[contacts].find(Registrant['phone']) != -1:
                        email = ContactsList[contacts].split("/")[1]
                        ContactsList[contacts] = ContactsList[contacts].replace(email," "+Registrant['email']+" ")
                        
            else:
                phone = ContactsList[contacts].split("/")[2]
                ContactsList[contacts] = ContactsList[contacts].replace(email," "+Registrant['phone']+" ")

for Leads in LeadsList:
    LeadName = LeadsList[Leads].split("/")[0]
    LeadEmail = LeadsList[Leads].split("/")[1]
    LeadPhone = LeadsList[Leads].split("/")[2]
    if LeadEmail.find('None') == -1:
        for contacts in ContactsList:
            ContactEmail = ContactsList[contacts].split("/")[1]
            if ContactEmail == LeadEmail:
                LeadsList.pop(Leads)
                if LeadName.find('None') == -1:
                    
                    ContactsList[str(int(list(ContactsList)[-1]) + 1)] = LeadsList[Leads]
                break;
            else:
                if LeadName.find('None') == -1:
                    ContactsList[str(int(list(ContactsList)[-1]) + 1)] = LeadsList[Leads]
                break;

    else:
        if LeadPhone.find('None') == -1:
            for contacts in ContactsList:
                ContactPhone = ContactsList[contacts].split("/")[2]
                if ContactPhone == LeadPhone:
                    LeadsList.pop(Leads)
                    if LeadName.find('None') == -1:
                        ContactsList[str(int(list(ContactsList)[-1]) + 1)] = LeadsList[Leads]
                    break;
                else:
                    if LeadName.find('None') == -1:
                        ContactsList[str(int(list(ContactsList)[-1]) + 1)] = LeadsList[Leads]
                    break;
                
print(ContactsList)
        
            
            











