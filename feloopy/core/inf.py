'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


from tabulate import tabulate as tb

def table(model_name, interface_name, solver_name, direction, num_pos_grp, num_pos_tot, num_bin_grp, num_bin_tot, num_int_grp, num_int_tot, num_free_grp, num_free_tot, num_var_grp, num_var_tot, num_objs_tot, num_cons_tot):

    print()
    print("----------------------------------------------------------")
    print("   FelooPy (Version 0.1.11) - Released: November 21, 2022 ")
    print("----------------------------------------------------------")
    print()

    print()
    print("PROBLEM FEATURES \n --------")
    print(
        tb(
            {
                "info": ["model", "interface", "solver", "direction"],
                "detail": [model_name, interface_name, solver_name, direction],
                "variable": ["positive", "binary", "integer", "free", "tot"],
                "count (cat,tot)": [str((num_pos_grp, num_pos_tot)), str((num_bin_grp, num_bin_tot)), str((num_int_grp, num_int_tot)), str((num_free_grp, num_free_tot)), str((num_var_grp, num_var_tot))],
                "other": ["objective", "constraint"],
                "count (tot)": [num_objs_tot, num_cons_tot]
            },
            headers="keys", tablefmt="github"
        )
    )
