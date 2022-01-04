# Exercise 8-14

def make_car(manufacturer, model, **car_info):
    """Create dictionary with info about the car"""
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

my_car = make_car('Mercedes Benz', 'GT-S',
                  sport=True, drive_system='FWD')

print(my_car)