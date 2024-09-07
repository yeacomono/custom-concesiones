# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
import requests
import frappe
from datetime import timedelta
import calendar


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()

	if filters.get("customer") is not None:
		customer = filters.get("customer")
	else:
		customer = "todos"

	if filters.get("sucursal") is not None:
		sucursal = filters.get("sucursal")
	else:
		sucursal = "todos"

	if filters.get("month") is not None:
		month = filters.get("month")
	else:
		month = "todos"

	if filters.get("year") is not None:
		year = filters.get("year")
	else:
		year = "todos"

	url = "https://horario-salida-qa-erpwin.shalom.com.pe/ventas-abastecimiento-interno/" + customer + "/" + sucursal + "/" + month + "/" + year

	arrayData = requests.get(url)
	arrayData = arrayData.json()

	if "message" in arrayData:
		return columns, arrayData.get("message")

def get_columns():
	columns = [
		{
			'label': "Cliente",
			'fieldname': 'customer',
			'fieldtype': 'Data',
			'width': 100
		},
		{
			'label': "Agencia",
			'fieldname': 'agencia',
			'fieldtype': 'Data',
			'width': 150,
		},
		{
			'label': "Fecha",
			'fieldname': 'posting_date',
			'fieldtype': 'Data',
			'width': 120,
		},
		{
			'label': "Total",
			'fieldname': 'total',
			'fieldtype': 'Data',
			'width': 60,
		},
		{
			'label': "Serie",
			'fieldname': 'series',
			'fieldtype': 'Data',
			'width': 60,
		},
		{
			'label': "Numero",
			'fieldname': 'numeros',
			'fieldtype': 'Data',
			'width': 80,
		},
		{
			'label': "Link Comprobante",
			'fieldname': 'link_pdf',
			'fieldtype': 'Data',
			'width': 150,
		},
		{
			'label': "Id Nota Entrega",
			'fieldname': 'id_nota_entrega',
			'fieldtype': 'Data',
			'width': 150,
		},
		{
			'label': "Id Factura Venta",
			'fieldname': 'id_factura_venta',
			'fieldtype': 'Data',
			'width': 150,
		}
	]
	return columns
