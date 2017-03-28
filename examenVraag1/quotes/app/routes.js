module.exports = function(app) {

	var mongoose = require('mongoose');
	var Quote      = require('./models/Quote');
	var db       = require('../config/db');


	app.get('/index', function(req, res) {
				 if(mongoose.connection.readyState != 1) {
							mongoose.connect(db.url);
					}
				 mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection error:'));
				 var search = req.body.search_input;
				 var quotesList = [];
					Quote.find({}, function(err, quotes) {
								if (err) {
											throw err;
								}
								quotes.forEach( function(q){
									if (q.contains(search)){
										quotesList.add(q);
									}
								})
								return res.render('quuotes', {quotes: quotesList});
					});
	});

	// Get save form for new car
	app.get('/add', function(req, res) {
					res.render('add');
	});

 // Save new car
	app.post('/add', function(req, res) {
		  if(mongoose.connection.readyState != 1) {
				  mongoose.connect(db.url);
		  }
				var quote = new quote({quotes: req.body.quote_input});
				car.save(function (err, quote) {
					  if (err) {
										throw err;
							}
					  return res.redirect('/index');
				});
	});
};
