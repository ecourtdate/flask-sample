# flask-sample
Sample Python + Flask CRUD application

Purpose
-------

This is a simple Flask app that demonstrates how to use the eCourtDate JSON API.

Installation
------------

To install the sample app you need to have Python 3+ installed. You can
then install the project dependencies by running:

    $ pip install -r requirements.txt

This will install all the project dependencies.

Running the App
---------------

This app requires an eCourtDate API client to run. Create a client via the Console API page: 
https://console.ecourtdate.com/apis

Next, you need to rename the ``env.txt`` file to ``.env`` file in your project root. This holds the app parameters and API credentials
needed to run. Then, replace the sample values for ``CLIENT_ID``, ``CLIENT_SECRET``, ``AGENCY``, and ``REGION`` with your own.

Next, run the web server.

    flask run

Finally, go visit http://localhost:5000!