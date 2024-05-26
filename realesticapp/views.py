from tkinter import E
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import webbrowser
import mysql.connector as MySQLdb

# database connection
db = MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='dbrealistic')
c = db.cursor()

# Create your views here.

######################################################################
#                           LOAD INDEX PAGE
######################################################################


def basepage(request):
    return render(request, "base.html")


def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "index.html")

#########################################################################


def common(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "commonbase.html")
###############################################################################################################


def adminhome(request):
    m="SELECT * FROM `tblcustomer`"
    c.execute(m)
    data=c.fetchall()
    return render(request, "adminhome.html",{"data":data})

###############################################################################################################


def login(request):
    msg = ""
    if(request.POST):
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        s = "select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            s = "select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i = c.fetchone()
            if(i[1] == pwd):
                request.session['email'] = email
                if(i[3] == "1"):
                    if(i[2] == "admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2] == "architect"):
                        return HttpResponseRedirect("/architecthome")
                    elif(i[2] == "designer"):
                        return HttpResponseRedirect("/designerhome")
                    elif(i[2] == "contractor"):
                        return HttpResponseRedirect("/contractorhome")
                    elif(i[2] == "customer"):
                        return HttpResponseRedirect("/customerhome")
                    elif(i[2] == "shop"):
                        return HttpResponseRedirect("/shophome")
                else:
                    msg = "You are not authenticated to login"
            else:
                msg = "Incorrect password"
        else:
            msg = "User doesnt exist"
    return render(request, "login.html", {"msg": msg})

######################################################################################################


def architect(request):
    msg = ""
    if(request.POST):
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        quali = request.POST.get("txtquali")

        qproof = request.FILES["prooff"]
        print(quali)
        fs = FileSystemStorage()
        filename = fs.save(qproof.name, qproof)
        uploaded_file = fs.url(filename)

        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")

        img = request.FILES["txtFile"]
        fs = FileSystemStorage()
        fileimg = fs.save(img.name, img)
        uploaded_file_url = fs.url(fileimg)

        s = "select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "User already registered"
        else:
            s = "insert into tblarchitect(aName,aAddress,aContact,aqualification,aqproof,aEmail,aPhoto) values('"+str(name)+"','"+str(
                address)+"','"+str(contact)+"','"+str(quali)+"','"+str(uploaded_file)+"','"+str(email)+"','"+str(uploaded_file_url)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (username,password,utype,status) values('"+str(
                    email)+"','"+str(pwd)+"','architect','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login error"
                else:
                    msg = "Registration successfull"

    return render(request, "architect.html", {"msg": msg})

  ######################################################################################################


def designer(request):
    """ 
        The function for designer registration
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        quali = request.POST.get("txtquali")
        qproof = request.FILES["txtproof"]
        fs = FileSystemStorage()
        filename = fs.save(qproof.name, qproof)
        uploaded_file = fs.url(filename)
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        img = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        s = "select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "User already registered"
        else:
            s = "insert into tbldesigner(dName,dAddress,dContact,dqualification,dqproof,dEmail,dPhoto) values('"+str(name)+"','"+str(
                address)+"','"+str(contact)+"','"+str(quali)+"','"+str(uploaded_file)+"','"+str(email)+"','"+str(uploaded_file_url)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (username,password,utype,status) values('"+str(
                    email)+"','"+str(pwd)+"','designer','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login error"
                else:
                    msg = "Registration successfull"
    return render(request, "designer.html", {"msg": msg})

########################################################################################################


def contractor(request):
    """ 
        The function for contractor registration
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        pw = request.FILES["txtpw"]
        fs = FileSystemStorage()
        filename = fs.save(pw.name, pw)
        uploaded_file = fs.url(filename)

        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")

        img = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        s = "select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "User already registered"
        else:
            s = "insert into tblcontractor(cName,cAddress,cContact,cprework,cEmail,cPhoto) values('"+str(name)+"','"+str(
                address)+"','"+str(contact)+"','"+str(uploaded_file)+"','"+str(email)+"','"+str(uploaded_file_url)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (username,password,utype,status) values('"+str(
                    email)+"','"+str(pwd)+"','contractor','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login error"
                else:
                    msg = "Registration successfull"
    return render(request, "contractor.html", {"msg": msg})
#######################################################################################################


def customer(request):
    """ 
        The function for customer registration
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        aadhar = request.FILES["txtaadhar"]
        fs = FileSystemStorage()
        filename = fs.save(aadhar.name, aadhar)
        uploaded_file_url = fs.url(filename)
        s = "select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "User already registered"
        else:
            s = "insert into tblcustomer(cName,cAddress,cContact,cEmail,aadhar) values('"+str(
                name)+"','"+str(address)+"','"+str(contact)+"','"+str(email)+"','"+str(uploaded_file_url)+"')"
            print(s)
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (username,password,utype,status) values('"+str(
                    email)+"','"+str(pwd)+"','customer','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login error"
                else:
                    msg = "Registration successfull"
    return render(request, "customer.html", {"msg": msg})
##################################################################################


def adminarchitect(request):
    """ 
        The function for architect details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    s = "select * from tblarchitect where aEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data = c.fetchall()
    print("*"*300)
    print(data)
    print("*"*300)

    s = "select * from tblarchitect where aEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1 = c.fetchall()
    print("*"*300)
    print(data1)
    print("*"*300)
    return render(request, "adminarchitect.html", {"data": data, "data1": data1})
#########################################################################################################


def admindesigner(request):
    """ 
        The function for designer details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    s = "select * from tbldesigner where dEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data = c.fetchall()
    s = "select * from tbldesigner where dEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1 = c.fetchall()
    return render(request, "admindesigner.html", {"data": data, "data1": data1})

###############################################################################################################


def admincontractor(request):
    """ 
        The function for contractor details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    s = "select * from tblcontractor where cEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data = c.fetchall()
    s = "select * from tblcontractor where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1 = c.fetchall()

    return render(request, "adminconstractor.html", {"data": data, "data1": data1})

###################################################################################################


def admincustomer(request):
    """ 
        The function for customer details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    s = "select * from tblcustomer where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data = c.fetchall()
    return render(request, "admincustomer.html", {"data": data})


###################################################################################################
def adminapproveuser(request):
    """ 
        The function to approve users
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.GET.get("id")
    status = request.GET.get("status")
    url = request.GET.get("url")
    s = "update tbllogin set status='"+status+"' where username='"+email+"'"
    c.execute(s)
    db.commit()
    c.execute("select utype from tbllogin where username='"+email+"'")
    k = c.fetchone()
    if(k[0] == 'architect'):
        n = "Select aContact from tblarchitect where aEmail='"+email+"'"
        c.execute(n)
        d = c.fetchone()
        contact = d[0]
        msg = "Your registeration is approved"

    if(k[0] == 'designer'):
        n = "Select dContact from tbldesigner where dEmail='"+email+"'"
        c.execute(n)
        d = c.fetchone()
        contact = d[0]
        msg = "Your registeration is approved"

    if(k[0] == 'contractor'):
        n = "Select cContact from tblcontractor where cEmail='"+email+"'"
        c.execute(n)
        d = c.fetchone()
        contact = d[0]
        msg = "Your registeration is approved"

    if(k[0] == 'customer'):
        n = "Select cContact from tblcustomer where cEmail='"+email+"'"
        c.execute(n)
        d = c.fetchone()
        contact = d[0]
        msg = "Your registeration is approved"

    if(k[0] == 'shop'):
        n = "Select scontact from shop where semail='"+email+"'"
        c.execute(n)
        d = c.fetchone()
        contact = d[0]
        msg = "Your registeration is approved"

    return HttpResponseRedirect(url)


def deletecon(request):
    email = request.GET.get("email")
    print(email)
    c.execute("delete from tblcontractor where cEmail='"+str(email)+"'")
    db.commit()
    return HttpResponseRedirect("admincontractor")


def customerhome(request):
    """ 
        The function for customer home
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select * from tblcustomer where cEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    if request.POST:
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        email = request.POST.get("txtEmail")
        e = "update tblcustomer set cName='"+str(name)+"',cAddress='"+str(
            address)+"',cContact='"+str(contact)+"' where cEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/customerhome")
    return render(request, "customerhome.html", {"data": data})
###############################################################################################################


def customerrequirement(request):
    """ 
        The function for customer requirement
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    msg = ""
    if(request.POST):
        bed = request.POST["txtBed"]
        bath = request.POST["txtBath"]
        attached = request.POST["txtAttached"]
        car = request.POST["txtCar"]
        kitchen = request.POST["txtKitchen"]
        sitout = request.POST["txtSitout"]
        work = request.POST["txtWork"]
        floor = request.POST["txtFloor"]
        sqft = request.POST["txtSqft"]
        other = request.POST["txtOther"]
        s = "insert into tblrequirement(cEmail,bedroom,bathroom,attached,carporch,kitchen,sitout,workarea,floor,sqft,other,reqDate,reqStatus) values('"+email + \
            "','"+bed+"','"+bath+"','"+attached+"','"+car+"','"+kitchen+"','"+sitout+"','" + \
            work+"','"+floor+"','"+sqft+"','"+other + \
            "',(select sysdate()),'requested')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Requirement submitted"
    s = "Select * from tblrequirement where cEmail='"+email + \
        "'  and tblrequirement.reqStatus='requested'"
    c.execute(s)
    data = c.fetchall()

    email = request.session["email"]
    s1 = "Select * from tblrequirement where cEmail='"+email+"'"
    c.execute(s1)
    data1 = c.fetchall()
    return render(request, "customerrequirement.html", {"msg": msg, "data": data, "data1": data1})

########################################################################################################


def editreq(request):
    reqid = request.GET.get("reqid")
    s1 = "Select * from tblrequirement where reqid='"+reqid+"'"
    c.execute(s1)
    data1 = c.fetchone()
    if request.POST:
        t1 = request.POST.get("t1")
        t2 = request.POST.get("t2")
        t3 = request.POST.get("t3")
        t4 = request.POST.get("t4")
        t5 = request.POST.get("t5")
        t6 = request.POST.get("t6")
        t7 = request.POST.get("t7")
        t8 = request.POST.get("t8")
        t9 = request.POST.get("t9")
        t10 = request.POST.get("t10")
        e = "update tblrequirement set bedroom='"+str(t1)+"',bathroom='"+str(t2)+"',attached='"+str(t3)+"',carporch='"+str(t4)+"',kitchen='"+str(
            t5)+"',sitout='"+str(t6)+"',workarea='"+str(t7)+"',floor='"+str(t8)+"',sqft='"+str(t9)+"',other='"+str(t10)+"'  where reqid='"+str(reqid)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/customerrequirement")

    return render(request, "editreq.html", {"data": data1})

###############################################################################################################


def account(request):
    msg = ""
    uid = request.session['email']
    if "add" in request.POST:
        upi = request.POST.get("upi")
        cardno = request.POST.get("cardno")
        cvv = request.POST.get("cvv")
        exp = request.POST.get("exp")
        upi = request.POST.get("upi")

        uid = request.session['email']
        s = "insert into account(u_id,acc_no,card_no,cvv,exp_date,upi,bal) values('"+str(
            uid)+"','"+str(upi)+"','"+str(cardno)+"','"+str(cvv)+"','"+str(exp)+"','"+str(upi)+"','0')"
        print(s)
        c.execute(s)
        db.commit()
        msg = "Added  Successfully"
    s = "Select * from account where u_id='"+uid+"'"
    c.execute(s)
    data2 = c.fetchone()
    print(data2)
    if 'update' in request.POST:
        upi = request.POST.get("upi")
        cardno = request.POST.get("cardno")
        cvv = request.POST.get("cvv")

        uid = request.session['email']

        qry = "UPDATE account SET acc_no='"+str(upi)+"',`card_no`='"+str(
            cardno)+"',cvv='"+str(cvv)+"',upi='"+str(upi)+"' WHERE `u_id`='"+str(uid)+"'"
        c.execute(qry)
        print(qry)
        db.commit()
        return HttpResponseRedirect("/account")
    return render(request, "customeraccount.html", {"msg": msg, "data2": data2})

####################################################################################################################


def assignarchitect(request):
    msg = ""
    data = ""

    if(request.POST):
        msg = ""

        reqid = request.GET.get('reqid')
        aid = request.POST.get('archid')
        m = "insert into tblallocation(requid,archid,status) values('" + \
            str(reqid)+"','"+str(aid)+"','assigned')"
        c.execute(m)
        db.commit()
        print("assign query", m)

        msg = "Assigned successfuly"
    n = "select * from tblarchitect,tbllogin where tbllogin.status='1' and tblarchitect.aEmail=tbllogin.username "
    c.execute(n)
    data1 = c.fetchall()
    print(data1)
    data = showarchitect()
    return render(request, "assignarchitect.html", {"data": data, "msg": msg, "data1": data1})


def showarchitect():

    data = ""
    c.execute(
        "select * from tblarchitect where aEmail in(select username from tbllogin where status='1')")

    data = c.fetchall()
    return data

############################################################################################################


def architecthome(request):

    email = request.session["email"]
    s = "select * from tblarchitect where aEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    if request.POST:
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        email = request.POST.get("txtEmail")
        e = "update tblarchitect set aName='"+str(name)+"',aAddress='"+str(
            address)+"',aContact='"+str(contact)+"' where aEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/architecthome")
    return render(request, "architecthome.html", {"data": data})

###################################################################################################################


def architectrequest(request):
    email = request.session['email']
    s = "select tblrequirement.*,tblcustomer.cName from tblcustomer,tblrequirement,tblallocation,tblarchitect where tblrequirement.cEmail=tblcustomer.cEmail and tblallocation.Status='assigned' and tblallocation.archid='" + \
        str(email)+"' and tblallocation.archid=tblarchitect.aEmail and tblallocation.requid=tblrequirement.reqId and tblrequirement.reqStatus='requested'"
    print("0"*20)
    print(s)
    print("0"*20)
    c.execute(s)
    data = c.fetchall()
    print(data)
    print("0"*20)
    return render(request, "architectrequirement.html", {"data": data})
##################################################################################################################


def architectrequest(request):

    email = request.session['email']
    s = "select tblrequirement.*,tblcustomer.cName from tblcustomer,tblrequirement,tblallocation,tblarchitect where tblrequirement.cEmail=tblcustomer.cEmail and tblallocation.Status='assigned' and tblallocation.archid='" + \
        str(email)+"' and tblallocation.archid=tblarchitect.aEmail and tblallocation.requid=tblrequirement.reqId and tblrequirement.reqStatus='requested'"
    print("0"*20)
    print(s)
    print("0"*20)
    c.execute(s)
    data = c.fetchall()
    print(data)
    print("0"*20)
    return render(request, "architectrequirement.html", {"data": data})
#############################################################################################################


def architectaddplan(request):

    msg = ""
    email = request.session["email"]
    rid = request.GET.get("id")

    if(request.POST):
        img = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        sqft = request.POST["txtSqft"]
        cost = request.POST["txtCost"]
        fees = int(sqft)*2
        s = "insert into tblplan (aEmail,reqId,plan,sqft,cost,planStatus,fees) values('"+email + \
            "','"+rid+"','"+uploaded_file_url+"','"+sqft + \
            "','"+cost+"','submitted','"+str(fees)+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            s = "update tblrequirement set reqStatus='plan uploaded' where reqId='"+rid+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry error"
            else:
                msg = "Plan added"
    return render(request, "architectaddplan.html", {"msg": msg})

#############################################################################################################


def architectplan(request):

    email = request.session["email"]
    s = "select tblrequirement.reqId,tblcustomer.cName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.plan,tblplan.`feesstatus` from tblrequirement,tblplan,tblcustomer where tblcustomer.cEmail=tblrequirement.cEmail and tblplan.reqId=tblrequirement.reqId and tblplan.aEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    print(data)
    return render(request, "architectplan.html", {"data": data})
###################################################################################################################


def customerviewplans(request):
    email = request.session["email"]
    s = "Select * from tblrequirement where cEmail='"+email + \
        "'  and tblrequirement.reqStatus<>'plan approved'"
    c.execute(s)
    data1 = c.fetchall()
    print(data1)

    email = request.session["email"]
    s1 = "select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan,tblplan.fees from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail='" + \
        email + \
        "' and (tblplan.planStatus='approved' or tblplan.planStatus='3D requested')"
    c.execute(s1)
    data12 = c.fetchall()
    print(data12)
    return render(request, "customerviewplans.html", {"data1": data1, "data12": data12})

###################################################################################################################


def customerplan(request):
    """ 
        The function to load plan status
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    rid = request.GET.get("id")
    s = "select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblplan.reqId='" + \
        str(rid)+"' and tblrequirement.cEmail='"+str(email)+"'"
    c.execute(s)
    data = c.fetchall()

    email = request.session["email"]
    s12 = "select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan,tblplan.fees from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail='" + \
        email + \
        "' and (tblplan.planStatus='approved' or tblplan.planStatus='3D requested')"
    c.execute(s12)
    data12 = c.fetchall()
    print(data12)
    return render(request, "customerplan.html", {"data": data, "data12": data12})

######################################################################################################################


def customerplanupdate(request):

    pid = request.GET.get("id")
    fees = request.GET.get("fees")
    rid = request.GET.get("rid")

    request.session["pid"] = pid
    request.session["fees"] = fees
    request.session["rid"] = rid

    status = request.GET.get("status")
    url = request.GET.get("url")
    rid = request.GET.get("rid")
    s = "update tblplan set planStatus='"+status + \
        "',feesstatus='paid' where planId='"+pid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        if(status == "approved"):
            status1 = "rejected"
        elif(status == "rejected"):
            status1 = "approved"
        s = "update tblplan set planStatus='"+status1 + \
            "' where reqId='"+rid+"' and planId<>'"+pid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            if(status == "approved"):
                status = "plan approved"
                s = "update tblrequirement set reqStatus='"+status+"' where reqId='"+rid+"'"
                try:
                    c.execute(s)
                    db.commit()
                    url = 'first'
                except:
                    pass
                else:
                    url = 'first'
                    return HttpResponseRedirect("/"+url+"?id="+pid)

            else:
                return HttpResponseRedirect("/"+url)



#################################################################################################

 #                             PAYMENT PAGES

def first(request):
    if request.POST:
        return HttpResponseRedirect("/second")
    return render(request, "first.html")


def second(request):
    if request.POST:
        return HttpResponseRedirect("/third")
    return render(request, "second.html")


def third(request):
    return HttpResponseRedirect("/fourth")


def fourth(request):
    return HttpResponseRedirect("/fifth")


def fifth(request):
    
    
    return render(request, "Fifth.html")


#################################################################################################
def feedback(request):
    msg = ""
    uid = request.session['email']
    if(request.POST):
        msg = ""

        desc = request.POST.get('feedback')
        m = "INSERT INTO `feedback`(`feedback`,`uid`)VALUES('" + \
            str(desc)+"','"+str(uid)+"')"
        c.execute(m)
        db.commit()
        print(m)
        msg = "Message Added"

    return render(request, "customeraddfeedback.html", {"msg": msg})
######################################################################################################


def viewfeedback(request):

    data = ""
    c.execute(
        "select feedback.*,tblcustomer.* from feedback join tblcustomer on feedback.uid=tblcustomer.cEmail")

    data = c.fetchall()
    print(data)
    return render(request, "adminviewfeedback.html", {"data": data})

##########################################################################################################


def designerhome(request):

    email = request.session["email"]
    s = "select * from tbldesigner where dEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    if request.POST:
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        email = request.POST.get("txtEmail")
        e = "update tbldesigner set dName='"+str(name)+"',dAddress='"+str(
            address)+"',dContact='"+str(contact)+"' where dEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/designerhome")

    return render(request, "designerhome.html", {"data": data})


#############################################################################################################

def contractorhome(request):

    email = request.session["email"]
    s = "select * from tblcontractor where cEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    if request.POST:
        name = request.POST.get("txtName")
        address = request.POST.get("txtAddress")
        contact = request.POST.get("txtContact")
        email = request.POST.get("txtEmail")
        e = "update tblcontractor set cName='"+str(name)+"',cAddress='"+str(
            address)+"',cContact='"+str(contact)+"' where cEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/contractorhome")
    return render(request, "contractorhome.html", {"data": data})

###########################################################################################################


def customerviewplan(request):
    """ 
        The function to view plan
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    plan = request.GET.get("id")
    return render(request, "customerviewplan.html", {"plan": plan})


#############################################################################################################

def customerplan(request):
    """ 
        The function to load plan status
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    rid = request.GET.get("id")
    s = "select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblplan.reqId='" + \
        str(rid)+"' and tblrequirement.cEmail='"+str(email)+"'"
    c.execute(s)
    data = c.fetchall()

    email = request.session["email"]
    s12 = "select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan,tblplan.fees from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail='" + \
        email + \
        "' and (tblplan.planStatus='approved' or tblplan.planStatus='3D requested')"
    c.execute(s12)
    data12 = c.fetchall()
    print(data12)
    return render(request, "customerplan.html", {"data": data, "data12": data12})

##################################################################################################################


def customerviewdesigner(request):
    msg=data=""
    print("*"*90)
    y = request.GET.get("id")
    print(y)
    request.session["planid"] = y
    c.execute("select COUNT(planId) FROM `tbldesignrequest` WHERE planId='"+str(y)+"'")
    k=c.fetchone()
    if int(k[0])>0:
        msg="ALREADY REQUESTED"
       
    else:
        s = "select * from tbldesigner where dEmail in (select username from tbllogin where status='1')"
        c.execute(s)
        data = c.fetchall()
       
    
    return render(request, "customerviewdesigner.html", {"data": data,"msg": msg})

################################################################################################################




#############################################################################################################
def customerpassplan(request):
    email = request.GET.get("id")
    planid = request.session["planid"]

    s = "SELECT COUNT(planId) FROM `tbldesignrequest` WHERE planId='"+planid+"'"
    c.execute(s)
    i=c.fetchone()
    if(i[0]>0):
           msg="Already requested"
    else:
        s = "insert into tbldesignrequest(planId,dEmail,dreqStatus) values('"+str(
        planid)+"','"+str(email)+"','requested')"
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        s = "update tblplan set planStatus='3D requested' where planId='" + \
            str(planid)+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/customerdesignrequest") 
###########################################################################################################  

def customerdesignrequest(request):
    """ 
        The function for request for design
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblrequirement.reqId,tbldesigner.dName,tblplan.sqft,tblplan.cost,tbldesignrequest.dreqId,tbldesignrequest.dreqStatus from tblrequirement,tbldesigner,tblplan,tbldesignrequest where tblrequirement.reqId=tblplan.reqId and tblplan.planId=tbldesignrequest.planid and tbldesigner.dEmail=tbldesignrequest.dEmail and tblrequirement.cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerdesignrequest.html",{"data":data})   

#############################################################################################################   

def designerrequest(request):
    """ 
        The function to view all design request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblcustomer.cName,tblcustomer.cAddress,tblcustomer.cContact,tblplan.plan,tblplan.sqft,tbldesignrequest.dreqId from tbldesignrequest,tblcustomer,tblplan,tblrequirement where tbldesignrequest.dEmail='"+str(email)+"' and tbldesignrequest.planId=tblplan.planId and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail=tblcustomer.cEmail and tbldesignrequest.dreqStatus='requested'"
    print(s)
    c.execute(s)
    data=c.fetchall()
    print(data)
    return render(request,"designerrequest.html",{"data":data})

####################################################################################################

def designeraddvideo(request):
    """ 
        The function to view all design request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    dreqid=request.GET.get("id")
    if(request.POST):
        fees=request.POST["fees"]
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)
        s="insert into tblvideo (dreqId,video,videoStatus,amount) values('"+dreqid+"','"+uploaded_file_url+"','video uploaded','"+fees+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            s="update tbldesignrequest set dreqStatus='video uploaded' where dreqId='"+dreqid+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry som error"
            else:
                msg="Video added successfully"
    return render(request,"designeraddvideo.html",{"msg":msg})

########################################################################################################
def designerviewwork(request):
    email=request.session["email"]
    s="SELECT tblcustomer.`cName`, tblcustomer.`cContact`,tblcustomer.`cEmail`,tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.videoId,tblvideo.amount,tblplan.plan,`tblvideo`.`paymentstatus` FROM `tblcustomer`,tbldesignrequest,tbldesigner,tblvideo,tblplan WHERE tbldesignrequest.planId=tblplan.reqid AND tbldesignrequest.dreqId=tblvideo.dreqId AND tbldesignrequest.dEmail=tbldesigner.dEmail  AND tbldesignrequest.dEmail='"+str(email)+"'"
    print(s)
    c.execute(s)
    data=c.fetchall()
    print("*"*90)
    print(data)
    print("@"*90)
    return  render(request,"dviewvideo.html",{"data":data})

##############################################################################################################

def customervideo(request):
  
    email=request.session["email"]
    s="SELECT tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.`video`,tblvideo.amount FROM tbldesignrequest,tbldesigner,tblvideo WHERE tbldesignrequest.dreqId=tblvideo.dreqId AND tbldesignrequest.dEmail=tbldesigner.dEmail AND tbldesignrequest.planId IN(SELECT planId FROM tblplan WHERE reqId IN(SELECT reqId FROM tblrequirement WHERE cEmail='"+email+"')) AND tbldesignrequest.dreqStatus='video uploaded'"
    c.execute(s)
    data=c.fetchall()
    
    print("*"*300)
    print(data)
    print("*"*300)

    s="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.videoId,tblvideo.amount from tbldesignrequest,tbldesigner,tblvideo where tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) and tbldesignrequest.dreqStatus='video approved'"
    c.execute(s)
    data1=c.fetchall()



    s1="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.video,tblvideo.videoId,tblvideo.amount from tbldesignrequest,tbldesigner,tblvideo where tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) "
    print(s1)
    c.execute(s1)
    pdata=c.fetchall()
    return render(request,"customervideo.html",{"data":data,"data1":data1,"pdata":pdata})

#############################################################################################################

def customerselectcontractor(request):

    s="select * from tblcontractor where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    print(data)
    return render(request,"customerselectcontractor.html",{"data":data})

###################################################################################################

def customervideoupdate(request):
  
    pid=request.GET.get("id")
    print("piddd=",pid)
    fees=request.GET.get("fees")
    print("fees=",fees)

    request.session["vid"]=pid
    request.session["fees"]=fees
    print(request.session["vid"])

    status=request.GET.get("status")
    print(status)
    url=request.GET.get("url")
    s="update `tblvideo` set `videoStatus`='"+status+"', `paymentstatus`='paid' where `dreqId`='"+pid+"'"
    print("qryresult :",s)
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        if(status=="approved"):
                status="video approved"
                s="update tbldesignrequest set dreqStatus='"+status+"' where dreqId in(select dreqId from tblvideo where dreqId	='"+pid+"')"
                print(s)
                try:
                    c.execute(s)
                    db.commit()
                  
                except:
                    pass
                else:
                    url = 'first1'
                    return HttpResponseRedirect("/"+url+"?amount="+fees)
        else:
                return HttpResponseRedirect(url)
            
 #################################################################################################################
 
 
 
def first1(request):
    if request.POST:
        return HttpResponseRedirect("/second1")
    return render(request, "first.html")


def second1(request):
    if request.POST:
        return HttpResponseRedirect("/third1")
    return render(request, "second.html")


def third1(request):
    return render(request, "Third1.html")

def fourth1(request):
    return render(request, "Fourth1.html")


def fifth1(request):
    
    return render(request, "fifth1.html")


#######################################################################################################################
def customerassignwork(request):
    """ 
        The function for request for contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    
    pid=request.session["vid"]
    fees=request.session["fees"]
    
    cemail=request.GET.get("id")
    vid=request.session["vid"]
    
    s="insert into tblwork (videoId,cEmail,wDate,wStatus) values('"+str(vid)+"','"+str(cemail)+"',(select sysdate()),'assigned')"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/customerhome")

####################################################################################################################

def contractorrequest(request):
    """ 
        The function to view contractor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    print(email)
    s="SELECT tblwork.`workId`,tblvideo.`video`,tblcustomer.cName,tblcustomer.cAddress,tblcustomer.cContact,tblplan.plan,tblplan.sqft,tblwork.*,tblrequirement.* FROM tblrequirement JOIN tblcustomer ON tblrequirement.cEmail=tblcustomer.cEmail JOIN tblplan ON tblplan.reqId=tblrequirement.`reqId` JOIN tbldesignrequest ON tbldesignrequest.planId=tblplan.`planId` JOIN tblvideo ON tblvideo.`dreqId`=tbldesignrequest.dreqId JOIN tblwork ON tblwork.`videoId`=tblvideo.`dreqId` WHERE tblwork.cEmail='"+email+"' AND tblwork.wStatus='assigned'"
    print("0"*100)
    print(s)
    print("0"*100)
    c.execute(s)
    data=c.fetchall()
    print(data)
    print("0"*100)
    return render(request,"contractorrequest.html",{"data":data})

###############################################################################################################

def contractorapprove(request):
    if(request.GET):

        workid=request.GET.get("workid")
        m="UPDATE tblwork SET `wStatus`='Approved' WHERE `workId`='"+str(workid)+"'"
        c.execute(m)
        print(m)
        db.commit()
    return render(request,"contractorrequest.html")

#######################################################################################################


def contractorreject(request):
    if(request.GET):

        workid=request.GET.get("workid")
        m="UPDATE tblwork SET `wStatus`='Rejected' WHERE `workId`='"+str(workid)+"'"
        c.execute(m)
        print(m)
        db.commit()
    return render(request,"contractorrequest.html")


###############################################################################
 
def contractorprequest(request):

    email=request.session["email"]
    s="SELECT tblwork.`workId`,tblvideo.`video`,tblcustomer.cName,tblcustomer.cAddress,tblcustomer.cContact,tblplan.plan,tblplan.sqft,tblwork.*,tblrequirement.* FROM tblrequirement JOIN tblcustomer ON tblrequirement.cEmail=tblcustomer.cEmail JOIN tblplan ON tblplan.reqId=tblrequirement.`reqId` JOIN tbldesignrequest ON tbldesignrequest.planId=tblplan.`planId` JOIN tblvideo ON tblvideo.`dreqId`=tbldesignrequest.dreqId JOIN tblwork ON tblwork.`videoId`=tblvideo.`dreqId` WHERE tblwork.cEmail='"+email+"' and tblwork.wstatus='Approved'"
    print("#"*100)

    print(s)
    print("#"*100)
    c.execute(s)
    data=c.fetchall()

    return render(request,"contractorprequest.html",{"data":data})
###########################################################################################################

# def viewgallery(request):
#     email = request.session['email']
#     query="SELECT * FROM `gallery` WHERE `email`='"+email+"'"
#     print(query)
#     c.execute(query)
#     db.commit()
#     print(query)
#     data=c.fetchall()
#     return render(request,"ViewGallery.html",{"data12":data})


def addgallery(request):
    
    msg = ""
    data=""
    email = request.session['email']
    uid = request.session['email']
    query="SELECT * FROM `gallery` WHERE `email`='"+email+"'"
    print(query)
    c.execute(query)
    db.commit()
    print(query)
    data=c.fetchall()
    if request.POST:
        s = "SELECT COUNT(*) FROM `gallery` WHERE email='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            image1 = request.FILES["txtFile1"]
            image2 = request.FILES["txtFile2"]
            image3 = request.FILES["txtFile2"]
            image4 = request.FILES["txtFile3"]

            fs = FileSystemStorage()
            filename1 = fs.save(image1.name, image1)
            filename2 = fs.save(image2.name, image2)
            filename3 = fs.save(image3.name, image3)
            filename4 = fs.save(image4.name, image4)
            uploaded_file1 = fs.url(filename1)
            uploaded_file2 = fs.url(filename2)
            uploaded_file3 = fs.url(filename3)
            uploaded_file4= fs.url(filename4)
            q="UPDATE gallery SET `image1`='"+str(uploaded_file1)+"',image2='"+str(uploaded_file2)+"',image3='"+str(uploaded_file3)+"',image4='"+str(uploaded_file4)+"' WHERE email='"+str(email)+"'"
            c.execute(q)
            db.commit()
            print(q)
            return HttpResponseRedirect("/addgallery")
        else:
            image1 = request.FILES["txtFile1"]
            image2 = request.FILES["txtFile2"]
            image3 = request.FILES["txtFile2"]
            image4 = request.FILES["txtFile3"]

            fs = FileSystemStorage()
            filename1 = fs.save(image1.name, image1)
            filename2 = fs.save(image2.name, image2)
            filename3 = fs.save(image3.name, image3)
            filename4 = fs.save(image4.name, image4)
            uploaded_file1 = fs.url(filename1)
            uploaded_file2 = fs.url(filename2)
            uploaded_file3 = fs.url(filename3)
            uploaded_file4= fs.url(filename4)
            
            qry="INSERT INTO `gallery`(`email`,`image1`,`image2`,`image3`,`image4`)VALUES('"+str(uid)+"','"+str(uploaded_file1)+"','"+str(uploaded_file2)+"','"+str(uploaded_file3)+"','"+str(uploaded_file4)+"')"
            c.execute(qry)
            db.commit()
            print(qry)
            msg = "Photo Added"
    return render(request,"addgallery.html",{"msg":msg,"data12":data})

def designeraddgallery(request):
    
    msg = ""
    data=""
    email = request.session['email']
    uid = request.session['email']
    query="SELECT * FROM `gallery` WHERE `email`='"+email+"'"
    print(query)
    c.execute(query)
    db.commit()
    print(query)
    data=c.fetchall()
    if request.POST:
        s = "SELECT COUNT(*) FROM `gallery` WHERE email='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            image1 = request.FILES["txtFile1"]
            image2 = request.FILES["txtFile2"]
            image3 = request.FILES["txtFile2"]
            image4 = request.FILES["txtFile3"]

            fs = FileSystemStorage()
            filename1 = fs.save(image1.name, image1)
            filename2 = fs.save(image2.name, image2)
            filename3 = fs.save(image3.name, image3)
            filename4 = fs.save(image4.name, image4)
            uploaded_file1 = fs.url(filename1)
            uploaded_file2 = fs.url(filename2)
            uploaded_file3 = fs.url(filename3)
            uploaded_file4= fs.url(filename4)
            q="UPDATE gallery SET `image1`='"+str(uploaded_file1)+"',image2='"+str(uploaded_file2)+"',image3='"+str(uploaded_file3)+"',image4='"+str(uploaded_file4)+"' WHERE email='"+str(email)+"'"
            c.execute(q)
            db.commit()
            print(q)
            return HttpResponseRedirect("/addgallery")
        else:
            image1 = request.FILES["txtFile1"]
            image2 = request.FILES["txtFile2"]
            image3 = request.FILES["txtFile2"]
            image4 = request.FILES["txtFile3"]

            fs = FileSystemStorage()
            filename1 = fs.save(image1.name, image1)
            filename2 = fs.save(image2.name, image2)
            filename3 = fs.save(image3.name, image3)
            filename4 = fs.save(image4.name, image4)
            uploaded_file1 = fs.url(filename1)
            uploaded_file2 = fs.url(filename2)
            uploaded_file3 = fs.url(filename3)
            uploaded_file4= fs.url(filename4)
            
            qry="INSERT INTO `gallery`(`email`,`image1`,`image2`,`image3`,`image4`)VALUES('"+str(uid)+"','"+str(uploaded_file1)+"','"+str(uploaded_file2)+"','"+str(uploaded_file3)+"','"+str(uploaded_file4)+"')"
            c.execute(qry)
            db.commit()
            print(qry)
            msg = "Photo Added"
    return render(request,"designergallery.html",{"msg":msg,"data12":data})

def contractoraddgallery(request):
    
    msg = ""
    data=""
    email = request.session['email']
    uid = request.session['email']
    query="SELECT * FROM `gallery` WHERE `email`='"+email+"'"
    print(query)
    c.execute(query)
    db.commit()
    print(query)
    data=c.fetchall()
    if request.POST:
        s = "SELECT COUNT(*) FROM `gallery` WHERE email='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            image1 = request.FILES["txtFile1"]
            image2 = request.FILES["txtFile2"]
            image3 = request.FILES["txtFile2"]
            image4 = request.FILES["txtFile3"]

            fs = FileSystemStorage()
            filename1 = fs.save(image1.name, image1)
            filename2 = fs.save(image2.name, image2)
            filename3 = fs.save(image3.name, image3)
            filename4 = fs.save(image4.name, image4)
            uploaded_file1 = fs.url(filename1)
            uploaded_file2 = fs.url(filename2)
            uploaded_file3 = fs.url(filename3)
            uploaded_file4= fs.url(filename4)
            q="UPDATE gallery SET `image1`='"+str(uploaded_file1)+"',image2='"+str(uploaded_file2)+"',image3='"+str(uploaded_file3)+"',image4='"+str(uploaded_file4)+"' WHERE email='"+str(email)+"'"
            c.execute(q)
            db.commit()
            print(q)
            return HttpResponseRedirect("/addgallery")
        else:
            image1 = request.FILES["txtFile1"]
            image2 = request.FILES["txtFile2"]
            image3 = request.FILES["txtFile2"]
            image4 = request.FILES["txtFile3"]

            fs = FileSystemStorage()
            filename1 = fs.save(image1.name, image1)
            filename2 = fs.save(image2.name, image2)
            filename3 = fs.save(image3.name, image3)
            filename4 = fs.save(image4.name, image4)
            uploaded_file1 = fs.url(filename1)
            uploaded_file2 = fs.url(filename2)
            uploaded_file3 = fs.url(filename3)
            uploaded_file4= fs.url(filename4)
            
            qry="INSERT INTO `gallery`(`email`,`image1`,`image2`,`image3`,`image4`)VALUES('"+str(uid)+"','"+str(uploaded_file1)+"','"+str(uploaded_file2)+"','"+str(uploaded_file3)+"','"+str(uploaded_file4)+"')"
            c.execute(qry)
            db.commit()
            print(qry)
            msg = "Photo Added"
    return render(request,"contractorgallery.html",{"msg":msg,"data12":data})

def customerviewgal(request):
    a="SELECT * FROM `tblarchitect`"
    print(a)
    c.execute(a)
    db.commit()
    print(a)
    data=c.fetchall()
    
    cc="SELECT * FROM `tblcontractor`"
    print(cc)
    c.execute(cc)
    db.commit()
    print(cc)
    data1=c.fetchall()
    
    d="SELECT * FROM `tbldesigner`"
    print(d)
    c.execute(d)
    db.commit()
    print(d)
    data2=c.fetchall()
    return render(request,"customerviewgal.html",{"data":data,"data1":data1,"data2":data2})

##########################################################################################################
def moduleimages(request):
    id = request.GET['email']
    print("id",id)
    query="SELECT * FROM `gallery` WHERE `email`='"+str(id)+"'"
    print(query)
    c.execute(query)
    db.commit()
    print(query)
    data=c.fetchall()
    
    return render(request,"ViewGallery.html",{"data":data})

#############################################################################################################
def customerwork(request):
  
    email=request.session["email"]
    s="SELECT tblwork.workId,tblcontractor.cName,tblplan.sqft,tblwork.wStatus FROM tblwork,tblcontractor,tblplan,tblvideo,tbldesignrequest WHERE tblwork.videoId=tblvideo.`dreqId` AND tblvideo.dreqId=tbldesignrequest.dreqId AND tbldesignrequest.planId=tblplan.planId AND tblwork.cEmail=tblcontractor.cEmail AND tblplan.reqId IN(SELECT reqId FROM tblrequirement WHERE cEmail='"+email+"') "
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerwork.html",{"data":data})








