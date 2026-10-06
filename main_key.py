from test_key import main_control
from test_key import main_control_2




if __name__ == "__main__":
    soccer_tornament, first_match_s = main_control()
    first_match_list = first_match_s

    basketball_tornament, first_match_b = main_control_2(first_match_list)
    first_match_list = first_match_b

    volleyball_tornament, first_match_v = main_control_2(first_match_list)
    first_match_list = first_match_v

    dodgeball_tornament, first_match_d = main_control_2(first_match_list)
    first_match_list = first_match_d
    


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

    for c in first_match_list:
        print(c)