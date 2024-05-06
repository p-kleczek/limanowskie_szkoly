from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict, Tuple, Optional, Set

SzR = int  # rocznik szematyzmu


# cytowanie
class Source:
    pass


@dataclass
class Place:
    """Miejscowość"""
    name: str
    pass


class Title(Enum):
    ks = auto()  # ks.
    wikariusz = auto()  # wikariusz


@dataclass
class Teacher:
    names: Dict[str, Set[SzR]]
    main_name: Optional[str]
    surnames: Dict[str, Set[SzR]]
    main_surname: str
    titles: Set[SzR: Title] = field(default_factory=set)


class Function(Enum):
    prow = auto()  # prow.
    zast = auto()  # zast.
    mlod = auto()  # młod.
    nadet = auto()  # nadet.
    kier = auto()  # kier.
    tymcz = auto()  # tymcz.
    star = auto()  # star.
    eksp = auto()  # eksp., exp.
    pomoc = auto()  # pomoc / Lehrgehilfe
    musterl = auto()  # Musterlehrer


@dataclass
class FunctionEntry:
    functions: Set[Function] = field(default_factory=set)
    aux: str = None
    "Dodatkowe informacje"
    exp_place: Optional[Place] = None
    "Miejsce ekspozytury"


@dataclass
class TeacherEntry:
    teacher: Teacher
    func: Optional[FunctionEntry] = None


UNOCCUPIED = [(None, None)]

LOCAL_CLERGY = Teacher()
"Duchowieństwo miejscowe"


class SchoolType(Enum):
    trivial = auto()
    "trywialna"
    class_1 = auto()
    "1-klasowa"
    class_2 = auto()
    "2-klasowa"
    class_3 = auto()
    "3-klasowa"
    class_4 = auto()
    "4-klasowa"
    class_5 = auto()
    "5-klasowa"
    unorganized = auto()
    "niezorganizowana"
    parish = auto()
    "parafialna"
    filial = auto()
    "filialna"
    private = auto()
    "prywatna"


UNKNOWN = None


@dataclass
class SchoolYear:
    type: SchoolType
    teachers: List[TeacherEntry]
    catechist: Optional[Teacher] = None
    n_children: Optional[int] = UNKNOWN


@dataclass
class School:
    place: Place
    school_years: Dict[SzR: SchoolYear]
