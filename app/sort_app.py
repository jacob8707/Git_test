from SRC.sort_list  import sort_value
Country_list=list(('Canada', 'Japan', 'Germany', 'Switzerland', 'Australia', 'USA', 'France', 'UK'))
per_GDP_list=list((46327, 40113, 46468, 85300, 55057, 65280, 40380,42540))
print(sort_value(dict(zip(Country_list,per_GDP_list))))

