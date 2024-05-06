from mytypes import Teacher, Title

T_UNOCCUPIED = Teacher(
    main_name="UNOCCUPIED",
    main_surname="UNOCCUPIED",
    names={},
    surnames={}
)
"Unbesetzt"

T_Rudnicki_Mateusz = Teacher(
    main_name="Mateusz",
    main_surname="Rudnicki",
    names={"Matthäus": {1861, 1862, 1863}},
    surnames={"Rudnicki": {1861, 1862, 1863}}
)

T_Hudzicki_Stanislaw = Teacher(
    main_name="Stanisław",
    main_surname="Hudzicki",
    names={"Stanislaus": {1861, 1862, 1863}},
    surnames={"Hudzicki": {1861, 1862, 1863}}
)

T_Kapturkiewicz_Michal = Teacher(
    main_name="Michał",
    main_surname="Kapturkiewicz",
    names={"Michael": {1861, 1862, 1863}},
    surnames={"Kapturkiewicz": {1861, 1862, 1863}}
)

T_Bienkowski_Jozef = Teacher(
    main_name="Józef",
    main_surname="Bieńkowski",
    names={"Joseph": {1861, 1862, 1863}},
    surnames={"Bieńkowski": {186, 1862, 1863}}
)

T_Olexy_Jozef = Teacher(
    main_name="Józef",
    main_surname="Olexy",
    names={"Joseph": {1861, 1862, 1863}},
    surnames={"Olexy": {1861, 1862, 1863}}
)

T_Andrusikiewicz_Wincent = Teacher(
    main_name="Wincent",
    main_surname="Andrusikiewicz",
    names={"Vincenz": {1861, 1862, 1863}},
    surnames={"Andrusikiewicz": {1861, 1862, 1863}}
)

T_Dlugopolski_Marek = Teacher(
    main_name="Marek",
    main_surname="Długopolski",
    names={"Markus": {1861, 1862}},
    surnames={"Długopolski": {1861, 1862}}
)

T_Barbacki_Jan = Teacher(
    main_name="Jan",
    main_surname="Barbacki",
    names={"Johann": {1861, 1862}},
    surnames={"Barbacki": {1861, 1862}}
)

T_Zborowski_Kacper = Teacher(
    main_name="Kacper",
    main_surname="Zborowski",
    names={"Caspar": {1861, 1862}},
    surnames={"Zborowski": {1861, 1862}}
)

T_Kwasniak_X_proboszcz = Teacher(
    main_name=None,
    main_surname="Kwaśniak",
    names={"": {1861}},
    surnames={"Kwaśniak": {1861}},
    titles={1861: Title.wikariusz},
)

T_Budzyk_Jan = Teacher(
    main_name="Jan",
    main_surname="Budzyk",
    names={"Johann": {1862}},
    surnames={"Budzyk": {1862}},
    titles={1862: Title.wikariusz},
)
