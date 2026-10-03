from control   import  main_control
from control   import  main_control_2
from control   import  translate_list
from excell     import  makefile




def mian_function(soccer_mian, soccer_ex, basketball_main, basketball_ex, volleyball_main, volleyball_ex, dodgeball_main, dodgeball_ex):
    soccer_list, first_mach_s, class_num_s      = main_control(soccer_mian, soccer_ex)
    first_mach_list                             = first_mach_s
    soccer_tornament                            = translate_list(soccer_list)

    print("soccer")
    for c in soccer_tornament:
        print(c)

    basketball_list, first_mach_b, class_num_b  = main_control_2(first_mach_list, basketball_main, basketball_ex)
    first_mach_list                             = first_mach_b
    basketball_tornament                        = translate_list(basketball_list)

    print("basketball")
    for c in basketball_tornament:
        print(c)

    volleyball_list, first_mach_v, class_num_v  = main_control_2(first_mach_list, volleyball_main, volleyball_ex)
    first_mach_list                             = first_mach_v
    volleyball_tornament                        = translate_list(volleyball_list)

    print("volleyball")
    for c in volleyball_tornament:
        print(c)

    dodgeball_list, first_mach_d, class_num_d   = main_control_2(first_mach_list, dodgeball_main, dodgeball_ex)
    first_mach_list                             = first_mach_d
    print("dodgeball")
    for c in dodgeball_list:
        print(c)
    dodgeball_tornament                         = translate_list(dodgeball_list)

    print("dodgeball")
    for c in dodgeball_tornament:
        print(c)
    



    for c in first_mach_list:
        print(c)

    makefile(soccer_tornament,      class_num_s,
            basketball_tornament,   class_num_b,
            volleyball_tornament,   class_num_v,
            dodgeball_tornament,    class_num_d
            )