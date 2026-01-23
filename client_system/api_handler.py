from flask import Flask
import collect_system_data

app = Flask("test_endpoint")

@app.route("/api")
def endpoint_test():
    try:
        data = collect_system_data.return_data()
        print(data)
        return data
        #return "test"
        #pass
    except:
        return "Coudn't get data"

if __name__ == "__main__":
    app.run(port=8081)