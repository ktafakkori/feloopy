from feloopy import *

# Credit: https://github.com/ErayCakici/Scheduling-DOCPLEX-Examples_CP

m = target_model('constraint', 'flexible_resource_constrained_scheduling', 'cplex_cp', key=0)

J = range(5) #Set of jobs
O = range(20) #Set of all operations
C = range(5) #Set of operation classes
R = range(3) #Set of resource types required

operations_for_each_job = m.uniformlist(len(C)-3, len(C), C, [J])
class_of_operation = m.uniformint(0,len(C)-1,[O])
job_due_date  = m.uniformint(2000, 3000, [J])
capacity_of_resource = m.uniformint(20,32, [R])
operation_requires_resource = m.uniformint(0,4, [O,R])
batch_size_of_operation = m.uniformint(2,5,[O])
duration_of_each_operation_class = m.uniformint(10,40,[C])

operation = m.cevar('operation', [o for o,c in sets(O,C) if class_of_operation[o]==c], {o: [duration_of_each_operation_class[c], None, None] for o,c in sets(O,C) if class_of_operation[o]==c}, optional=True)
job_operation = m.cevar('job_operation', [(j,o) for j,o in sets(J,O)], {(j,o): [duration_of_each_operation_class[c], None, None] for j,o,c in sets(J,O,C) if class_of_operation[o]==c}, optional=True)
tardiness_indicator = m.bvar('tardiness', [J])

m.obj(sum(tardiness_indicator[j] for j in J))

for r in R:
    m.con(sum([m.control_resource(operation[o], operation_requires_resource[o,r], function='pulse') for o in O if operation_requires_resource[o,r]>0])<=capacity_of_resource[r])

for o in O:
    m.con(sum(m.presence_of(job_operation[j,o]) for j in J)<=batch_size_of_operation[o])

for j,o,c in sets(J,O,C):
    if class_of_operation[o]==c:
        m.con(m.synchronize(job_operation[j,o], [operation[(o1)] for o1,c1 in sets(O,C) if o1 == o]))
        m.con(m.presence_of(job_operation[j,o]) <= m.presence_of(operation[o]))

for j,o,c in sets(J,O,C):
    if class_of_operation[o]==c:
        m.scon_soft_indicator_geq(tardiness_indicator[j], m.end_of(job_operation[j,o]), job_due_date[j], big_m=100000)

for j,c in sets(J,C):
    if c in operations_for_each_job[j]:
        m.con(sum(m.presence_of(job_operation[j,o]) for o in O if class_of_operation[o]== c)  == 1 - tardiness_indicator[j])
    if c not in operations_for_each_job[j]:
        m.con(sum(m.presence_of(job_operation[j, o]) for o in O if class_of_operation[o]== c) == 0)

for j in J:
    m.con(m.forbid_overlap([job_operation[j, o] for o in O]))

for j,o1,c1,o2,c2 in sets(J, O,C,O,C):
    if class_of_operation[o1]==c1 and class_of_operation[o2]==c2 and o1 <o2: 
        m.con(m.prec_end_before_start(job_operation[j, o1], job_operation[j, o2]))

m.solve(['min'], 'cplex')
m.report()