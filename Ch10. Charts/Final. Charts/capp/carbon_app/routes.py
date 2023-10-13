from flask import render_template, Blueprint
from capp.carbon_app.forms import AddRecordForm
from capp.carbon_app.carbon_calculator_functions import co2_bus_calculator, co2_car_calculator, co2_plane_calculator, co2_ferry_calculator, co2_motorbike_calculator

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/carbon_app', methods=['GET', 'POST'])
def carbon_app_home():
    form = AddRecordForm()
    if form.validate_on_submit():
        bus_kms = form.bus_kms.data
        car_kms = form.car_kms.data
        plane_kms = form.plane_kms.data
        ferry_kms = form.ferry_kms.data
        motorbike_kms = form.motorbike_kms.data
        scooter_kms = form.scooter_kms.data
        bicycle_kms = form.bicycle_kms.data
        walk_kms = form.walk_kms.data

        bus_type = form.bus_type.data
        car_type = form.car_type.data
        plane_type = form.plane_type.data
        ferry_type = form.ferry_type.data
        motorbike_type = form.motorbike_type.data
        scooter_type = form.scooter_type.data
        bicycle_type = form.bicycle_type.data
        walk_type = form.walk_type.data

        co2_bus = co2_bus_calculator(bus_type, bus_kms)
        co2_car = co2_car_calculator(car_type, car_kms)
        co2_plane = co2_plane_calculator(plane_type, plane_kms)
        co2_ferry = co2_ferry_calculator(ferry_type, ferry_kms)
        co2_motorbike = co2_motorbike_calculator(motorbike_type, motorbike_kms)
        co2_scooter = float(scooter_kms) * 0
        co2_bicycle = float(bicycle_kms) * 0
        co2_walk = float(walk_kms) * 0

        co2_bus = float("{:.2f}".format(co2_bus))
        co2_car = float("{:.2f}".format(co2_car))
        co2_plane = float("{:.2f}".format(co2_plane))
        co2_ferry = float("{:.2f}".format(co2_ferry))
        co2_motorbike = float("{:.2f}".format(co2_motorbike))
        co2_scooter = float("{:.2f}".format(co2_scooter))
        co2_bicycle = float("{:.2f}".format(co2_bicycle))
        co2_walk = float("{:.2f}".format(co2_walk))

        form.bus_co2.data = co2_bus
        form.car_co2.data = co2_car
        form.plane_co2.data = co2_plane
        form.ferry_co2.data = co2_ferry
        form.motorbike_co2.data = co2_motorbike
        form.scooter_co2.data = co2_scooter
        form.bicycle_co2.data = co2_bicycle
        form.walk_co2.data = co2_walk
        return render_template('carbon_app/carbon_app2.html', title='App Calculator', legend='App Calculator', form=form, 
            co2_bus=co2_bus, co2_car=co2_car, co2_plane=co2_plane, co2_ferry=co2_ferry, co2_motorbike=co2_motorbike,
            co2_scooter=co2_scooter, co2_bicycle=co2_bicycle, co2_walk=co2_walk)
    return render_template('carbon_app/carbon_app.html', title='App Calculator', legend='App Calculator', form=form)

    