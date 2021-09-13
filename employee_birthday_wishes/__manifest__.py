{
	"name": "HR Employee Birthday Wishes",
	"description": "Odoo Website Birthday Reminder module allows to send birthday greetings to customers on their birthday.A cron scheduler is running which help to send birthday greetings automatically to the customer.",
	"depends": ["mail","hr"],
	"author": "Ravi Singh Parihar",
	"version": "14.0.0.1",
	"data": [
		"security/birthday_schduler.xml",
		"views/email_template_view.xml"
	],
	"images": [
		"static/description/bday1.jpg",
		"static/description/bday2.jpg",
	]
	"price": 5,
	"currency": "USD",
	"installable": True,
}