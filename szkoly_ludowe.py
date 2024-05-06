from mytypes import *
from teachers import *
from places import *

S_Dobra = \
    School(place=P_Dobra,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Rudnicki_Mateusz),
                   ],
                   n_children=135,
               ),
               1862: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Rudnicki_Mateusz),
                   ],
                   n_children=128,
               ),
               1863: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Rudnicki_Mateusz),
                       TeacherEntry(teacher=T_UNOCCUPIED, func=FunctionEntry(functions={Function.pomoc})),
                   ],
                   n_children=122,
               ),
           },
           )

S_Limanowa = \
    School(place=P_Limanowa,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Hudzicki_Stanislaw),
                       TeacherEntry(teacher=T_Kapturkiewicz_Michal, func=FunctionEntry(functions={Function.pomoc})),
                   ],
                   n_children=247,
               ),
               1862: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Hudzicki_Stanislaw),
                       TeacherEntry(teacher=T_Kapturkiewicz_Michal, func=FunctionEntry(functions={Function.pomoc})),
                   ],
                   n_children=214,
               ),
               1863: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Hudzicki_Stanislaw),
                       TeacherEntry(teacher=T_Kapturkiewicz_Michal, func=FunctionEntry(functions={Function.pomoc})),
                   ],
                   n_children=150,
               ),
           },
           )

S_Mszana_Dolna = \
    School(place=P_Mszana_Dolna,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Bienkowski_Jozef),
                   ],
                   n_children=97,
               ),
               1862: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Bienkowski_Jozef),
                   ],
                   n_children=86,
               ),
               1863: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Bienkowski_Jozef),
                   ],
                   n_children=104,
               ),
           },
           )

S_Niedzwiedz = \
    School(place=P_Niedzwiedz,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Olexy_Jozef),
                   ],
                   n_children=150,
               ),
               1862: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Olexy_Jozef),
                   ],
                   n_children=150,
               ),
               1863: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Olexy_Jozef),
                   ],
                   n_children=164,
               ),
           },
           )

S_Tymbark = \
    School(place=P_Tymbark,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Andrusikiewicz_Wincent),
                   ],
                   n_children=109,
               ),
               1862: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Andrusikiewicz_Wincent),
                   ],
                   n_children=126,
               ),
               1863: SchoolYear(
                   type=SchoolType.trivial,
                   teachers=[
                       TeacherEntry(teacher=T_Andrusikiewicz_Wincent),
                   ],
                   n_children=115,
               ),
           },
           )

S_Olszowka = \
    School(place=P_Olszowka,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Dlugopolski_Marek),
                   ],
                   n_children=71,
               ),
               1862: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Dlugopolski_Marek),
                   ],
                   n_children=74,
               ),
           },
           )

S_Slopnice = \
    School(place=P_Slopnice,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Barbacki_Jan),
                   ],
                   n_children=113,
               ),
               1862: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Barbacki_Jan),
                   ],
                   n_children=114,
               ),
           },
           )

S_Kasina_Wielka = \
    School(place=P_Kasina_Wielka,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Zborowski_Kacper),
                   ],
                   n_children=37,
               ),
               1862: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Zborowski_Kacper),
                   ],
                   n_children=48,
               ),
           },
           )

S_Lososina_Gorna = \
    School(place=P_Lososina_Gorna,
           school_years={
               1861: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Kwasniak_X_proboszcz),
                   ],
                   n_children=111,
               ),
               1862: SchoolYear(
                   type=SchoolType.parish,
                   teachers=[
                       TeacherEntry(teacher=T_Budzyk_Jan),
                   ],
                   n_children=95,
               ),
           },
           )

S_Mstow = \
    School(place=P_Mstow,
           school_years={
               1862: SchoolYear(
                   type=SchoolType.filial,
                   teachers=[],
               ),
           },
           )

schools = {
    S_Dobra, S_Limanowa, S_Mszana_Dolna, S_Niedzwiedz,
    S_Tymbark, S_Olszowka, S_Slopnice, S_Kasina_Wielka,
    S_Lososina_Gorna, S_Mstow}
