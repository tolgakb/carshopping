# Carshopping

In this Django project; images,css and js files are used with the help of static files.
The common parts on each page were collected in a base page and new created pages were extended over base.html.
Code blocks that are contains at each page such as toolbar, navbar and footer are defined on a separate page and included in the needed pages.
With the Django model, table has been created in the database to store the requests for the cars.
With Django authentication, user login, register and logout processes are done.
With Django messages, messages are given to users as a result of successful or unsuccessful login and registration processes.


On the homepage, the vehicles are saved in the database are queried according to the name, model, location, year, car type and price, and the vehicles corresponding to the query are listed.
![Screenshot_1](https://user-images.githubusercontent.com/101968167/230415115-04142c81-d359-46fd-b704-de796963741b.png)

In the Featured cars section, the vehicles are filtered and listed from the last added vehicle to the first added vehicle.

![Screenshot_2](https://user-images.githubusercontent.com/101968167/230415422-f0f12974-0b21-4d6b-9933-696024125884.png)

In the Latest cars section, the vehicles are listed only from the last added vehicle to the first added vehicle.

![Screenshot_3](https://user-images.githubusercontent.com/101968167/230415508-81529c56-cf3e-4767-b6e6-98fb445dbde5.png)

In the Cars section, vehicles are listed from the last added vehicle to the first added vehicle. However, with the paginator process, the information on how many cars will be displayed on each page is specified.
![Screenshot_4](https://user-images.githubusercontent.com/101968167/230415580-4c1dc959-64f6-4940-baae-baed817ae6bd.png)

When the link on the vehicles is clicked, detailed information is given about the vehicles on the detail page.
![Screenshot_8](https://user-images.githubusercontent.com/101968167/230415794-f0a8c78c-156a-41c9-ae22-d8b3c2fa1ae3.png)

In the same way, the search process can be performed according to the special fields of vehicles.
Users can send a message to get information about the vehicles with a form. In the Dashboard, they can access the list of vehicles they have requested inquiry.
![Screenshot_5](https://user-images.githubusercontent.com/101968167/230415662-12965e4a-1c9c-4128-ad6f-3c041ad07e99.png)

There are also authentication functions such as user login, registration, logout.
![Screenshot_6](https://user-images.githubusercontent.com/101968167/230415838-59390f93-c111-41be-aa98-f4db65a6e991.png)
![Screenshot_7](https://user-images.githubusercontent.com/101968167/230415879-f62dc1a1-4bd7-4d92-9f8a-517d56b04348.png)




