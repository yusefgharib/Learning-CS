a, b = input(), input()
p = {('1/2', '-1/3'): 'Strange Quark', ('1/2', '2/3'): 'Charm Quark',
     ('1/2', '-1'): 'Electron Lepton', ('1/2', '0'): 'Neutrino Lepton', 
     ('1', '0'): 'Photon Boson'}

print(p[(a, b)])
