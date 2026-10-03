from test_key import main_control
from test_key import main_control_2




if __name__ == "__main__":
    soccer_tornament, first_mach_s = main_control()
    first_mach_list = first_mach_s

    basketball_tornament, first_mach_b = main_control_2(first_mach_list)
    first_mach_list = first_mach_b

    volleyball_tornament, first_mach_v = main_control_2(first_mach_list)
    first_mach_list = first_mach_v

    dodgeball_tornament, first_mach_d = main_control_2(first_mach_list)
    first_mach_list = first_mach_d
    


    print("soccer")
    for c in soccer_tornament:
        print(c)

    print("basketball")
    for c in basketball_tornament:
        print(c)

    print("volleyball")
    for c in volleyball_tornament:
        print(c)

    print("dodgeball")
    for c in dodgeball_tornament:
        print(c)

    for c in first_mach_list:
        print(c)