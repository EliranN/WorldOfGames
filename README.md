# WorldOfGames


Client : 
    pip install -r requirements.txt --user
    python3 MainGame.py

Server:
    Python:
    pip install -r requirements.txt --user
    
    Run:
    docker volume create app
    docker run -d -it -p 8777:8777 -v "$(pwd)":/app --name worldofgames elirann/worldofgames
        
        OR:
        docker-compose up -d

    Test:
        python3 tests/e2e.py <server ip> <port>
            Default port 8777
