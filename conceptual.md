### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  1. **Use Cases:**
     - **Python:** General-purpose programming language used for web development, data science, artificial intelligence, automation, etc.
     - **JavaScript:** Primarily a scripting language for web development, used for creating interactive and dynamic web pages.

  2. **Execution Environment:**
     - **Python:** Interpreted language with the option for compilation. Runs on the server side (e.g., Django, Flask) or can be embedded in other applications.
     - **JavaScript:** Interpreted language executed in web browsers for client-side scripting. Also used on the server side with platforms like Node.js.

  3. **Syntax:**
     - **Python:** Emphasizes readability and uses indentation for block structure. Uses dynamic typing.
     - **JavaScript:** C-style syntax with curly braces for block structure. Uses dynamic typing as well.

  <!-- 4. **Typing:**
     - **Python:** Dynamically typed (variable types are determined at runtime).
     - **JavaScript:** Dynamically typed. -->

  4. **Concurrency Model:**
     - **Python:** Generally follows a multi-threaded approach, but the Global Interpreter Lock (GIL) can limit concurrent execution in some cases.
     - **JavaScript:** Uses an event-driven, non-blocking I/O model. Supports asynchronous programming through callbacks and Promises.

---

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. **Using try-except Method:**
   ```python
   my_dict = {"a": 1, "b": 2}
   try:
      value = my_dict[key]
    except KeyError
      print('not found')
   ```

  2. **Using a Conditional Check:**
   ```python
   my_dict = {"a": 1, "b": 2}
   key = "c"
   value = my_dict[key] if key in my_dict else 'not found'
   ```

---

- What is a unit test?
  - A unit test is a small, automated test that checks a specific piece of functionality in isolation to ensure it behaves as expected. It helps validate that individual parts of a program work correctly.
  
---

- What is an integration test?
  - An integration test checks interactions between different components or systems to ensure they work together as intended. It validates the collaboration and integration of various modules or services within a larger application.

---

- What is the role of web application framework, like Flask?
  - A web application framework, like Flask, provides a structured way to build and organize web applications. It facilitates tasks such as routing, handling HTTP requests, managing sessions, and templating, simplifying the development process by offering a set of conventions and tools for building web-based software.

---

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - I will use route parameters (`/foods/pretzel`) when the information is essential to the resource being accessed like identifying a specific food item and query parameters (`foods?type=pretzel`) when the information is optional, and it doesn't fundamentally identify the resource but provides additional details or filters like filtering foods by type.

---

- How do you collect data from a URL placeholder parameter using Flask?
  - In Flask, we can collect data from a URL placeholder parameter using the `<>` syntax in the route definition. For example:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/foods/<food_type>')
def get_food(food_type):
    return f"You requested information about {food_type}"

if __name__ == '__main__':
    app.run(debug=True)
```
Here, the `food_type` parameter in the route (`/foods/<food_type>`) captures the value from the URL, and we can use it as a parameter in the corresponding view function (`get_food`).

---

- How do you collect data from the query string using Flask?
  - In Flask, we can collect data from the query string using the `request` object. For example:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/foods')
def get_food():
    food_type = request.args.get('type')
    return f"You requested information about {food_type}"

if __name__ == '__main__':
    app.run(debug=True)
```
`request.args.get('type')` retrieves the value of the 'type' parameter from the query string.

---

- How do you collect data from the body of the request using Flask?
  - In Flask, we can collect data from the body of the request using the `request` object and its `json` attribute for JSON data or `form` attribute for form data. For example:

For JSON data:
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    return f"Received JSON data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
```

For form data:
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.form['key']
    return f"Received form data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
```
`request.json` is used for JSON data, and `request.form['key']` is used for form data.

---

- What is a cookie and what kinds of things are they commonly used for?
  - A cookie is a small piece of data stored on a user's device by a web browser. 
  It is commonly used to store user preferences, session information, and tracking data.

---

- What is the session object in Flask?
  - In Flask, the session object is a dictionary-like object that allows to store data that persists across requests for a specific user.

---

- What does Flask's `jsonify()` do?
  - Flask's `jsonify()` function converts a Python dictionary or other JSON-serializable object into a JSON response, setting the appropriate content type. It simplifies the process of returning JSON responses from Flask routes.
