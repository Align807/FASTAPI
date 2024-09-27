# Create a virtual environment 
python -m venv env

# For Windows: env\Scripts\activate

# Install required Python libraries
pip install -r requirements.txt

# Run the FastAPI application
uvicorn app.main:app --reload

go to: http://127.0.0.1:8000/docs to access the FastAPI auto-generated documentation and test the APIs

install docker in the system
start the docker

#check docker is starting properly
docker info

#build docker image
docker build -t fastapi_service .
