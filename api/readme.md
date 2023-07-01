# Back-end

We are using Flask for back-end.

## Getting started

1. Set up a Python virtual environment. See [this guide](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/);
2. Install the dependencies: `pip install -r requirements.txt`;
3. Create a `.env` file in the `app` directory with the following content:

```
MONGO_URI=<your-mongo-uri>
```

…where `<your-mongo-uri>` is the URI of your MongoDB database. To obtain the
URI, log in to MongoDB Atlas, and click on _Connect_ on the _JobFlow_ cluster.
Choose _Drivers_, and then select _Python_ as the driver. Copy the URI;

4. Run the app: `python run.py`;
5. The app will be available at `http://localhost:5000`. Try going to
   <http://localhost:5000/users>, for example. You should see a JSON list of all
   users in the database.
