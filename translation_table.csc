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
    P1.7117.0.0 <-- NENNSTROM                  # Nennsstrom Effektivwert 
    P1.7120.0.0 <-- STROM_MAX                  # MAximalstrom Effektivwert
    P1.7123.0.0 <-- DREH_MAX                   # Maximale Drehzahl in rpm
    P1.7126.0.0 <-- NENN_DREH                  # Nenndrehzahl in rpm
    P1.7129.0.0 <-- INDUKTION                  # windingInductance H
    P1.7132.0.0 <-- WIDERSTAND                 # windingResistance in Ohm
    P1.7135.0.0 <-- DREHM_KONS                 # Torque constant
    P1.7144.0.0 <-- I2T_AUF * 0.001            # I2t in seconds
    P1.7147.0.0 <-- TEMP_SPULE                 # maximum Winding temperature
    P1.71421.0.0 <-- STRANGSPAN                 # voltageRated
    # P1.7152.0.0 <-- ???                      # Temperature sensor type of the motor {dstorage_id: 10, datatype: 'TemperatureSensorType', default: 'TEMPSENSOR_TYPE_NOT_CONNECTED' }" 
    # P1.7155.0.0 <-- ???                      # Temperature sensor characteristic Index0 - Gain. Index1 - Offset Motor (motor data Festo) {dstorage_id: 10, datatype: 'FLOAT32', default: '0' }"
    # P1.7155.0.1 <-- ???                      # Temperature sensor characteristic Index0 - Gain. Index1 - Offset Motor (motor data Festo) {dstorage_id: 10, datatype: 'FLOAT32', default: '0' }"
    P1.7159.0.0 <-- FL_BREMSE                  # isBrakeAvaible -- bool parameter
    P1.7162.0.0 <-- OPEN_TIME_BRAKE * 0.001    # brakeTurnOnDelay 
    P1.7165.0.0 <-- CLOSE_TIME_BRAKE * 0.001   # brakeTurnOffDelay
    P1.71424.0.0 <-- STIL_STROM                 # continousStandstilCurrent

    # P1.7183 --- Berechnung Eduardo...TODO

    P1.71430.0.0 <-- INDUKTION                  # qAxisInductance ... TODO: ANLEGEN IN CACOS
    P1.71431.0.0 <-- INDUKTION                  # dAxisInductance  ... TODO: ANLEGEN IN CACOS
    P1.71432.0.0 <-- MOT_TYP                    # Motor Typ
    