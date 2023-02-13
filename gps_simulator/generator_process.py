import random
from copy import deepcopy
from math import sqrt, atan, sin, cos
from time import sleep
from rabbit_client import RabbitEnqueuer

def __format_point__(point:str):
    sp = point.split(',')
    return {
            "long": float(sp[0]),
            "lat": float(sp[1])
        }

class ConstConfig:
    begin = 1
    end = 55
    step = 10
    decimals = 4


# in meters
def get_random() -> float:
    return random.randrange(ConstConfig.begin, ConstConfig.end, ConstConfig.step)


def calc_distance(point1,  point2):
    xd = point1["long"] - point2["long"]
    yd = point1["lat"] - point2["lat"]
    return sqrt(xd*xd + yd*yd)

def static_const(**kwargs):
    def decorate(f):
        point1 = kwargs["start"]
        point2 = kwargs["end"]
        xd = point1["long"] - point2["long"]
        yd = point1["lat"] - point2["lat"]
        angle = atan( float('inf') if xd == 0 else yd/xd )
        setattr(f, "const_x", cos(angle)/1000)
        setattr(f, "const_y", sin(angle)/1000)
        return f
    return decorate


# Since the calc is done every second the time is taken as one second
# But the result is given in km/h
def calc_speed(dist: float):
    return round(dist * 3.6, ConstConfig.decimals)


def start_trip_process(vehicle_id, departure_geo_point, destination_geo_point, queue, exchange, routing_key, driver_id):
    start = __format_point__(departure_geo_point)
    end = __format_point__(destination_geo_point)


    @static_const(start=start, end=end)
    def calc_point(distance: float, point):
        return {
            "long": round(
                distance * calc_point.const_x + point["long"],
                ConstConfig.decimals
                ),
            "lat": round(
                distance * calc_point.const_y + point["lat"],
                ConstConfig.decimals
                )
                }

    def generate_trip(vehicle_id:int, start, end, queuer: RabbitEnqueuer, driver_id):
        last = deepcopy(start)
        covered_dist, current_dist = 0, 0
        # As distance between two geo poins is given in km, we have to convert to meters
        full_dist = calc_distance(start, end) * 1000
        while current_dist < full_dist:
            last = calc_point(covered_dist, last)
            gps_data = {
                    "id": vehicle_id,
                    "geo_coordinates": last,
                    "speed": calc_speed(covered_dist),
                    "driver_id": driver_id
                    }
            queuer.basic_publish(gps_data)
            current_dist += covered_dist
            covered_dist = get_random()
            sleep(1)

        final_gps_data = gps_data = {
                    "id": vehicle_id,
                    "geo_coordinates": end,
                    "speed": calc_speed(calc_distance(last, end)),
                    "driver_id": driver_id
        }

        queuer.basic_publish(final_gps_data)

    generate_trip(
        vehicle_id=vehicle_id,
        start=start,
        end=end,
        queuer=RabbitEnqueuer(
            queue_name=queue,
            exchange=exchange,
            routing_key=routing_key
        ),
        driver_id=driver_id
    )