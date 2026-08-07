from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import (
    InvalidRatingError,
    NegativeDistanceError,
    RideHistoryError,
)

@ride_logger
def book_ride(vehicle):

    fare = vehicle.calculate_fare()

    try:
        with open("ride_history.txt", "a") as file:
            file.write(f"Driver: {vehicle.driver_name}\n")
            file.write(f"Vehicle: {vehicle.__class__.__name__}\n")
            file.write(f"Distance: {vehicle.distance} km\n")
            file.write(f"Fare: Rs. {fare}\n")
            file.write("-" * 30 + "\n")

    except Exception as e:
        raise RideHistoryError(f"File Error: {e}")

    return fare

def main():

    try:
        vehicle_type = input("Enter Vehicle Type (Bike/Car): ").strip().lower()
        driver = input("Enter Driver Name: ")
        rating = float(input("Enter Rating (1-5): "))
        distance = float(input("Enter Distance (km): "))

        if vehicle_type == "bike":
            vehicle = Bike(driver, rating, distance)
        elif vehicle_type == "car":
            vehicle = Car(driver, rating, distance)
        else:
            print("Invalid vehicle type.")
            return

        fare = book_ride(vehicle)

        print("Driver :", vehicle.driver_name)
        print("Vehicle :", vehicle.__class__.__name__)
        print("Distance :", vehicle.distance, "km")
        print("Fare : Rs.", fare)

    except InvalidRatingError as e:
        print(e)

    except NegativeDistanceError as e:
        print(e)

    except RideHistoryError as e:
        print(e)

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()