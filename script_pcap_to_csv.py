import os, glob
import pandas as pd

path = '/home/pedro/Documentos/ufpe/mestrado/automotives/autoeth-intrusion-dataset/single/'

for filename in glob.glob(os.path.join(path, '*.csv')):
	df = pd.read_csv(filename,usecols=[0,1,2], names=["pk:number", "pk:type", "data"])  
	#df = df[df['pk:type'] == 'eth:ethertype:vlan:ethertype:ieee1722:iec61883']
	df = df[df['pk:type'] ==  'eth:ethertype:vlan:ethertype:ieee1722:iec61883:mp2t:mp2t']

	df.data = df.data.apply(lambda x: bytearray.fromhex(str(x))) #Inteiro
	aux = filename.split('/')[-1].split('.')[0]
	df.to_csv('/home/pedro/Documentos/ufpe/mestrado/automotives/autoeth-intrusion-dataset/' +aux + '_converted.csv')
