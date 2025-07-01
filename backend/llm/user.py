from dotenv import load_dotenv
import logging, os, time
import hashlib

def get_client_session():
    load_dotenv()
    if os.environ.get("SESSION_ID") is not None:
        logging.info("Using session_id from environment variable")
        return os.environ.get("SESSION_ID")
    else:
        session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()
        print(session_id)
        return session_id

if __name__ == "__main__":
    session_id = get_client_session()
    print(f"Session ID: {session_id}")
