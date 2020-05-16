import os 
import smootimage  
from werkzeug.utils import secure_filename
from flask import Flask,request, render_template, url_for, flash,redirect,send_from_directory


app=Flask(__name__)

@app.route('/')

def index():
    return render_template('layouts/upload.html')


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/images')
UPLOAD_MASK = os.path.join(APP_ROOT, 'static/mask')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_MASK'] = UPLOAD_MASK
@app.route('/upload', methods=['GET','POST'])

def upload():
    if request.method == "POST":
        
        o_images = request.files.getlist("image[]")
        m_images = request.files.getlist("image3[]")
        g_images = request.files.getlist("image2[]")
        
        load(o_images)
        load2(g_images)
        load3(m_images)
        return redirect(url_for('showdata'))
        
            
    
    
    return render_template('layouts/upload.html')





def load(images):
    global alter_image
    for image in images:   
        alter_image=''+net(image)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        

def load2(images):
    global goal_image
    for image in images:   
        goal_image=''+net(image)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

def load3(images):
    global mask_image
    for image in images:   
        mask_image=''+net(image)
        image.save(os.path.join(app.config['UPLOAD_MASK'], image.filename))
        

def net(image):
    
    name = str(image)
    name =name.replace('<FileStorage: ','')
    name =name.replace("('image/jpeg')>", "")
    name =name.replace("('image/png')>", "")
    name =name.replace("'", "")
    return name
        
@app.route('/showtoupload', methods=['GET','POST'])

def showtoupload():
    if request.method == "POST":
        hists = os.listdir('static/images')
        mask = os.listdir('static/mask')
        for file in hists :
            os.remove("static/images/"+file)
        for file in mask :
            os.remove("static/mask/"+file)
        return redirect(url_for('index'))


@app.route('/showtoresult', methods=['GET','POST'])

def showtoresult():
    if request.method == "POST":
        #
        # เอา detectกรอบ มาใส่  mask_image  เป็นแค่ชื่อภาพที่มีmask อยู่ ที่อยู่ของไฟล์อยู่ที่ static/mask/
        # crop = cropimage.crop(alter_image,x1,y1,x4,y4)
        # แปะ รูป goal_image กับ crop   -----> final = แปะของพี่โอ(goal_image,crop)
        # smootimage.smoot(final)
        #
        return redirect(url_for('result'))  

@app.route('/resulttoshow', methods=['GET','POST'])

def resulttoshow():
    if request.method == "POST":
        hists = os.listdir('static/image')
        for file in hists :
            os.remove("static/image/"+file)

        return redirect(url_for('showdata'))              
    
    
    
@app.route('/showdata')

def showdata():
    image_names = os.listdir('./static/images')  
    print(image_names)
    return render_template("layouts/show.html", image_names=image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)



@app.route('/result')

def result():
    hists = os.listdir('static/image')
    hists = ['image/'+ file for file in hists]
    print(hists)
    return render_template("layouts/result.html", hists=hists)




if __name__=='__main__':
    app.run(debug=True)
    
