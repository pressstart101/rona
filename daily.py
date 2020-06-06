from flask import Flask, render_template
from deaths import *
from script import *

app = Flask(__name__)
country = Deaths.country()
@app.route('/')
def home():
    us = Deaths.country()
    return render_template("home.html", us = us)

if __name__ == "__main__":
    app.run(debug=True)

country = Deaths.country()
state = Deaths.state()
city = Deaths.city()


# create_table()
# insert(country, state, city)

# print(view_one("country"))
# print(view_all())

arr = view_all()
# print(arr[0][1])
# print(type(arr[0]))
for a in arr:
    us = a[1]
    print("US: ", us)




# print('US: ', Deaths.country())
# print('California: ', Deaths.state())
# print('Los Angeles: ', Deaths.city())
