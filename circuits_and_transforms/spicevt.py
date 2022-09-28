from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import numpy 
import matplotlib.pyplot as plt
import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Probe.Plot import plot


logger=Logging.setup_logging()
circuit=Circuit("Circuit1")
circuit.V('V1','v1in','Cout',1@u_V)
circuit.V('V2','v2in','Cout',2@u_V)
circuit.R(1,'v1in','Cin',1@u_Ohm)
circuit.R(2,'v2in','Cin',2@u_Ohm)
circuit.C(1,'Cin','Cout',1@u_uF)
print(circuit)
simulator=circuit.simulator(temperature=25,nominal_temperature=25)
simulator.initial_condition(Cin=0@_V,Cout=0@_V)
analysis=simulator.transient(step_time=0.1,end_time=5)
fig=plt.figure()
x=np.array(analysis["Cin"])-np.array(analysis["Cout"])
plt.plot(np.array(analysis.time),x)
plt.grid()
fig.savefig("spice.png",dpi=300)


