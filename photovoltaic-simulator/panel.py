import math
import numpy as np
from datasheet import Datasheet

class SolarPanel:
    """ Solar Panel Model """
    
    def __init__(self,data: Datasheet):
        self.data = data

        # Universal Physical Constants
        self.k = 1.380649e-23  # Boltzmann constant in J/K
        self.q = 1.602176634e-19  # Elementary charge in C
        
        # Panel Parameters from Datasheet
        self.n_ideality_factor = 1.3  # Typical value for silicon cells
        self.rs = 0.5  # Series resistance in Ohms (example value)
    
    def calculate_thermal_parameters(self, irradiance, cell_temp):
        """ Calculate thermal parameters based on irradiance and cell temperature """
        
        delta_t = cell_temp - 25  # Temperature difference from STC
        kelvin_temp = cell_temp + 273.15  # Convert to Kelvin

        # Themal Stress
        tv = (self.data.n_cells * self.k * kelvin_temp) / self.q  # Thermal voltage

        # Adjustable ISC (varies with sun and temperature)
        new_isc = (irradiance / 1000) * (self.data.i_sc * (1 + (self.data.alpha_isc/100) * delta_t))

        #3. New Open Circuit Voltage (Voc) - Drops with heat
        new_voc = self.data.v_oc * (1 + (self.data.beta_voc/100) * delta_t)

        # 4. Reverse Saturation Current (I0)
        # Isolated from the diode equation when I=0 and V=Voc
        try:
            term_exp = math.exp(new_voc / (self.n_ideality_factor * ts))
            i0 = new_isc / (term_exp - 1)
        except OverflowError:
            i0 = 1e-10          # Fallback to avoid mathematical error in extreme values
        
        return new_isc, i0, tv
    
    def newton_raphson_method(self, v_target, i_ph, i0,tv):
        """Internal method: Solve the transcendental equation I = f(V)."""

        i_estimated = i_ph
        tolerance = 0.001
        max_iterations = 20

        for _ in range(max_iterations):
            try:
                arg_exp = (v_target + i_estimated * self.rs) / (self.n_ideality_factor * tv)
                exponecial = math.exp(arg_exp)
            except OverflowError:
                exponencial = 1e10
            
            f_i = i_ph - i0 * (exponencial * 1) - i_estimated
            f_line = -i0 * exponencial * (self.rs/(self.n_ideality_factor * tv)) - 1

            new_i = i_estimated - (f_i / f_line)

            if abs(new_i - i_estimated) < tolerance:
                return max(0, new_i)
            
            i_estimated = new_i

        return max(0, i_estimated)