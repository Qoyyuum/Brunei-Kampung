#!/usr/bin/env python
# encoding: utf-8
import json
from typing import Dict
from flask import Blueprint, jsonify, request

bp = Blueprint('tulus', __name__, url_prefix='/api')

@bp.route('/')
@bp.route('/<district>', methods=["GET"])
@bp.route('/<district>/<mukim>', methods=["GET"])
@bp.route('/<district>/<mukim>/<kampong>', methods=["GET"])
@bp.route('/<district>/<mukim>/<kampong>/<postcode>', methods=["GET"])
def get(district:str=None, mukim:str=None, kampong:str=None, postcode:str=None) -> Dict:
	with open("Tulus/brunei_kampung.json", "r") as data_file:
		data=json.load(data_file)
		if district is not None and district != "search":
			district_filtered_data = [d for d in data if district in d['District']]
			if mukim is not None and district_filtered_data:
				mukim_filtered_data = [m for m in district_filtered_data if mukim in m['Mukim']]
				if kampong is not None and mukim_filtered_data:
					kampong_filtered_data = [k for k in mukim_filtered_data if kampong in k['Kampong']]
					if postcode is not None and kampong_filtered_data:
						postcode_filitered_data = [p for p in kampong_filtered_data if postcode in p['Code']]
						return jsonify({'response' : postcode_filitered_data})
					return jsonify({'response': kampong_filtered_data})
				return jsonify({'response': mukim_filtered_data})
			return jsonify({'response' : district_filtered_data})
		return jsonify({'response':data})


@bp.route('/search/<query>', methods=["GET"])
def wild_search(query):
	"""To allow developers to wildcard search for anything"""
	# TODO: Filter the data based on the query against the entire list and all items.
	with open("Tulus/brunei_kampung.json", "r") as data_file:
		data=json.load(data_file)
		return jsonify({'response': data})