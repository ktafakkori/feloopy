'''
+---------------------------------------------------------+
│  Project: FelooPy (0.2.8)                               │
│  Modified: Wednesday, 27th September 2023 11:37:09 pm   │
│  Modified By: Keivan Tafakkori                          │
│  Project: https://github.com/ktafakkori/feloopy         │
│  Contact: https://www.linkedin.com/in/keivan-tafakkori/ │
│  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         │
+---------------------------------------------------------+
'''

import numpy as np

def format_string(input):
    if input>10000 or input<-10000:
        return "{:.2e}".format(input)
    else:
        return "{:.2f}".format(input)
    
def center(input, box_width=80):
    print("│" + " " + str(input).center(box_width-2) + " " + "│")

def tline(box_width=80):
    print("╭" + "─"*box_width + "╮")

def tline_text(input, box_width=80):
    print("╭─ " + input +" " + "─"*(box_width-len(input)-3) + "╮")
    

def bline_text(input, box_width=80):
    print("╰" + input + " " + "─"*(box_width-len(input)-3) + "╯")
        
def empty_line(box_width=80):
    print("│" + " "*box_width + "│")

def bline(box_width=80):
    print("╰" + "─"*box_width + "╯")

def hline(box_width=80):
    print("├" + "─"*box_width + "┤")

def whline(box_width=80):
    print("+" + "."*box_width + "┤")

def hrule(box_width=80):
    print("├" + "="*box_width + "┤")

def vspace():
    print()

def two_column(input1,input2, box_width=80):
    padding = box_width - len(input1) - len(input2) - 2
    print("│ " + str(input1) + " "*padding + str(input2) + " │")

def three_column(input1, input2, input3, box_width=80, underline=False):
    total_padding = box_width - len(input1) - len(input2) - len(input3) - 6
    padding1 = total_padding // 2
    padding2 = total_padding - padding1
    
    if underline:
        input1 = f"\033[4m{input1}\033[0m"
        input2 = f"\033[4m{input2}\033[0m"
        input3 = f"\033[4m{input3}\033[0m"
    
    print("│ " + str(input1) + " " * padding1 + "  " + str(input2) + " " * padding2 + "  " + str(input3) + " │")

def list_three_column(input_list, box_width=80, underline=False):
    column1_width = max(len(str(x[0])) for x in input_list) + 2
    column2_width = max(len(str(x[1])) for x in input_list) + 2
    column3_width = max(len(str(x[2])) for x in input_list) + 2

    space_left = box_width - column1_width - column2_width - column3_width - 2
    padding1 = space_left // 2
    padding2 = space_left - padding1

    for row in input_list:
        if row[2]!=0:
            input1, input2, input3 = row
            if underline:
                input1 = f"\033[4m{input1}\033[0m"
                input2 = f"\033[4m{input2}\033[0m"
                input3 = f"\033[4m{input3}\033[0m"
            print(f"│ {input1:<{column1_width}}{padding1 * ' '}{input2:<{column2_width}}{padding2 * ' '}{input3:<{column3_width}} │")

def boxed(text, box_width=80):
    
    import textwrap
    lines = textwrap.wrap(text, width=box_width - 4)
    for line in lines:
        left_align(line,box_width)


def left_align(input, box_width=80):
    print("│" + " " + input.ljust(box_width-2) + " " + "│")

def right_align(input, box_width=80):
    print("│" + " " + input.rjust(box_width-2) + " " + "│")

def feature_print(type, input):
    if input[0]>0:
        three_column(type, f"{input[0]}", f"{input[1]}")

def objective_print(type, input):
    if input[0]>0:
        three_column(type, "-", f"{input[1]}")

def constraint_print(type, input):
    if input[0]>0:
        three_column(type, f"{input[0]}", f"{input[1]}")

def status_row_print(ObjectivesDirections, status, box_width=80):
    if len(ObjectivesDirections) != 1 and ObjectivesDirections[0] !="nan":
        row = "│ " + "Status: " + " " * (len(status[0]) - len("Status: ")) + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str(status[0])) - 3)
        for j in range(len(ObjectivesDirections)):
            obj_row = ObjectivesDirections[j]
            row += " " * (10 - len(obj_row)) + obj_row
        print(row + " │")
        
    else:
        row = "│ " + "Status: " + " "*(len(str(status)) - len("Status: ")) + " " * (box_width-10*len(ObjectivesDirections) + 1 - len(str(status)) - 3)
        for j in range(len(ObjectivesDirections)):
            obj_row = ObjectivesDirections[j]
            row += " " * (10 - len(obj_row)) + obj_row

        if len(row + " │")==box_width+2:
            print(row + " │")

        elif len(row + " │") <box_width+2:
            row = "│ " + "Status: " + " "*(len(str(status)) - len("Status: ")) + " " * (box_width-10*len(ObjectivesDirections) + 1 - len(str(status)) - 3)
            for j in range(len(ObjectivesDirections)):
                obj_row = ObjectivesDirections[j]
                row += " " * (10 - len(obj_row)) + obj_row
            print(row + " │")
            
        else:
            row = "│ " + "Status: " + " "*(len(str(status)) - len("Status: ")) + " " * (box_width-10*len(ObjectivesDirections) - len(str(status)) - 3)
            for j in range(len(ObjectivesDirections)):
                obj_row = ObjectivesDirections[j]
                row += " " * (10 - len(obj_row)) + obj_row
            print(row + " │")


def solution_print(ObjectivesDirections, status, get_obj, get_payoff=None, box_width=80):
    if len(ObjectivesDirections)!=1:
        if status[0] != "infeasible (constrained)":
            for i in range(len(status)):
                row = "│ " + str(status[i]) + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str(status[i])) - 3)
                obj_row = get_obj[i]
                for j in range(len(obj_row)):
                    num_str = format_string(obj_row[j])
                    row += " " * (10 - len(num_str)) + num_str
                print(row + " │")

            for j in range(len(ObjectivesDirections)):
                row = "│ " + str(f"payoff {j}") + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str(f"payoff {j}")) - 3)
                for k in range(len(ObjectivesDirections)):
                    num_str = format_string(get_payoff[j, k])
                    row += " " * (10 - len(num_str)) + num_str
                print(row + " │")

            row = "│ " + str("max") + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str("max")) - 3)
            for j in range(len(ObjectivesDirections)):
                num_str = format_string(np.max(get_obj[:,j]))
                row += " " * (10 - len(num_str)) + num_str
            print(row + " │")

            row = "│ " + str("ave") + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str("ave")) - 3)
            for j in range(len(ObjectivesDirections)):
                num_str = format_string(np.average(get_obj[:,j]))
                row += " " * (10 - len(num_str)) + num_str
            print(row + " │")

            row = "│ " + str("std") + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str("std")) - 3)
            for j in range(len(ObjectivesDirections)):
                num_str = format_string(np.std(get_obj[:,j]))
                row += " " * (10 - len(num_str)) + num_str
            print(row + " │")

            row = "│ " + str("min") + " " * (box_width - 10 * len(ObjectivesDirections) + 1 - len(str("min")) - 3)
            for j in range(len(ObjectivesDirections)):
                num_str = format_string(np.min(get_obj[:,j]))
                row += " " * (10 - len(num_str)) + num_str
            print(row + " │")

    else:
        row = "│ " + str(status) + " " * (box_width-9*len(ObjectivesDirections) +1 - len(str(status)) - 3)
        obj_row = get_obj
        num_str = format_string(obj_row)
        row += " " * (9 - len(num_str)) + num_str
        print(row + " │")

def metrics_print(ObjectivesDirections, show_all_metrics, get_obj, calculated_indicators, start=0, end=0, length=None, box_width = 80):
    hour, min, sec =  calculate_time_difference(start, end, length)

    try:
        if len(ObjectivesDirections) != 1:
            if show_all_metrics and len(get_obj) != 0:
                for key, label in [("gd", "GD (min)"), ("gdp", "GDP (min)"), ("igd", "IGD (min)"), ("igdp", "IGDP (min)"), ("ms", "MS (max)"), ("sp", "SP (min)"), ("hv", "HV (max)")]:
                    value = calculated_indicators.get(key)
                    if value is not None:
                        two_column(label, format_string(value))
    except Exception as e:
        center(f"No special metric is calculatable.")
        
    if length== None:
        two_column('CPT (microseconds)', format_string((end - start) * 10 ** 6))
    else:
        two_column('CPT (microseconds)', format_string((length) * 10 ** 6))

    two_column('CPT (hour:min:sec)', "%02d:%02d:%02d" % (hour, min, sec))        

def calculate_time_difference(start=0, end=0, length=None):
    if length == None:
        hour = round((end - start), 3) % (24 * 3600) // 3600
        minute = round((end - start), 3) % (24 * 3600) % 3600 // 60
        second = round((end - start), 3) % (24 * 3600) % 3600 % 60
    else:

        hour = round((length), 3) % (24 * 3600) // 3600
        minute = round((length), 3) % (24 * 3600) % 3600 // 60
        second = round((length), 3) % (24 * 3600) % 3600 % 60

    return hour, minute, second