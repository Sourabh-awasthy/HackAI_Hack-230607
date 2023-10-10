from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
class Weather_data:
    def collect_weather_preferences():
        if request.method == 'POST':
            country = request.form['country']
            state = request.form['state']
            city = request.form['city']
            min_temperature = request.form['minTemperature']
            max_temperature = request.form['maxTemperature']
            
            # Now you can process the collected data as needed.
            # For example, you can print it to the console.
            print(f'Country: {country}')
            print(f'State: {state}')
            print(f'City: {city}')
            print(f'Min Temperature: {min_temperature}')
            print(f'Max Temperature: {max_temperature}')
            
            # You can also store the data in a database or perform other actions here.
        
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, render_template, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# @app.route('/', methods=['GET', 'POST'])
# def weather_preferences():
#     if request.method == 'POST':
#         # Collect form data and store it in the session
#         data = {
#             'country': request.form['country'],
#             'state': request.form['state'],
#             'city': request.form['city'],
#             'min_temperature': request.form['minTemperature'],
#             'max_temperature': request.form['maxTemperature']
#         }

    
#     if data:
#         # Use the form data as needed
#         print(f'Country: {data["country"]}')
#         print(f'State: {data["state"]}')
#         print(f'City: {data["city"]}')
#         print(f'Min Temperature: {data["min_temperature"]}')
#         print(f'Max Temperature: {data["max_temperature"]}')
#     else:
#         print('No form data available.')

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
