# this function was used to sort the dictionary based on its values.
def sort_value(diction):
    lst=list(diction.items())
    def sort_criteria(m):
        return m[1]
    lst.sort(key=sort_criteria, reverse =True)
    dict_new=dict(lst)
    return dict_new

if __name__=="__main__":
    name=['Hang', 'Dakai', 'Beau', 'Meichouchou']
    age=[35,34,0,10]
    sort_age=sort_value(dict(zip(name,age)))
    print (sort_age)

