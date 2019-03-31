def mp_arrange(input_list):
	m=len(input_list)-1
	while m>=1:
		i=0
		while i<m:
			if input_list[i]>input_list[i+1]:
				bf=input_list[i]
				input_list[i]=input_list[i+1]
				input_list[i+1]=bf
			i+=1
		m-=1
	return(input_list)