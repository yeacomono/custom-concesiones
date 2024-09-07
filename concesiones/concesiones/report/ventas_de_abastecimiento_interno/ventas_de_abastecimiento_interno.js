// Copyright (c) 2016, Marco Bohorquez and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ventas de Abastecimiento Interno"] = {
	"filters": [
		{
			"fieldname": "customer",
			"label": __("Cliente"),
			"fieldtype": "Link",
			"options": "Customer",
			"default": "",
			"width": "150px",
		},
		{
			"fieldname": "sucursal",
			"label": __("Sucursal"),
			"fieldtype": "Link",
			"options": "Branch",
			"width": "100px",
			"default": "",
			"get_query": function() {
				return {
					"filters": {
						"concesionario": 1
					}
				};
			}
		},
		{
			"fieldname": "month",
			"label": __("Mes"),
			"fieldtype": "Select",
			"default": "5",
			"options": [
				{ "value": "todos", "label": __("") },
				{ "value": "1", "label": __("Enero") },
				{ "value": "2", "label": __("Febrero") },
				{ "value": "3", "label": __("Marzo") },
				{ "value": "4", "label": __("Abril") },
				{ "value": "5", "label": __("Mayo") },
				{ "value": "6", "label": __("Junio") },
				{ "value": "7", "label": __("Julio") },
				{ "value": "8", "label": __("Agosto") },
				{ "value": "9", "label": __("Septiembre") },
				{ "value": "10", "label": __("Octubre") },
				{ "value": "11", "label": __("Noviembre") },
				{ "value": "12", "label": __("Diciembre") }
			],
			"width": "100px"
		},
		{
			"fieldname": "year",
			"label": __("Año"),
			"fieldtype": "Select",
			"options": [
				{ "value": "2023", "label": __("2023") },
				{ "value": "2024", "label": __("2024") },
				{ "value": "2025", "label": __("2025") }
			],
			"width": "100px",
			"default": "2024"
		},
	]
};
