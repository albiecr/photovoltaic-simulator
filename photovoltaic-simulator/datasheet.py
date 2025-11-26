from dataclasses import dataclass

@dataclass
class Datasheet:
    """ STC Datasheet for a Photovoltaic Module """
    model: str
    p_max: float
    v_oc: float
    i_sc: float
    alpha_isc: float
    beta_voc: float
    n_cells: int