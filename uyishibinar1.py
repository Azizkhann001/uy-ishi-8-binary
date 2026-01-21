users = [
    'Abdulla Abdullaev', 
    'Samandar Asadov', 
    'Shaxnoza Jurayeva', 
    'Ikrom Karimov',
    'Gulnora Xalilova',
    'Ziyoda Yuldashova'
    ]
men=[]
women=[]

for i in users:
    familiya=i.split()[-1].lower()
    if familiya.endswith(("ev","ov")):
        men.append(i)
    elif familiya.endswith("va"):
        women.append(i)
print("men=",men)
print("women=",women)