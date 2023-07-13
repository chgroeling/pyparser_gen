# ====================================
# Translation table for cacos db
# ====================================

# ------------------------------------
# First look into control table
# ------------------------------------
USE_TABLE control

#   P0.28121.0.0 <-- U_NETZ_MIN           # mainsVoltageLimitLowMin
#   P0.28131.0.0 <-- U_NETZ_MIN           # mainsVoltageLimitHighMin

#   P0.28120.0.0 <-- U_NETZ_MAX           # mainsVoltageLimitLowMax
#   P0.28130.0.0 <-- U_NETZ_MAX           # mainsVoltageLimitHighMax

    P0.2835.0.0  <-- R_MIN_CHOPPER        # externalBrakeResistorRMin
    P0.2836.0.0  <-- R_MAX_CHOPPER        # externalBrakeResistorRMax

    P0.2843.0.0  <-- ZEITLIMIT            # sfIitTimeFs
    P0.2844.0.0  <-- ZEITLIMIT_LOW_FREQ   # sfIitTimeFsMin

#   P0.2838.0.0  <-- PULSE_ENERGY_CHOPPER # externalBrakeResistorWRatedMax

# TODO: 
# - ÜBERTRAGEN IN USER CONFIG DATEN
# - Konzept Werkeinstellungen zurückbauen
# - Rechenvorschrift ... addition
# - BOOL Parameter support
# - Berechnungsvorschrift Eduardo

USE_TABLE motdat
    P1.718.0.0  <-- POL_PAAR                   # Polpaarzahl
    
    P1.7111.0.0 <-- TRAEG_ROTO * 0.0001        # + TRAEG_BREM * 0.0000001  
       