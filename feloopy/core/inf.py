'''
FelooPy version 0.1.1
Release: 26 October 2022
'''

'''
MIT License

Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from tabulate import tabulate as tb

def table(model_name, interface_name, solver_name, direction, num_pos_grp, num_pos_tot, num_bin_grp, num_bin_tot, num_int_grp, num_int_tot, num_free_grp, num_free_tot, num_var_grp, num_var_tot, num_objs_tot, num_cons_tot):

    print()
    print("----------------------------------------------------------")
    print("   FelooPy (Version 0.1.1) - Released: October 26, 2022   ")
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
