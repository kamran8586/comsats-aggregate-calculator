from flask import Flask, render_template , request

app = Flask(__name__)


def calculate_merit(matric_percentage, fsc_percentage, nts_percentage):
    return (matric_percentage * .1) + (fsc_percentage * .4) + (nts_percentage * .5)

def calculate_percentage(obtained, total):
    return (obtained/total) * 100



@app.route("/",methods =["GET", "POST"])
def comsats_cal():

    if request.method == "POST":
        total_matric = int(request.form.get("t_matric"))
        obtained_matric = int(request.form.get("o_matric"))
        total_fsc = int(request.form.get("t_fsc"))
        obtained_fsc = int(request.form.get("o_fsc"))
        nts = int(request.form.get("nts"))

        matric_percentage = calculate_percentage(obtained_matric, total_matric)
        fsc_percentage = calculate_percentage(obtained_fsc, total_fsc)
        nts_percentage = calculate_percentage(nts, 100)
        final_merit = calculate_merit(
        matric_percentage, fsc_percentage, nts_percentage)  
        return render_template('index.html', result= final_merit)
    
    return render_template('index.html', result=0)

