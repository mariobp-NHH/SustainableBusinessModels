from flask import render_template, Blueprint
from capp.carbon_app.forms import AddRecordForm

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/carbon_app', methods=['GET', 'POST'])
def carbon_app_home():
    form = AddRecordForm()
    if form.validate_on_submit():
        return render_template('carbon_app/carbon_app2.html', title='App Calculator', legend='App Calculator', form=form)
    return render_template('carbon_app/carbon_app.html', title='App Calculator', legend='App Calculator', form=form)

    
