stages = [
    "Enquiry yet to float",
    "Awaiting pre-offer from vendor",
    "Pre-order pending with EDRC",
    "PRE-ORDER COMMENTS ISSUED",
    "PRE-ORDER TECHNICALLY CLEARED",
    "PRE-ORDER TECHNICALLY REJECTED",
    "Regret offer",
    "Sent to SCM",
    "Awaiting post-offer from vendor",
    "Post-order pending with EDRC",
    "POST-ORDER COMMENTS ISSUED",
    "POST-ORDER TECHNICALLY CLEARED",
    "MFC issued"
]
a="Pre-order comments issued"
if a in stages[1:13]:
    print("Yahoo")
    
    # if row[5] is  None or row[12] is None or row[5].strip()=="" or row[12].strip()==""  :
    #     return jsonify({'success': False, 'error': 'Please fill the mandatory fields- Vendor Name & PR Issued Date in row: '+ str(session["rownum"])}),403