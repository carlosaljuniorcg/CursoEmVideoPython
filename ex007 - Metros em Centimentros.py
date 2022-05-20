#COnverter metros em centimetros e milimetros
medida = float(input('Uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))