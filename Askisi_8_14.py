# Άσκηση 8-14

def make_car(owner, model, **car_info):
    """ksksks"""
    car_info['owner_name'] = owner
    car_info['model_name'] = model
    return car_info

my_car = make_car('karl benz', 'mercedes benz',
                  sport=True, drive_system='FWD')

print(my_car)
