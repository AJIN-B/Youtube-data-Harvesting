# Youtube-Data-Harvesting

## Project Descriptions:
#### This app is build for to extract the youtube channel data 
- The problem statement is to create a Streamlit application that allows users to access and analyze data from __YouTube Channels__:
   - Using _**Google API** we retrieve all the relevant data for a _**YouTube channel ID**_.
  
        __| Channel name | Subscribers | Total video count | Playlist ID | Video ID | Likes| Comments of each video |__
   - Store the data in a MongoDB database.
   - Ability to collect data form the YouTube channels and store them in the data lake by clicking a button.

---

<h3 align="left">Languages and Tools:</h3>

<p align="left">
   <!-- Python -->
   <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
   </a>
  
   <!-- Numpy -->
   <a href="https://pytorch.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="Numpy" width="70" height="40"/>
   </a>

   <!-- Pandas -->
   <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/>
   </a>

   <!-- Git -->
   <a href="https://git-scm.com/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/>
   </a>

   <!-- MySQL -->
   <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/>
   </a>
  
   <!-- Streamlit -->
   <a href="https://streamlit.io/" target="_blank" rel="noreferrer">
    <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="streamlit" width="70" height="40"/>
   </a>

   <!-- Youtube -->
   <a href="https://streamlit.io/" target="_blank" rel="noreferrer">
    <img src="https://t3.ftcdn.net/jpg/03/00/38/90/240_F_300389025_b5hgHpjDprTySl8loTqJRMipySb1rO0I.jpg" alt="Youtube" width="70" height="40"/>
   </a>

   <!-- MongoDB -->
   <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/mongodb/mongodb-ar21.svg" alt="MongoDB" width="60" height="40"/>
   </a>

#### To run this app
`python -m streamlit run app.py`  **or**  `streamlit run app.py`

#### NOTE
- provide your api key for the youtube 
- provide your sql user, database name, password.
- provide your mongodb database name.

## Basic Requirements:
- __[Python 3.10](https://docs.python.org/3/)__
- __[googleapiclient](https://developers.google.com/api-client-library)__ 
- __[mysql_connector](https://dev.mysql.com/doc/connector-python/en/)__ 
- __[Pandas](https://pandas.pydata.org/docs/)__
- __[Streamlit](https://docs.streamlit.io/)__
- __[Numpy](https://numpy.org/doc/)__ 
- __[pymongo](https://pymongo.readthedocs.io/en/stable/)__

### **Local Setup**:

1. **Clone the Repository**:
```bash
git clone git@github.com:AJIN-B/Youtube-data-Harvesting.git
cd Youtube-data-Harvesting
```

2. **Set Up a Virtual Environment** (Optional but Recommended):
```bash
# For macOS and Linux:
python3 -m venv venv

# For Windows:
python -m venv venv
```

3. **Activate the Virtual Environment**:
```bash
# For macOS and Linux:
source venv/bin/activate

# For Windows:
.\venv\Scripts\activate
```

4. **Install Required Dependencies**:
```bash
pip install -r requirements.txt
```

5. **Set up the Environment Variables**:

```bash
# add the following Keys

API_KEY="Your Youtube API KEY"

HOST="Your HOST ID"

USER="Your USER ID"

PASSWORD="Your PASSWORD"

PORT="Your PORT"

DATABASE_NAME="Your DATABASE NAME"

```

6. **Run**:
```bash
python -m streamlit run app.py 
or 
streamlit run app.py
```

After running the command, Streamlit will provide a local URL (usually `http://localhost:8501/`) which you can open in your web browser to access application.

