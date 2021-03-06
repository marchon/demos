from units import *

def show(name, measure):
    print "%s : '%s'" % (name, measure.uom)
    
print "The seven base SI units are..."
show("mass", kilogram)
show("length", meter)
show("time", second)
show("electric current", ampere)
show("thermodynamic temperature", kelvin)
show("amount of substance", mole)
show("luminous intensity", candela)
print
print "Some derived units are..."
show("electric charge", coulomb)
show("force", newton)
show("energy", joule)
show("power", watt)
# TODO: Use the formatting function.
print "electric potential " +str(volt)
print "magnetic flux density " +str(tesla)
print "electric field strength " +str(volt/meter)
print "resistance " +str(volt/ampere)
print "conductance " +str(ampere/volt)
print "permittivity " +str((coulomb ** 2)/(newton*(meter ** 2)))
print "permeability " +str(tesla * meter/ampere)
print "angular momentum " +str(joule * second)
print "frequency " +str(1 / second)
print "pressure, stress " +str(newton /(meter ** 2))
print "capacitance " +str(coulomb/volt)
print "magnetic flux " +str(volt * second)
print "inductance " +str(tesla * (meter ** 2)/ampere)
print "dynamic viscosity " +str(newton * second/meter **2)
print "moment of force " +str(newton * meter)
print "surface tension " +str(newton/meter)
print "heat flux density " +str(watt/meter ** 2)
print "heat capacity, entropy " +str(joule/kelvin)
print "thermal conductivity " +str(watt/(meter*kelvin))
print "energy density " +str(joule/(meter**3))
print "molar energy " +str(joule/mole)
print "molar entropy " +str(joule/(mole*kelvin))
