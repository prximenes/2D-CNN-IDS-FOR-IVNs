for file in /autoeth-intrusion-dataset/pcap_files/csvs/*
do 
	tshark -r "$file" -T fields -e frame.number -e frame.protocols -e iec61883.videodata -E separator=, -E occurrence=f > "/home/pedro/Documentos/ufpe/mestrado/automotives/autoeth-intrusion-dataset/pcap_files/csvs/${file##*/}.csv"
done



