project_teams = [["Ava","Samantha","James"],["lucas","zed"],["Edgar","Gabriel"]]
for team in project_teams:
    for member in team:
        print(member)
print( )
sales_data = [[12,17,22],[2,10,3],[5,12,13]]
scoops_sold = 0
for item in sales_data :
    print(item)
    for element in item:
        scoops_sold += element
    print(scoops_sold)