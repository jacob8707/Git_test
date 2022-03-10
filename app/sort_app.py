from SRC.sort_list  import sort_value
Country_list=list(('Canada', 'Japan', 'Germany', 'Switzerland', 'Australia', 'United states of America', 'France', 'Britain'))
per_GDP_list=list((46327, 40113, 46468, 85300, 55057, 65280, 40380,42540))
print('the sorted GDP is', sort_value(dict(zip(Country_list,per_GDP_list))))

