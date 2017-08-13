# WarpSpeed Python Flask Sample Application

[Flask](http://flask.pocoo.org/) is a Python Web microframework. [WarpSpeed](https://warpspeed.io) makes it incredibly easy to deploy Flask and other Python based projects. This guide will help you get up and running with Flask and WarpSpeed.

Each of the WarpSpeed sample projects is a simple "To Do" list. All of the projects, regardless of language or framework, have the same basic functionality. If you are new to a particular language or framework, just compare the code to a language example that you are familiar with and you will be able to catch on quickly. A preview of the deployed project is show below:

![Sample Screenshot](http://docs.warpspeed.io/assets/img/sample_project_screenshot.png)

## Vagrant Development Environment

This guide assumes that you are using the WarpSpeed Vagrant development environment. Doing so will help you follow best practices and keep your development and production environments as similar as possible.

Throughout this guide commands will need to be run either from within your Virtual Machine (VM) or your local machine environment (outside the VM). Each set of commands will be clearly marked regarding where they should be run. Anytime you need to access your WarpSpeed Vagrant VM, perform the following:

```
# RUN THESE COMMANDS ON YOUR LOCAL MACHINE

# open a terminal and cd to your warpspeed-vagrant directory
cd ~/warpspeed-vagrant

# make sure your VM is running
vagrant up

# SSH into your VM
vagrant ssh
```

## Fork and Clone the Sample Project

The best way to begin using this project is to fork the repository to your own GitHub account. This will allow you to make updates and begin using the project as a template for your own work. To fork the repository, simply click the "Fork" button for this repository.

Once you have forked the repository, you can clone it to your development environment or use pull-deploy to deploy it directly to a server configured with WarpSpeed.io.

To clone the repository to your local machine (not in your VM), perform the following:

```
# RUN THESE COMMANDS ON YOUR LOCAL MACHINE

# access your Sites directory
cd ~/Sites

# clone the forked repository, specifying a name for the directory
git clone git@github.com:YOUR_USERNAME/python-flask-sample.git warpspeed-flask.dev
```

## Create a Database

The sample project uses a MySQL database. This can easily be swapped with an SQLite or PostgreSQL database. To create a MySQL database and user with WarpSpeed, do the following:

```
# RUN THESE COMMANDS IN YOUR VM

# run the db creation command
warpspeed mysql:db tasks_db tasks_user password123
```

This will create a database named "tasks\_db" along with a user, "tasks\_user", that has access via the password "password123". Feel free to change the values to suit your needs (hint: perhaps choosing a better password would be wise).

## Create a WarpSpeed Site

We need to create the appropriate server configuration files to run the site. To configure Nginx and Passenger, perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# run the site creation command
# notice that --force is used because the site directory already exists
warpspeed site:create python warpspeed-flask.dev --force
```

## Create a Virtual Environment

Creating a virtual environment will isolate the libraries for one project from another and is very useful when you have multiple Python applications running on a single server.

To create a virtual environment, perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# make sure you are in the proper site directory
cd ~/sites/warpspeed-flask.dev

# create the virtual environment (on mac/linux)
virtualenv env

# create the virtual environment (on windows)
virtualenv env --always-copy
```

You should now have a folder "env" within your "warpspeed-flask.dev" directory.

## Configure your App Settings

The Flask app needs certain configuration settings that are sensitive, such as an application secret key and your database credentials. These should not be stored in GitHub for obvious reasons. To avoid this, you can use environment variables that get referenced in your app settings. The sample app comes pre-configured this way, so all you need to do is add some new variables into your environment.

### Configuring Nginx and Passenger

Phusion Passenger is used to host your Python site via Nginx. In order to get environment variables to be picked up by Passenger, we need to modify the Nginx configuration file for your site. We also need Passenger to use the virtual environment we created earlier. Perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# open the nginx site configuration file
sudo nano /etc/nginx/sites-available/warpspeed-flask.dev

# uncomment the passenger_python line
# this tells passenger to use the virtual environment you created
passenger_python /home/vagrant/sites/warpspeed-flask.dev/env/bin/python;

# add the following lines below the passenger_python line
# these tell passenger to set the appropriate values in the environment
passenger_env_var DB_NAME tasks_db;
passenger_env_var DB_USER tasks_user;
passenger_env_var DB_PASS password123;
passenger_env_var SECRET_KEY YOUR_SECRET_KEY_HERE;
passenger_env_var DEBUG_MODE True;

# save and exit
```

### Configure Bash Environment

In addition to making your environment variables accessible to Passenger, we also want them to be available via commands run at the command line. To do this, you will need to modify either your "~/.bashrc" or your "~/sites/warpspeed-flask.dev/env/bin/activate" file. We recommend modifying the virtualenv activation file because it keeps your settings specific to this project. Perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# open your virtualenv activation file
nano ~/sites/warpspeed-flask.dev/env/bin/activate

# add the following lines to the top of the file
export DB_NAME=tasks_db
export DB_USER=tasks_user
export DB_PASS=password123
export SECRET_KEY="YOUR_SECRET_KEY_HERE"
export DEBUG_MODE=True

# save and exit
```

Now, whenever you activate your virtualenv, all of your application's environment variables will be available so you can do things like run migrations, etc.

## Install Flask and Run Migrations

We need to install the flask dependencies into our virtual environment and run our database migrations to create the required tables. To do so, perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# make sure you are in the proper site directory
cd ~/sites/warpspeed-flask.dev

# activate your virtualenv
source env/bin/activate

# install flask and other dependencies
pip install -r requirements.txt

# run the database migrations
python manage.py db upgrade

# when you are done with your virtualenv you can run
deactivate
```

If the migrations do not run successfully, it is likely that you have not configured your environment with your database credentials. Please see the "Configure your App Settings" section above for details.

## Add a Hosts File Entry

To access your new Flask site, you will need to add an entry to the hosts file on your machine (not in your VM). To do so, perform the following:

```
# RUN THESE COMMANDS ON YOUR LOCAL MACHINE

# open a terminal and run the following command (for Mac)
sudo nano /etc/hosts

# using git bash or similar, must be run as admin (windows)
notepad /c/Windows/System32/Drivers/etc/hosts

# using command prompt, must be run as admin (windows)
notepad C:\Windows\System32\Drivers\etc\hosts

# add a line that looks like this to the end of the file
192.168.88.10  warpspeed-flask.dev

# save and exit
```

Now, whenever you access "warpspeed-flask.dev" in your web browser, you will be directed to your Flask site within your VM.

## Restart your Site and Celebrate

Finally, we need to reload the site configuration to make all of the changes we made take effect. Perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# reload the site configuration
warpspeed site:reload warpspeed-flask.dev
```

Now, you can access http://warpspeed-flask.dev on your machine to view the site.

## Troubleshooting

If you have issues and need to troubleshoot, you should view the Nginx log file for clues. To do so, perform the following:

```
# RUN THESE COMMANDS IN YOUR VM

# open the nginx error log
sudo nano /var/log/nginx/error.log
```

# License

This sample project is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).

