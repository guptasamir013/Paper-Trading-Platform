# Paper-Trading-Platform

## Installation
1. python -m venv venv
2. venv/Scripts/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver


## Urls
1. All Watchlists: stocks/watchlist/
2. Specific Stock Details: stocks/stock/id/
3. Specific Watchlist Details: stocks/watchliststock/id/
4. Pending Order List: stocks/pendingorder/
5. Executed Order List: stocks/executedorder/
6. Registration: user/register/
7. Login: user/login/
8. Logout: user/logout/
9. Profile: user/profile/

## Description
- The Web Application allows the authenticated user to paper trade on live stock data obtained using web sockets
- The authenticated user can maintain (create; update; delete) his/her personal watchlists to keep track of certain stocks
- Django Framework is used both for Frontend and Backend development with PostgreSQL DB for storing Django-Models
