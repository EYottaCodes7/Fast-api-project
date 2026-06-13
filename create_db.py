# import os
# from app.database import Base, engine
# import app.models

# print("Running from:", os.getcwd())
# print("DB URL:", engine.url)

# Base.metadata.create_all(bind=engine)
# print("Done")

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)
print("Database created!")