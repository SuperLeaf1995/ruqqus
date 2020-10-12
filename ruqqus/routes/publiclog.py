import mistletoe
from sqlalchemy import func
from bs4 import BeautifulSoup
import pyotp
import qrcode
import io

from ruqqus.helpers.wrappers import *
from ruqqus.helpers.base36 import *
from ruqqus.helpers.sanitize import *
from ruqqus.helpers.filters import *
from ruqqus.classes import *
from ruqqus.classes.publiclog import PublicLog
from flask import *
from ruqqus.__main__ import app, cache, limiter

def log_add(content='', v=None):
	if v == None:
		body = f"A guest {content}."
	else:
		body = f"{v.username} {content}."
	
	log = PublicLog(content=body)
	
	g.db.add(log)
	g.db.commit()
	return True

@app.route("/logs", methods=["GET"])
def log_obtain(v=None):
	max_entries = request.args.get('number')
	if max_entries == None or max_entries < 25:
		max_entries = 50
	
	logs = g.db.query(PublicLog).all()
	
	if (len(logs) > max_entries):
		logs = l1[:max_entries]
	
	for i in range(0,len(logs)):
		logs[i].created_utc = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(logs[i].created_utc))
	
	#return jsonify({'logs':[x.json for x in logs]})
	return render_template('publiclogs-listing.html',logs=logs,v=v)
