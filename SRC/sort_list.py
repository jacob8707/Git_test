# this function was used to sort the dictionary based on its values.
def sort_value(diction):
    lst=diction.items()
    def sort_criteria(m):
        return m[1]
    lst_new=sorted(lst,key=sort_criteria)
    dict_new=dict(lst_new)
    return dict_new

if __name__=="__main__":
    name=['Hang', 'Dakai', 'Beau', 'Meichou']
    age=[35,34,0,10]
    sort_age=sort_value(dict(zip(name,age)))
    print (sort_age)

